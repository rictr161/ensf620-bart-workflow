from datetime import datetime, timezone
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")  # Save files without opening an interactive session.
import matplotlib.pyplot as plt
import numpy as np

from check_fourier_numpy import read_bart_2d


def main() -> None:
    if len(sys.argv) != 2:
        raise ValueError(
            "Usage: python visualize_synthetic.py <numpy-check-directory>"
        )

    check_dir = Path(sys.argv[1])
    reference = read_bart_2d("reference")
    kspace = read_bart_2d("kspace")
    bart_image = read_bart_2d("reconstruction")
    numpy_image = np.load(
        check_dir / "reconstruction_numpy.npy",
        allow_pickle=False,
    )

    if numpy_image.shape != reference.shape or not np.isfinite(numpy_image).all():
        raise ValueError(
            "NumPy image has incompatible dimensions or non-finite values"
        )

    image_max = float(np.abs(reference).max())
    if not np.isfinite(image_max) or image_max <= 0:
        raise ValueError(
            "Reference must have a finite, positive maximum magnitude"
        )

    log_kspace = np.log1p(np.abs(kspace))
    residual = np.abs(numpy_image - reference)

    views = [
        (
            "01_reference.png", "Reference magnitude",
            np.abs(reference), image_max, "Magnitude",
        ),
        (
            "02_kspace.png", "Centered k-space: log magnitude",
            log_kspace, None, "ln(1 + |K|)",
        ),
        (
            "03_bart.png", "BART reconstruction magnitude",
            np.abs(bart_image), image_max, "Magnitude",
        ),
        (
            "04_numpy.png", "NumPy reconstruction magnitude",
            np.abs(numpy_image), image_max, "Magnitude",
        ),
        (
            "05_residual.png", "Complex residual: |NumPy - reference|",
            residual, None, "Absolute complex difference",
        ),
    ]

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    output = check_dir / f"figures-{stamp}"
    output.mkdir(exist_ok=False)

    for filename, title, values, upper, label in views:
        fig = plt.figure(figsize=(6.5, 5.5))

        # Transpose for display only: array axis 0 runs horizontally.
        image = plt.imshow(
            values.T,
            origin="lower",
            interpolation="nearest",
            vmin=0,
            vmax=upper,
            aspect="equal",
        )
        plt.colorbar(image, label=label)
        plt.title(title)
        plt.xlabel("Array axis 0 index")
        plt.ylabel("Array axis 1 index")
        plt.tight_layout()

        fig.savefig(output / filename, dpi=160)
        plt.close(fig)

    (output / "plot-info.txt").write_text(
        f"NumPy: {np.__version__}\n"
        f"Matplotlib: {matplotlib.__version__}\n"
        f"NumPy input: {check_dir / 'reconstruction_numpy.npy'}\n"
        f"Shared image display range: 0 to {image_max:.9e}\n"
        "K-space display: ln(1 + |K|); separate display range.\n"
        "Residual display: |NumPy - reference|; separate display range.\n"
        "Array axis 0 displayed horizontally; no anatomical orientation assigned.\n"
        "No reconstruction performed; original arrays were not modified.\n",
        encoding="utf-8",
    )

    print(f"Saved 5 PNG figures in: {output}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
