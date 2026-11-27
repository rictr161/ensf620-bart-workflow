"""Interactively inspect an existing scalar BART reconstruction."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Sequence

import numpy as np

if __package__:
    from .bart_workflow import read_bart_array
else:
    from bart_workflow import read_bart_array


def view_bart_slices(
    input_base: Path,
    axis: int = 2,
    voxel_spacing: Sequence[float] | None = None,
) -> None:
    """Open one scalar 2D or 3D BART reconstruction for slice inspection."""
    if axis not in (0, 1, 2):
        raise ValueError("axis must be 0, 1, or 2")
    if voxel_spacing is not None:
        if len(voxel_spacing) != 3 or any(
            not np.isfinite(value) or value <= 0 for value in voxel_spacing
        ):
            raise ValueError("voxel spacing must contain three finite positive values")

    values = read_bart_array(input_base)
    if values.ndim < 2 or any(size != 1 for size in values.shape[3:]):
        raise ValueError(
            "expected a scalar 2D or 3D reconstruction with singleton "
            "channel, map-set, and later axes"
        )
    shape = tuple(
        values.shape[index] if index < values.ndim else 1 for index in range(3)
    )
    magnitude = np.abs(values.reshape(shape))
    maximum = float(magnitude.max())
    display_maximum = maximum if maximum > 0 else 1.0

    import matplotlib
    from matplotlib.backends import backend_registry

    backend, framework = backend_registry.resolve_backend(matplotlib.get_backend())
    if framework not in {"macosx", "qt", "qt5", "tk", "wx", "gtk3", "gtk4"}:
        raise RuntimeError(
            f"Matplotlib backend {backend!r} does not provide a supported "
            "interactive desktop window; configure an available GUI backend"
        )

    import matplotlib.pyplot as plt
    from matplotlib.widgets import Slider

    plane_axes = tuple(index for index in range(3) if index != axis)
    initial_index = shape[axis] // 2
    extent = None
    if voxel_spacing is not None:
        horizontal_spacing = voxel_spacing[plane_axes[0]]
        vertical_spacing = voxel_spacing[plane_axes[1]]
        extent = (
            -0.5 * horizontal_spacing,
            (shape[plane_axes[0]] - 0.5) * horizontal_spacing,
            -0.5 * vertical_spacing,
            (shape[plane_axes[1]] - 0.5) * vertical_spacing,
        )

    figure, axes = plt.subplots()
    if shape[axis] > 1:
        figure.subplots_adjust(bottom=0.22)
    image = axes.imshow(
        np.take(magnitude, initial_index, axis=axis).T,
        cmap="gray",
        origin="lower",
        aspect="equal",
        interpolation="none",
        vmin=0,
        vmax=display_maximum,
        extent=extent,
    )
    unit = "mm" if voxel_spacing is not None else "index"
    axes.set_xlabel(f"Array axis {plane_axes[0]} {unit}")
    axes.set_ylabel(f"Array axis {plane_axes[1]} {unit}")
    figure.colorbar(image, ax=axes, label="Magnitude")

    def update(index: float) -> None:
        selected = int(round(index))
        image.set_data(np.take(magnitude, selected, axis=axis).T)
        axes.set_title(f"Array axis {axis} = {selected}")
        figure.canvas.draw_idle()

    update(initial_index)
    if shape[axis] > 1:
        slider_axis = figure.add_axes((0.15, 0.08, 0.7, 0.04))
        slider = Slider(
            slider_axis,
            f"Axis {axis} index",
            valmin=0,
            valmax=shape[axis] - 1,
            valinit=initial_index,
            valstep=1,
        )
        slider.on_changed(update)
    plt.show(block=True)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Interactively inspect an existing scalar BART reconstruction."
    )
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="BART pair base path, without .hdr or .cfl",
    )
    parser.add_argument("--axis", type=int, choices=(0, 1, 2), default=2)
    parser.add_argument(
        "--voxel-spacing",
        type=float,
        nargs=3,
        metavar=("SX", "SY", "SZ"),
        help="positive voxel spacing in mm for array axes 0, 1, and 2",
    )
    args = parser.parse_args(argv)
    try:
        view_bart_slices(args.input, args.axis, args.voxel_spacing)
    except (ImportError, OSError, RuntimeError, ValueError) as exc:
        print(f"ERROR: interactive slice viewer: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
