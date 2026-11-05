"""Validate one BART 64 x 64 x 64 data pair."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np


SPATIAL_SHAPE = (64, 64, 64)
VALID_PAIRS = ("reference", "kspace", "reconstruction")
COMPLEX64 = np.dtype("<c8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate one BART 64 x 64 x 64 data pair."
    )
    parser.add_argument(
        "preparation_directory",
        type=Path,
        help="Directory containing the selected BART .hdr and .cfl pair.",
    )
    parser.add_argument(
        "pair",
        choices=VALID_PAIRS,
        help="Pair to validate: reference, kspace, or reconstruction.",
    )
    return parser.parse_args()


def read_dimensions(header: Path) -> tuple[int, ...]:
    lines = [line.strip() for line in header.read_text().splitlines()]
    try:
        dimensions = lines[lines.index("# Dimensions") + 1].split()
        return tuple(int(value) for value in dimensions)
    except (ValueError, IndexError) as exc:
        raise ValueError(f"{header}: invalid dimensions header") from exc


def read_bart_3d(name: str) -> np.ndarray:
    """Read and validate one BART 64 x 64 x 64 volume."""
    base_path = Path(name)
    header = Path(f"{base_path}.hdr")
    binary = Path(f"{base_path}.cfl")
    if not header.is_file() or not binary.is_file():
        raise ValueError(f"{base_path}: expected .hdr and .cfl files")
    dimensions = read_dimensions(header)

    if dimensions[:3] != SPATIAL_SHAPE or any(
        dimension != 1 for dimension in dimensions[3:]
    ):
        raise ValueError(
            f"{header}: expected 64 x 64 x 64 with trailing singleton axes"
        )

    expected_bytes = int(np.prod(dimensions)) * COMPLEX64.itemsize
    if binary.stat().st_size != expected_bytes:
        raise ValueError(f"{binary}: file size does not match the header")

    values = np.fromfile(binary, dtype=COMPLEX64)
    if not np.isfinite(values).all():
        raise ValueError(f"{binary}: non-finite values detected")

    return values.reshape(SPATIAL_SHAPE, order="F").astype(np.complex128)


def validate_pair(preparation_directory: Path, pair: str) -> None:
    if not preparation_directory.is_dir():
        raise ValueError(
            f"{preparation_directory}: preparation directory does not exist"
        )

    read_bart_3d(str(preparation_directory / pair))
    print(
        f"VALID: {pair} in {preparation_directory} "
        "(64 x 64 x 64, trailing singleton axes, complex64, finite values)"
    )


def main() -> int:
    args = parse_args()

    try:
        validate_pair(args.preparation_directory, args.pair)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
