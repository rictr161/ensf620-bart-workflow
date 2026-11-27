"""Run the reviewed Cartesian BART reconstruction routes.

The module supports the first implementation block only:

* fully sampled single-channel Cartesian 2D inverse FFT;
* fully sampled single-channel Cartesian 3D inverse FFT; and
* Cartesian 3D compressed-sensing ``pics`` with supplied maps or an explicitly
  requested ``ecalib`` calibration, supporting one ESPIRiT map set.

When requested, it estimates and saves a sampling pattern from the input
k-space. It does not generate phantoms or prepare a new retrospective
undersampling operation.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
import platform
from pathlib import Path
import subprocess
import sys
from typing import Any, Sequence

import numpy as np


MANUAL_CS_PROFILE = "manual-cartesian-3d-cs"
SENSITIVITY_SOURCE_PROVIDED = "provided"
SENSITIVITY_SOURCE_ECALIB = "ecalib"
SAMPLING_SOURCE_PROVIDED = "provided"
SAMPLING_SOURCE_BART_PATTERN = "bart-pattern"
_ECALIB_DEFAULT_KERNEL_SIZE = "6:6:6"
_ECALIB_DEFAULT_THRESHOLD = 0.001
_ECALIB_DEFAULT_CROP = 0.8
_ECALIB_DEFAULT_MAP_SETS = 1
_CS_PROFILE_VALUES = {
    "use_fista": True,
    "wavelet": "dau2",
    "regularization_weight": 0.01,
    "iterations": 100,
    "step": 0.95,
    "disable_random_shift": True,
    "data_scaling": 1.0,
}


@dataclass(frozen=True)
class ReconstructionConfig:
    """Configuration for one supported reconstruction execution."""

    kspace: Path
    output_directory: Path
    spatial_dimensionality: int
    compressed_sensing: bool = False
    bart_executable: str = "bart"
    fft_normalization: str = "unitary"
    sampling_mask: Path | None = None
    sensitivities: Path | None = None
    reconstruction_profile: str | None = None
    pics_use_fista: bool | None = None
    pics_wavelet: str | None = None
    pics_regularization_weight: float | None = None
    pics_iterations: int | None = None
    pics_step: float | None = None
    pics_disable_random_shift: bool | None = None
    pics_data_scaling: float | None = None
    sensitivity_source: str = SENSITIVITY_SOURCE_PROVIDED
    ecalib_calibration_region: str | None = None
    ecalib_kernel_size: str | None = None
    ecalib_threshold: float | None = None
    ecalib_crop: float | None = None
    ecalib_map_sets: int | None = None
    save_figures: bool = False
    sampling_source: str = SAMPLING_SOURCE_PROVIDED


@dataclass(frozen=True)
class ReconstructionResult:
    """Operational result of one workflow execution."""

    exit_code: int
    output_directory: Path | None
    reconstruction: Path | None
    stage_records: Path | None


class WorkflowInputError(ValueError):
    """Raised when supplied inputs or configuration are not supported."""


def read_bart_array(base_path: Path) -> np.ndarray:
    """Read a BART pair after validating its declared shape and binary size.

    Spatial dimensions are read from the header; no fixture-specific dimension
    is imposed. The caller remains responsible for checking route semantics.
    """

    header_path = Path(f"{base_path}.hdr")
    binary_path = Path(f"{base_path}.cfl")
    if not header_path.is_file() or not binary_path.is_file():
        raise WorkflowInputError(
            f"{base_path}: expected readable .hdr and .cfl files"
        )

    try:
        lines = [
            line.strip()
            for line in header_path.read_text(encoding="utf-8").splitlines()
        ]
        dimensions_line = lines[lines.index("# Dimensions") + 1]
        dimensions = tuple(int(value) for value in dimensions_line.split())
    except (OSError, UnicodeError, ValueError, IndexError) as exc:
        raise WorkflowInputError(f"{header_path}: invalid dimensions header") from exc

    if not dimensions or any(dimension <= 0 for dimension in dimensions):
        raise WorkflowInputError(f"{header_path}: dimensions must be positive")

    dtype = np.dtype("<c8")
    expected_bytes = int(np.prod(dimensions, dtype=np.int64)) * dtype.itemsize
    try:
        actual_bytes = binary_path.stat().st_size
    except OSError as exc:
        raise WorkflowInputError(f"{binary_path}: could not read file size") from exc
    if actual_bytes != expected_bytes:
        raise WorkflowInputError(
            f"{binary_path}: expected {expected_bytes} bytes, found {actual_bytes}"
        )

    try:
        values = np.fromfile(binary_path, dtype=dtype)
    except (OSError, ValueError) as exc:
        raise WorkflowInputError(f"{binary_path}: could not read complex data") from exc
    if not np.isfinite(values).all():
        raise WorkflowInputError(f"{binary_path}: non-finite values detected")
    return values.reshape(dimensions, order="F").astype(np.complex128)


def run_reconstruction(config: ReconstructionConfig) -> ReconstructionResult:
    """Run one supported route and record its effective execution.

    The output directory must not already exist. Mandatory stage failures return
    a non-zero result and preserve any files already produced.
    """

    output_directory: Path | None = None
    stage_records_path: Path | None = None
    stage_records: list[dict[str, Any]] = []
    created_by_call = False

    try:
        _validate_configuration(config)
        output_directory = config.output_directory
        reconstruction_path = output_directory / "reconstruction"
        if output_directory.exists():
            raise WorkflowInputError(
                f"output directory already exists; refusing to overwrite or reuse: "
                f"{output_directory}"
            )
        output_directory.mkdir(parents=True, exist_ok=False)
        created_by_call = True
        stage_records_path = output_directory / "stage-records.json"

        try:
            input_values = read_bart_array(config.kspace)
            if config.compressed_sensing:
                _validate_cs_kspace(input_values)
            else:
                _validate_spatial_input(input_values, config)
        except (OSError, WorkflowInputError) as exc:
            _record_stage(
                stage_records,
                "input-inspection",
                "failed",
                1,
                error=str(exc),
                kspace=str(config.kspace),
            )
            raise WorkflowInputError(f"k-space inspection failed: {exc}") from exc
        _record_stage(stage_records, "input-inspection", "success", 0)

        runtime_environment = {
            "python_executable": sys.executable,
            "python_version": platform.python_version(),
            "numpy_version": np.__version__,
            "operating_system": platform.system(),
            "os_release": platform.release(),
            "os_version": platform.version(),
            "architecture": platform.machine(),
            "bart_executable": config.bart_executable,
        }
        bart_version_command = [
            config.bart_executable,
            "version",
            "-V",
        ]
        bart_version_log = output_directory / "bart-version.log"
        (
            bart_version_result,
            bart_version_log_error,
            bart_version_response,
        ) = _run_bart(bart_version_command, bart_version_log)
        _record_stage(
            stage_records,
            "runtime-environment",
            "success" if bart_version_result == 0 else "failed",
            bart_version_result,
            environment=runtime_environment,
            bart_version_command=bart_version_command,
            bart_version_exit_code=bart_version_result,
            bart_version_response=bart_version_response,
            bart_version_log=(
                str(bart_version_log) if bart_version_log_error is None else None
            ),
            bart_version_log_requested=str(bart_version_log),
            bart_version_log_error=bart_version_log_error,
        )
        if bart_version_log_error is not None:
            _record_stage(
                stage_records,
                "bart-version-log",
                "failed",
                1,
                requested_path=str(bart_version_log),
                error=bart_version_log_error,
            )
        if bart_version_result != 0 or bart_version_log_error is not None:
            records_saved = _try_write_stage_records(
                stage_records_path, config, stage_records
            )
            return ReconstructionResult(
                bart_version_result if bart_version_result != 0 else 1,
                output_directory,
                None,
                stage_records_path if records_saved else None,
            )

        effective_settings = _effective_settings(config, output_directory)
        sensitivity_path: Path | None = None
        if config.compressed_sensing:
            sampling_mask_path = Path(effective_settings["sampling_mask"])
            if config.sampling_source == SAMPLING_SOURCE_BART_PATTERN:
                sampling_log = output_directory / "sampling-pattern.log"
                sampling_command = _build_sampling_pattern_command(
                    config, sampling_mask_path
                )
                sampling_result, sampling_log_error, _ = _run_bart(
                    sampling_command, sampling_log
                )
                _record_stage(
                    stage_records,
                    "sampling-pattern-estimation",
                    "success" if sampling_result == 0 else "failed",
                    sampling_result,
                    command=sampling_command,
                    log=str(sampling_log),
                    log_error=sampling_log_error,
                    source=config.sampling_source,
                    kspace=str(config.kspace),
                    requested_output=str(sampling_mask_path),
                    method="BART pattern nonzero k-space support",
                )
                if sampling_log_error is not None:
                    _record_stage(
                        stage_records,
                        "sampling-pattern-log",
                        "failed",
                        1,
                        error=sampling_log_error,
                        log=str(sampling_log),
                    )
                if sampling_result != 0 or sampling_log_error is not None:
                    records_saved = _try_write_stage_records(
                        stage_records_path, config, stage_records
                    )
                    return ReconstructionResult(
                        sampling_result if sampling_result != 0 else 1,
                        output_directory,
                        None,
                        stage_records_path if records_saved else None,
                    )
            try:
                mask_values = read_bart_array(sampling_mask_path)
                _validate_cs_mask_shape(mask_values, input_values)
                _validate_binary_mask(mask_values)
                _validate_masked_kspace(mask_values, input_values)
            except (OSError, WorkflowInputError) as exc:
                _record_stage(
                    stage_records,
                    "sampling-check",
                    "failed",
                    1,
                    error=str(exc),
                    source=config.sampling_source,
                    candidate_path=str(sampling_mask_path),
                )
                raise WorkflowInputError(
                    f"sampling mask validation failed: {exc}"
                ) from exc
            _record_stage(
                stage_records,
                "sampling-check",
                "success",
                0,
                source=config.sampling_source,
                sampling_mask=str(sampling_mask_path),
            )

            if config.sensitivity_source == SENSITIVITY_SOURCE_ECALIB:
                try:
                    _validate_ecalib_compatibility(
                        effective_settings["ecalib"], input_values, mask_values
                    )
                except WorkflowInputError as exc:
                    _record_stage(
                        stage_records,
                        "ecalib-input-check",
                        "failed",
                        1,
                        error=str(exc),
                    )
                    raise
                _record_stage(stage_records, "ecalib-input-check", "success", 0)
                sensitivity_path = output_directory / "sensitivities"
                eigenvalues_path = output_directory / "eigenvalues"
                calibration_log = output_directory / "ecalib.log"
                calibration_command = _build_ecalib_command(
                    config,
                    effective_settings["ecalib"],
                    sensitivity_path,
                    eigenvalues_path,
                )
                calibration_result, calibration_log_error, _ = _run_bart(
                    calibration_command, calibration_log
                )
                _record_stage(
                    stage_records,
                    "ecalib",
                    "success" if calibration_result == 0 else "failed",
                    calibration_result,
                    command=calibration_command,
                    log=str(calibration_log),
                    log_error=calibration_log_error,
                    settings=effective_settings["ecalib"],
                    sensitivities=str(sensitivity_path),
                    eigenvalues=str(eigenvalues_path),
                )
                if calibration_log_error is not None:
                    _record_stage(
                        stage_records,
                        "ecalib-log",
                        "failed",
                        1,
                        error=calibration_log_error,
                        log=str(calibration_log),
                    )
                if calibration_result != 0:
                    records_saved = _try_write_stage_records(
                        stage_records_path, config, stage_records
                    )
                    return ReconstructionResult(
                        calibration_result,
                        output_directory,
                        None,
                        stage_records_path if records_saved else None,
                    )
                if calibration_log_error is not None:
                    records_saved = _try_write_stage_records(
                        stage_records_path, config, stage_records
                    )
                    return ReconstructionResult(
                        1,
                        output_directory,
                        None,
                        stage_records_path if records_saved else None,
                    )

                try:
                    sensitivity_values = read_bart_array(sensitivity_path)
                    eigenvalues = read_bart_array(eigenvalues_path)
                    _validate_sensitivity_maps(sensitivity_values, input_values)
                    _validate_eigenvalues(eigenvalues, input_values)
                except (OSError, WorkflowInputError) as exc:
                    _record_stage(
                        stage_records,
                        "ecalib-output-check",
                        "failed",
                        1,
                        error=str(exc),
                    )
                    raise WorkflowInputError(
                        f"ecalib output validation failed: {exc}"
                    ) from exc
                _record_stage(
                    stage_records, "ecalib-output-check", "success", 0
                )
            else:
                if config.sensitivities is None:
                    raise WorkflowInputError(
                        "the provided sensitivity source requires --sensitivities"
                    )
                sensitivity_path = config.sensitivities
                try:
                    sensitivity_values = read_bart_array(sensitivity_path)
                    _validate_sensitivity_maps(sensitivity_values, input_values)
                except (OSError, WorkflowInputError) as exc:
                    _record_stage(
                        stage_records,
                        "sensitivity-map-check",
                        "failed",
                        1,
                        error=str(exc),
                        sensitivities=str(sensitivity_path),
                    )
                    raise WorkflowInputError(
                        f"sensitivity-map validation failed: {exc}"
                    ) from exc
                _record_stage(
                    stage_records,
                    "sensitivity-map-check",
                    "success",
                    0,
                    sensitivities=str(sensitivity_path),
                )
            _record_stage(
                stage_records,
                "sampling-and-sensitivity-checks",
                "success",
                0,
            )
        else:
            _record_stage(
                stage_records,
                "sampling-and-sensitivity-checks",
                "not-required",
                0,
            )

        command = _build_command(
            config,
            effective_settings,
            reconstruction_path,
            sensitivity_path,
        )
        reconstruction_log = output_directory / "reconstruction.log"
        command_result, log_error, _ = _run_bart(command, reconstruction_log)
        _record_stage(
            stage_records,
            "reconstruction",
            "success" if command_result == 0 else "failed",
            command_result,
            command=command,
            log=str(reconstruction_log),
            settings=effective_settings,
            log_error=log_error,
        )
        if log_error is not None:
            _record_stage(
                stage_records,
                "reconstruction-log",
                "failed",
                1,
                error=log_error,
                log=str(reconstruction_log),
            )
        if command_result != 0:
            records_saved = _try_write_stage_records(
                stage_records_path, config, stage_records
            )
            return ReconstructionResult(
                command_result,
                output_directory,
                None,
                stage_records_path if records_saved else None,
            )
        if log_error is not None:
            records_saved = _try_write_stage_records(
                stage_records_path, config, stage_records
            )
            return ReconstructionResult(
                1,
                output_directory,
                None,
                stage_records_path if records_saved else None,
            )

        try:
            output_values = read_bart_array(reconstruction_path)
            if config.compressed_sensing:
                _validate_cs_reconstruction(output_values, input_values)
            else:
                _validate_spatial_input(output_values, config)
                _validate_output_shape(output_values, input_values, config)
        except (OSError, WorkflowInputError) as exc:
            _record_stage(
                stage_records,
                "reconstruction-output-check",
                "failed",
                1,
                error=str(exc),
                reconstruction=str(reconstruction_path),
            )
            raise WorkflowInputError(
                f"reconstruction output validation failed: {exc}"
            ) from exc
        _record_stage(stage_records, "reconstruction-output-check", "success", 0)
        if config.save_figures:
            figure_path = output_directory / "figures" / "reconstruction.png"
            presentation: dict[str, Any] = {
                "spatial_dimensionality": config.spatial_dimensionality,
                "colormap": "gray",
                "origin": "lower",
                "aspect": "equal",
                "interpolation": "none",
                "transpose_each_plane": True,
                "dpi": 160,
            }
            try:
                panels, presentation = _prepare_reconstruction_figure(
                    output_values, config.spatial_dimensionality
                )
                _save_reconstruction_figure(
                    figure_path, panels, presentation
                )
            except (ImportError, OSError, RuntimeError, ValueError) as exc:
                _record_stage(
                    stage_records,
                    "reconstruction-figure",
                    "failed",
                    1,
                    destination=str(figure_path),
                    presentation=presentation,
                    error=str(exc),
                )
                _report_warning(
                    "optional reconstruction figure generation failed; the "
                    "reconstruction remains valid. The destination was not "
                    f"confirmed as saved: {figure_path}: {exc}"
                )
            else:
                _record_stage(
                    stage_records,
                    "reconstruction-figure",
                    "success",
                    0,
                    path=str(figure_path),
                    presentation=presentation,
                )
        if not _try_write_stage_records(stage_records_path, config, stage_records):
            return ReconstructionResult(1, output_directory, None, None)
        return ReconstructionResult(
            0, output_directory, reconstruction_path, stage_records_path
        )
    except (OSError, WorkflowInputError) as exc:
        _report_error(str(exc))
        if created_by_call and output_directory is not None:
            if stage_records_path is None:
                stage_records_path = output_directory / "stage-records.json"
            _record_stage(stage_records, "workflow", "failed", 1, error=str(exc))
            if not _try_write_stage_records(stage_records_path, config, stage_records):
                stage_records_path = None
        return ReconstructionResult(
            1, output_directory, None, stage_records_path
        )


def _validate_configuration(config: ReconstructionConfig) -> None:
    if not isinstance(config, ReconstructionConfig):
        raise WorkflowInputError("configuration must be a ReconstructionConfig")
    if not isinstance(config.spatial_dimensionality, int) or isinstance(
        config.spatial_dimensionality, bool
    ):
        raise WorkflowInputError("spatial dimensionality must be an integer")
    if config.spatial_dimensionality not in (2, 3):
        raise WorkflowInputError("spatial dimensionality must be 2 or 3")
    if not isinstance(config.compressed_sensing, bool):
        raise WorkflowInputError("compressed sensing selection must be boolean")
    if not isinstance(config.save_figures, bool):
        raise WorkflowInputError("figure-generation selection must be boolean")
    if not isinstance(config.sampling_source, str) or config.sampling_source not in (
        SAMPLING_SOURCE_PROVIDED,
        SAMPLING_SOURCE_BART_PATTERN,
    ):
        raise WorkflowInputError(
            "sampling source must be 'provided' or 'bart-pattern'"
        )
    if not isinstance(config.fft_normalization, str):
        raise WorkflowInputError("FFT normalization must be a string")
    if config.fft_normalization != "unitary":
        raise WorkflowInputError(
            "the reviewed FFT routes currently support only unitary normalization"
        )
    if not isinstance(config.kspace, Path):
        raise WorkflowInputError("k-space must be a non-null pathlib.Path")
    if not isinstance(config.output_directory, Path):
        raise WorkflowInputError("output directory must be a non-null pathlib.Path")
    for path, label in (
        (config.sampling_mask, "sampling mask"),
        (config.sensitivities, "sensitivities"),
    ):
        if path is not None and not isinstance(path, Path):
            raise WorkflowInputError(f"{label} must be a pathlib.Path or None")
    if not isinstance(config.bart_executable, str) or not config.bart_executable:
        raise WorkflowInputError("BART executable must be a non-empty string")
    if config.reconstruction_profile is not None and (
        not isinstance(config.reconstruction_profile, str)
        or config.reconstruction_profile != MANUAL_CS_PROFILE
    ):
        raise WorkflowInputError(
            f"unsupported reconstruction profile: {config.reconstruction_profile!r}"
        )
    if config.spatial_dimensionality == 2 and config.compressed_sensing:
        raise WorkflowInputError(
            "Cartesian 2D compressed sensing is not implemented in this block"
        )
    if config.compressed_sensing and config.spatial_dimensionality != 3:
        raise WorkflowInputError(
            "the reviewed compressed-sensing route currently requires 3D input"
        )
    if not isinstance(config.sensitivity_source, str) or config.sensitivity_source not in (
        SENSITIVITY_SOURCE_PROVIDED,
        SENSITIVITY_SOURCE_ECALIB,
    ):
        raise WorkflowInputError(
            "sensitivity source must be 'provided' or 'ecalib'"
        )
    ecalib_options = (
        config.ecalib_calibration_region,
        config.ecalib_kernel_size,
        config.ecalib_threshold,
        config.ecalib_crop,
        config.ecalib_map_sets,
    )
    if config.compressed_sensing:
        if config.sampling_source == SAMPLING_SOURCE_PROVIDED:
            if config.sampling_mask is None:
                raise WorkflowInputError(
                    "sampling source 'provided' requires --sampling-mask"
                )
        elif config.sampling_mask is not None:
            raise WorkflowInputError(
                "--sampling-mask cannot be combined with sampling source "
                "'bart-pattern'"
            )
        _resolve_cs_settings(config)
        if config.sensitivity_source == SENSITIVITY_SOURCE_PROVIDED:
            if config.sensitivities is None:
                raise WorkflowInputError(
                    "the provided sensitivity source requires --sensitivities"
                )
            if any(value is not None for value in ecalib_options):
                raise WorkflowInputError(
                    "ecalib options are only accepted when sensitivity source is ecalib"
                )
        else:
            if config.sensitivities is not None:
                raise WorkflowInputError(
                    "do not provide --sensitivities when sensitivity source is ecalib"
                )
            _resolve_ecalib_settings(config)
    elif (
        config.sampling_mask is not None
        or config.sampling_source != SAMPLING_SOURCE_PROVIDED
        or config.sensitivities is not None
        or config.sensitivity_source != SENSITIVITY_SOURCE_PROVIDED
        or any(value is not None for value in ecalib_options)
        or config.reconstruction_profile is not None
        or any(
            value is not None
            for value in (
                config.pics_use_fista,
                config.pics_wavelet,
                config.pics_regularization_weight,
                config.pics_iterations,
                config.pics_step,
                config.pics_disable_random_shift,
                config.pics_data_scaling,
            )
        )
    ):
        raise WorkflowInputError(
            "sampling masks and non-default sampling sources, sensitivity, "
            "calibration, profiles, and pics options are only accepted for "
            "the CS route"
        )


def _resolve_ecalib_settings(config: ReconstructionConfig) -> dict[str, Any]:
    region = _parse_positive_triplet(
        config.ecalib_calibration_region, "ecalib calibration region"
    )
    kernel_value = (
        _ECALIB_DEFAULT_KERNEL_SIZE
        if config.ecalib_kernel_size is None
        else config.ecalib_kernel_size
    )
    kernel = _parse_positive_triplet(kernel_value, "ecalib kernel size")
    threshold = (
        _ECALIB_DEFAULT_THRESHOLD
        if config.ecalib_threshold is None
        else config.ecalib_threshold
    )
    crop = (
        _ECALIB_DEFAULT_CROP
        if config.ecalib_crop is None
        else config.ecalib_crop
    )
    map_sets = (
        _ECALIB_DEFAULT_MAP_SETS
        if config.ecalib_map_sets is None
        else config.ecalib_map_sets
    )

    for value, label in ((threshold, "threshold"), (crop, "crop")):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise WorkflowInputError(f"ecalib {label} must be numeric")
        if not np.isfinite(value):
            raise WorkflowInputError(f"ecalib {label} must be finite")
    if not 0 <= threshold < 1:
        raise WorkflowInputError("ecalib threshold must satisfy 0 <= threshold < 1")
    if crop < 0 or crop > 1:
        raise WorkflowInputError("ecalib crop must be between 0 and 1")
    if not isinstance(map_sets, int) or isinstance(map_sets, bool) or map_sets <= 0:
        raise WorkflowInputError("ecalib map-set count must be a positive integer")
    if map_sets != 1:
        raise WorkflowInputError(
            "multiple ESPIRiT map sets are not supported; use exactly one"
        )
    return {
        "calibration_region": ":".join(str(value) for value in region),
        "kernel_size": ":".join(str(value) for value in kernel),
        "threshold": float(threshold),
        "crop": float(crop),
        "map_sets": map_sets,
    }


def _parse_positive_triplet(value: str | None, label: str) -> tuple[int, int, int]:
    if not isinstance(value, str) or not value:
        raise WorkflowInputError(f"{label} must be specified as three positive integers")
    parts = value.split(":")
    if len(parts) != 3:
        raise WorkflowInputError(
            f"{label} must be specified as three positive integers"
        )
    try:
        values = (int(parts[0]), int(parts[1]), int(parts[2]))
    except ValueError as exc:
        raise WorkflowInputError(
            f"{label} must be specified as three positive integers"
        ) from exc
    if any(item <= 0 for item in values):
        raise WorkflowInputError(
            f"{label} must be specified as three positive integers"
        )
    return values


def _validate_ecalib_compatibility(
    settings: dict[str, Any], kspace: np.ndarray, mask: np.ndarray
) -> None:
    spatial_shape = kspace.shape[:3]
    region_size = _parse_positive_triplet(
        settings["calibration_region"], "ecalib calibration region"
    )
    kernel_size = _parse_positive_triplet(
        settings["kernel_size"], "ecalib kernel size"
    )
    for dimensions, label, parameter in (
        (region_size, "calibration region", settings["calibration_region"]),
        (kernel_size, "kernel size", settings["kernel_size"]),
    ):
        if any(size > available for size, available in zip(dimensions, spatial_shape)):
            raise WorkflowInputError(
                f"ecalib {label} {parameter} exceeds k-space spatial dimensions "
                f"{spatial_shape}"
            )
    if any(kernel > region for kernel, region in zip(kernel_size, region_size)):
        raise WorkflowInputError(
            "each ecalib kernel dimension must not exceed its calibration-region "
            "dimension"
        )
    if any(
        available > 1 and kernel == 1
        for available, kernel in zip(spatial_shape, kernel_size)
    ):
        raise WorkflowInputError(
            "this reconstruction route requires sensitivity maps with the full "
            "spatial shape of k-space; kernel size 1 is unsupported on spatial "
            "axes larger than 1"
        )
    starts = tuple(
        (available - requested) // 2
        for available, requested in zip(spatial_shape, region_size)
    )
    calibration_region = mask.reshape(spatial_shape, order="F")[
        tuple(
            slice(start, start + requested)
            for start, requested in zip(starts, region_size)
        )
    ]
    if not np.all(calibration_region == 1):
        raise WorkflowInputError(
            "the configured ecalib calibration region is not fully sampled by "
            "the effective sampling mask"
        )


def _validate_spatial_input(values: np.ndarray, config: ReconstructionConfig) -> None:
    spatial_dimensions = values.shape[: config.spatial_dimensionality]
    if len(spatial_dimensions) != config.spatial_dimensionality:
        raise WorkflowInputError("input does not contain the declared spatial axes")
    if any(dimension != 1 for dimension in values.shape[config.spatial_dimensionality :]):
        raise WorkflowInputError(
            "the supported single-channel route requires trailing singleton axes"
        )
    if not np.isfinite(values).all():
        raise WorkflowInputError("input contains non-finite values")


def _validate_binary_mask(mask: np.ndarray) -> None:
    if not np.isin(mask, (0 + 0j, 1 + 0j)).all():
        raise WorkflowInputError("sampling mask must contain only 0 + 0j and 1 + 0j")
    if np.count_nonzero(mask) == 0 or np.count_nonzero(mask) == mask.size:
        raise WorkflowInputError(
            "sampling mask must contain both acquired and omitted positions"
        )


def _axis_size(values: np.ndarray, axis: int) -> int:
    return values.shape[axis] if axis < values.ndim else 1


def _validate_cs_kspace(values: np.ndarray) -> None:
    if values.ndim < 3:
        raise WorkflowInputError("Cartesian 3D CS k-space must have three spatial axes")
    if _axis_size(values, 3) < 1:
        raise WorkflowInputError("k-space must have a positive channel dimension")
    if _axis_size(values, 4) != 1 or any(size != 1 for size in values.shape[5:]):
        raise WorkflowInputError(
            "Cartesian 3D CS supports one map set and requires later axes to be singleton"
        )


def _validate_cs_mask_shape(mask: np.ndarray, kspace: np.ndarray) -> None:
    if mask.ndim < 3 or mask.shape[:3] != kspace.shape[:3]:
        raise WorkflowInputError(
            f"sampling mask spatial shape {mask.shape[:3]} does not match "
            f"k-space spatial shape {kspace.shape[:3]}"
        )
    if any(size != 1 for size in mask.shape[3:]):
        raise WorkflowInputError(
            "the CS sampling mask must be spatial and singleton on all later axes"
        )


def _validate_masked_kspace(mask: np.ndarray, kspace: np.ndarray) -> None:
    spatial_shape = tuple(kspace.shape[:3])
    channel_count = _axis_size(kspace, 3)
    spatial_mask = mask.reshape(spatial_shape, order="F")
    channel_kspace = kspace.reshape(
        (*spatial_shape, channel_count), order="F"
    )
    if np.any((spatial_mask == 0)[..., np.newaxis] & (channel_kspace != 0)):
        raise WorkflowInputError(
            "k-space contains non-zero values at positions omitted by the mask"
        )


def _validate_sensitivity_maps(
    sensitivities: np.ndarray, kspace: np.ndarray
) -> None:
    if sensitivities.ndim < 3 or sensitivities.shape[:3] != kspace.shape[:3]:
        raise WorkflowInputError(
            f"sensitivity spatial shape {sensitivities.shape[:3]} does not match "
            f"k-space spatial shape {kspace.shape[:3]}"
        )
    if _axis_size(sensitivities, 3) != _axis_size(kspace, 3):
        raise WorkflowInputError(
            "sensitivity channel dimension does not match k-space channels"
        )
    if _axis_size(sensitivities, 4) != 1 or any(
        size != 1 for size in sensitivities.shape[5:]
    ):
        raise WorkflowInputError(
            "exactly one ESPIRiT map set is supported; later axes must be singleton"
        )
    if not np.any(sensitivities != 0):
        raise WorkflowInputError("sensitivity maps are completely zero")


def _validate_eigenvalues(eigenvalues: np.ndarray, kspace: np.ndarray) -> None:
    if eigenvalues.ndim < 3 or eigenvalues.shape[:3] != kspace.shape[:3]:
        raise WorkflowInputError(
            f"eigenvalue spatial shape {eigenvalues.shape[:3]} does not match "
            f"k-space spatial shape {kspace.shape[:3]}"
        )
    if any(size != 1 for size in eigenvalues.shape[3:]):
        raise WorkflowInputError(
            "eigenvalues must correspond to the single supported map set"
        )


def _validate_cs_reconstruction(output: np.ndarray, kspace: np.ndarray) -> None:
    if output.ndim < 3 or output.shape[:3] != kspace.shape[:3]:
        raise WorkflowInputError(
            f"reconstruction spatial shape {output.shape[:3]} does not match "
            f"k-space spatial shape {kspace.shape[:3]}"
        )
    if any(size != 1 for size in output.shape[3:]):
        raise WorkflowInputError(
            "the supported CS reconstruction output must have one map set and "
            "singleton later axes"
        )


def _normalized_shape(
    values: np.ndarray, minimum_axes: int = 0
) -> tuple[int, ...]:
    shape = values.shape
    end = len(shape)
    while end > minimum_axes and shape[end - 1] == 1:
        end -= 1
    return shape[:end]


def _validate_output_shape(
    output: np.ndarray, input_values: np.ndarray, config: ReconstructionConfig
) -> None:
    input_shape = _normalized_shape(input_values, config.spatial_dimensionality)
    output_shape = _normalized_shape(output, config.spatial_dimensionality)
    if output_shape != input_shape:
        raise WorkflowInputError(
            f"reconstruction shape {output_shape} does not match input shape "
            f"{input_shape}"
        )
    if output_shape[: config.spatial_dimensionality] != input_shape[
        : config.spatial_dimensionality
    ]:
        raise WorkflowInputError("reconstruction spatial shape does not match input")


def _prepare_reconstruction_figure(
    values: np.ndarray, spatial_dimensionality: int
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    spatial_shape = tuple(values.shape[:spatial_dimensionality])
    magnitude = np.abs(values.reshape(spatial_shape, order="F"))
    maximum_magnitude = float(np.max(magnitude))
    zero_magnitude = maximum_magnitude == 0.0
    display_maximum = 1.0 if zero_magnitude else maximum_magnitude

    if spatial_dimensionality == 2:
        panels = [
            {
                "title": "Full 2D reconstruction",
                "values": magnitude,
                "horizontal_axis": 0,
                "vertical_axis": 1,
            }
        ]
        center_indices: list[int] | None = None
    else:
        center_indices = [size // 2 for size in spatial_shape]
        center_0, center_1, center_2 = center_indices
        panels = [
            {
                "title": f"Array axes 0 and 1; axis 2 index {center_2}",
                "values": magnitude[:, :, center_2],
                "horizontal_axis": 0,
                "vertical_axis": 1,
            },
            {
                "title": f"Array axes 0 and 2; axis 1 index {center_1}",
                "values": magnitude[:, center_1, :],
                "horizontal_axis": 0,
                "vertical_axis": 2,
            },
            {
                "title": f"Array axes 1 and 2; axis 0 index {center_0}",
                "values": magnitude[center_0, :, :],
                "horizontal_axis": 1,
                "vertical_axis": 2,
            },
        ]

    presentation = {
        "spatial_shape": list(spatial_shape),
        "center_indices": center_indices,
        "magnitude_limits": {"vmin": 0.0, "vmax": display_maximum},
        "maximum_magnitude": maximum_magnitude,
        "zero_magnitude_fallback": zero_magnitude,
        "colormap": "gray",
        "origin": "lower",
        "aspect": "equal",
        "interpolation": "none",
        "transpose_each_plane": True,
        "dpi": 160,
        "figure_size_inches": (
            [6.5, 6.5] if len(panels) == 1 else [13.0, 4.5]
        ),
        "views": [
            {
                "title": panel["title"],
                "horizontal_axis": panel["horizontal_axis"],
                "vertical_axis": panel["vertical_axis"],
            }
            for panel in panels
        ],
    }
    return panels, presentation


def _save_reconstruction_figure(
    path: Path,
    panels: list[dict[str, Any]],
    presentation: dict[str, Any],
) -> None:
    import matplotlib
    presentation["matplotlib_version"] = matplotlib.__version__

    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.figure import Figure

    path.parent.mkdir(exist_ok=False)
    figure = Figure(
        figsize=tuple(presentation["figure_size_inches"]),
        dpi=presentation["dpi"],
        constrained_layout=True,
    )
    canvas = FigureCanvasAgg(figure)
    axes = figure.subplots(1, len(panels), squeeze=False).ravel()
    images = []
    limits = presentation["magnitude_limits"]
    for axis, panel in zip(axes, panels):
        image = axis.imshow(
            panel["values"].T,
            cmap=presentation["colormap"],
            origin=presentation["origin"],
            aspect=presentation["aspect"],
            interpolation=presentation["interpolation"],
            vmin=limits["vmin"],
            vmax=limits["vmax"],
        )
        images.append(image)
        axis.set_title(panel["title"])
        axis.set_xlabel(f"Array axis {panel['horizontal_axis']} index")
        axis.set_ylabel(f"Array axis {panel['vertical_axis']} index")
    figure.colorbar(images[-1], ax=axes, label="Magnitude")

    with path.open("xb") as figure_file:
        canvas.print_png(figure_file)
    if not path.is_file() or path.stat().st_size == 0:
        raise OSError(f"figure output was not saved as a non-empty PNG: {path}")


def _resolve_cs_settings(config: ReconstructionConfig) -> dict[str, Any]:
    values = dict(_CS_PROFILE_VALUES) if config.reconstruction_profile == MANUAL_CS_PROFILE else {}
    overrides = {
        "use_fista": config.pics_use_fista,
        "wavelet": config.pics_wavelet,
        "regularization_weight": config.pics_regularization_weight,
        "iterations": config.pics_iterations,
        "step": config.pics_step,
        "disable_random_shift": config.pics_disable_random_shift,
        "data_scaling": config.pics_data_scaling,
    }
    values.update({key: value for key, value in overrides.items() if value is not None})
    missing = [key for key in overrides if key not in values]
    if missing:
        raise WorkflowInputError(
            "CS settings are incomplete; provide explicit values or the reviewed "
            f"profile: {', '.join(missing)}"
        )
    if not isinstance(values["use_fista"], bool):
        raise WorkflowInputError("CS FISTA selection must be boolean")
    if not isinstance(values["wavelet"], str) or not values["wavelet"]:
        raise WorkflowInputError("CS wavelet must be a non-empty string")
    for key in ("regularization_weight", "step", "data_scaling"):
        value = values[key]
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise WorkflowInputError(f"CS {key} must be numeric")
        if not np.isfinite(value) or value <= 0:
            raise WorkflowInputError(f"CS {key} must be finite and positive")
    iterations = values["iterations"]
    if not isinstance(iterations, int) or isinstance(iterations, bool) or iterations <= 0:
        raise WorkflowInputError("CS iterations must be a positive integer")
    if not isinstance(values["disable_random_shift"], bool):
        raise WorkflowInputError("CS random-shift selection must be boolean")
    return values


def _effective_settings(
    config: ReconstructionConfig, output_directory: Path
) -> dict[str, Any]:
    sampling_mask_path: Path | None = None
    sampling_estimation: dict[str, str] | None = None
    if config.compressed_sensing:
        if config.sampling_source == SAMPLING_SOURCE_PROVIDED:
            sampling_mask_path = config.sampling_mask
        else:
            sampling_mask_path = output_directory / "sampling_mask"
            sampling_estimation = {
                "method": "BART pattern nonzero k-space support",
                "kspace": str(config.kspace),
            }
    settings: dict[str, Any] = {
        "spatial_dimensionality": config.spatial_dimensionality,
        "compressed_sensing": config.compressed_sensing,
        "fft_normalization": config.fft_normalization,
        "save_figures": config.save_figures,
        "kspace": str(config.kspace),
        "sampling_source": config.sampling_source,
        "sampling_mask": (
            str(sampling_mask_path) if sampling_mask_path is not None else None
        ),
        "sampling_estimation": sampling_estimation,
        "sensitivity_source": config.sensitivity_source,
        "sensitivities": (
            str(config.sensitivities)
            if config.sensitivities is not None
            else (
                str(output_directory / "sensitivities")
                if config.sensitivity_source == SENSITIVITY_SOURCE_ECALIB
                else None
            )
        ),
        "reconstruction_profile": config.reconstruction_profile,
    }
    if config.compressed_sensing:
        settings["pics"] = _resolve_cs_settings(config)
    if config.sensitivity_source == SENSITIVITY_SOURCE_ECALIB:
        settings["ecalib"] = _resolve_ecalib_settings(config)
        settings["eigenvalues"] = str(output_directory / "eigenvalues")
    return settings


def _build_sampling_pattern_command(
    config: ReconstructionConfig, sampling_mask_path: Path
) -> list[str]:
    return [
        config.bart_executable,
        "pattern",
        str(config.kspace),
        str(sampling_mask_path),
    ]


def _build_ecalib_command(
    config: ReconstructionConfig,
    settings: dict[str, Any],
    sensitivity_path: Path,
    eigenvalues_path: Path,
) -> list[str]:
    return [
        config.bart_executable,
        "ecalib",
        "-r",
        settings["calibration_region"],
        "-k",
        settings["kernel_size"],
        "-t",
        str(settings["threshold"]),
        "-c",
        str(settings["crop"]),
        "-m",
        str(settings["map_sets"]),
        str(config.kspace),
        str(sensitivity_path),
        str(eigenvalues_path),
    ]


def _build_command(
    config: ReconstructionConfig,
    settings: dict[str, Any],
    reconstruction_path: Path,
    sensitivity_path: Path | None,
) -> list[str]:
    if not config.compressed_sensing:
        axes = "3" if config.spatial_dimensionality == 2 else "7"
        return [
            str(config.bart_executable),
            "fft",
            "-i",
            "-u",
            axes,
            str(config.kspace),
            str(reconstruction_path),
        ]

    pics = settings["pics"]
    regularization = f"W:7:0:{pics['regularization_weight']}"
    sampling_mask_path = settings["sampling_mask"]
    if sampling_mask_path is None or sensitivity_path is None:
        raise WorkflowInputError(
            "CS reconstruction requires a sampling mask and sensitivity maps"
        )
    command = [str(config.bart_executable), "pics"]
    if pics["use_fista"]:
        command.append("--fista")
    command.extend(
        [
            "--wavelet",
            str(pics["wavelet"]),
            "-R",
            regularization,
            "-i",
            str(pics["iterations"]),
            "-s",
            str(pics["step"]),
        ]
    )
    if pics["disable_random_shift"]:
        command.append("-n")
    command.extend(
        [
            "-w",
            str(pics["data_scaling"]),
            "-p",
            str(sampling_mask_path),
            str(config.kspace),
            str(sensitivity_path),
            str(reconstruction_path),
        ]
    )
    return command


def _run_bart(
    command: Sequence[str], log_path: Path
) -> tuple[int, str | None, str | None]:
    try:
        completed = subprocess.run(
            list(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
        )
    except OSError as exc:
        _report_error(f"BART could not be invoked: {exc}")
        log_error = _try_write_text(log_path, f"ERROR: {exc}\n")
        if log_error:
            _report_error(f"BART invocation diagnostic could not be saved: {log_error}")
        return 1, log_error, None
    log_error = _try_write_text(
        log_path,
        f"Command: {json.dumps(list(command))}\n"
        f"Exit code: {completed.returncode}\n"
        f"{completed.stdout}",
    )
    if log_error:
        _report_error(
            f"BART returned exit code {completed.returncode}, but its log could "
            f"not be saved: {log_error}"
        )
    elif completed.returncode != 0:
        _report_error(f"BART returned exit code {completed.returncode}")
    return completed.returncode, log_error, completed.stdout


def _record_stage(
    stage_records: list[dict[str, Any]],
    stage: str,
    status: str,
    exit_code: int,
    **details: Any,
) -> None:
    stage_records.append(
        {"stage": stage, "status": status, "exit_code": exit_code, **details}
    )


def _write_stage_records(
    path: Path, config: ReconstructionConfig, records: list[dict[str, Any]]
) -> None:
    payload = {
        "configuration": _jsonable(asdict(config)),
        "stages": records,
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _try_write_stage_records(
    path: Path, config: ReconstructionConfig, records: list[dict[str, Any]]
) -> bool:
    try:
        _write_stage_records(path, config, records)
    except (OSError, TypeError, ValueError) as exc:
        _report_error(f"could not save stage records at {path}: {exc}")
        return False
    return True


def _try_write_text(path: Path, content: str) -> str | None:
    try:
        path.write_text(content, encoding="utf-8")
    except OSError as exc:
        return str(exc)
    return None


def _report_error(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def _report_warning(message: str) -> None:
    print(f"WARNING: {message}", file=sys.stderr)


def _jsonable(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, tuple):
        return [_jsonable(item) for item in value]
    if isinstance(value, dict):
        return {key: _jsonable(item) for key, item in value.items()}
    return value


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run one supported Cartesian BART reconstruction route."
    )
    parser.add_argument("--kspace", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    parser.add_argument("--spatial-dimensionality", type=int, choices=(2, 3), required=True)
    parser.add_argument("--compressed-sensing", action="store_true")
    parser.add_argument("--bart-executable", default="bart")
    parser.add_argument("--fft-normalization", default="unitary")
    parser.add_argument("--sampling-mask", type=Path)
    parser.add_argument(
        "--sampling-source",
        choices=(SAMPLING_SOURCE_PROVIDED, SAMPLING_SOURCE_BART_PATTERN),
        default=SAMPLING_SOURCE_PROVIDED,
    )
    parser.add_argument("--sensitivities", type=Path)
    parser.add_argument(
        "--sensitivity-source",
        choices=(SENSITIVITY_SOURCE_PROVIDED, SENSITIVITY_SOURCE_ECALIB),
        default=SENSITIVITY_SOURCE_PROVIDED,
    )
    parser.add_argument("--ecalib-calibration-region")
    parser.add_argument("--ecalib-kernel-size")
    parser.add_argument("--ecalib-threshold", type=float)
    parser.add_argument("--ecalib-crop", type=float)
    parser.add_argument("--ecalib-map-sets", type=int)
    parser.add_argument("--reconstruction-profile", choices=(MANUAL_CS_PROFILE,))
    parser.add_argument("--pics-use-fista", action=argparse.BooleanOptionalAction)
    parser.add_argument("--pics-wavelet")
    parser.add_argument("--pics-regularization-weight", type=float)
    parser.add_argument("--pics-iterations", type=int)
    parser.add_argument("--pics-step", type=float)
    parser.add_argument("--pics-disable-random-shift", action=argparse.BooleanOptionalAction)
    parser.add_argument("--pics-data-scaling", type=float)
    parser.add_argument("--save-figures", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    result = run_reconstruction(ReconstructionConfig(**vars(args)))
    if result.exit_code != 0:
        if result.stage_records is None:
            print("ERROR: reconstruction workflow failed; no diagnostic record was saved", file=sys.stderr)
        else:
            print(
                f"ERROR: reconstruction workflow failed; see {result.stage_records}",
                file=sys.stderr,
            )
    else:
        print(f"SUCCESS: reconstruction written to {result.reconstruction}")
    return result.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
