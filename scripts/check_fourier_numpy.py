from datetime import datetime, timezone
from pathlib import Path
import platform
import sys

import numpy as np

SHAPE = (64, 64)
AXES = (0, 1)


def read_bart_2d(name: str) -> np.ndarray:
    """Read only the 64 x 64, single-channel fixture used in this exercise."""
    header = Path(f"{name}.hdr")
    binary = Path(f"{name}.cfl")
    lines = [line.strip() for line in header.read_text().splitlines()]
    try:
        dims = [int(x) for x in lines[lines.index("# Dimensions") + 1].split()]
    except (ValueError, IndexError) as exc:
        raise ValueError(f"{header}: invalid dimensions header") from exc

    if tuple(dims[:2]) != SHAPE or any(d != 1 for d in dims[2:]):
        raise ValueError(f"{header}: expected 64 x 64 with trailing singleton axes")

    dtype = np.dtype("<c8")  # Little-endian complex64 on disk.
    count = SHAPE[0] * SHAPE[1]
    if binary.stat().st_size != count * dtype.itemsize:
        raise ValueError(f"{binary}: file size does not match the header")

    values = np.fromfile(binary, dtype=dtype)
    # BART stores the first index fastest: use Fortran array ordering.
    image = values.reshape(SHAPE, order="F").astype(np.complex128)
    if not np.isfinite(image).all():
        raise ValueError(f"{binary}: non-finite values detected")
    return image


def relative_error(reference: np.ndarray, result: np.ndarray) -> float:
    """Compare complex arrays without fitted scaling or phase correction."""
    denominator = float(np.linalg.norm(reference.ravel()))
    if not np.isfinite(denominator) or denominator == 0:
        raise ValueError("The comparison reference must have a finite, nonzero norm")
    value = float(np.linalg.norm((result - reference).ravel()) / denominator)
    if not np.isfinite(value):
        raise ValueError("The relative error is not finite")
    return value


def main() -> None:
    reference = read_bart_2d("reference")
    kspace = read_bart_2d("kspace")
    bart_reconstruction = read_bart_2d("reconstruction")

    # Match the centered, unitary inverse for this even-sized 2D fixture.
    numpy_reconstruction = np.fft.fftshift(
        np.fft.ifft2(
            np.fft.ifftshift(kspace, axes=AXES),
            axes=AXES,
            norm="ortho",
        ),
        axes=AXES,
    )
    if not np.isfinite(numpy_reconstruction).all():
        raise ValueError("NumPy reconstruction contains non-finite values")

    errors = {
        "BART vs reference": relative_error(reference, bart_reconstruction),
        "NumPy vs reference": relative_error(reference, numpy_reconstruction),
        "BART vs NumPy": relative_error(numpy_reconstruction, bart_reconstruction),
    }
    now = datetime.now(timezone.utc)
    output = Path("numpy-check-" + now.strftime("%Y%m%dT%H%M%S%fZ"))
    output.mkdir(exist_ok=False)
    np.save(output / "reconstruction_numpy.npy", numpy_reconstruction, allow_pickle=False)

    report = [
        "Independent Fourier comparison - exploratory 64 x 64 case",
        f"UTC time: {now.isoformat()}",
        f"Python: {platform.python_version()}",
        f"NumPy: {np.__version__}",
        f"Shape: {SHAPE}; axes: {AXES}; normalization: ortho; centered: yes",
        "Disk data: complex64; NumPy computation and comparison: complex128",
        "Relative L2 errors (denominator is the second named array):",
    ]
    report.extend(f"{name}: {value:.9e}" for name, value in errors.items())
    report.append("Measurements only: no numerical acceptance threshold applied.")
    text = "\n".join(report) + "\n"
    (output / "comparison.txt").write_text(text, encoding="utf-8")
    print(text, end="")
    print(f"Saved outputs in: {output}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
