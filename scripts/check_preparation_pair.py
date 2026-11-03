"""Validate one prepared BART 64 x 64 data pair."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from check_fourier_numpy import read_bart_2d


VALID_PAIRS = ("reference", "kspace")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate one prepared BART 64 x 64 data pair."
    )
    parser.add_argument(
        "generation_directory",
        type=Path,
        help="Directory containing the selected .hdr and .cfl pair.",
    )
    parser.add_argument(
        "pair",
        choices=VALID_PAIRS,
        help="Pair to validate: reference or kspace.",
    )
    return parser.parse_args()


def validate_pair(generation_directory: Path, pair: str) -> None:
    if not generation_directory.is_dir():
        raise ValueError(
            f"{generation_directory}: generation directory does not exist"
        )

    base_path = generation_directory / pair
    read_bart_2d(str(base_path))

    print(
        f"VALID: {pair} in {generation_directory} "
        "(64 x 64, complex64, finite values)"
    )


def main() -> int:
    args = parse_args()

    try:
        validate_pair(args.generation_directory, args.pair)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
