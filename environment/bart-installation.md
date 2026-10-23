# BART Installation Record — macOS

This records the guided recipe and returned evidence. It is not a verbatim full
installation log. Do not automatically reinstall over the working environment.
The selected release was v1.0.00; this record does not assert it remains latest.

Location: `~/software/bart-1.0.00`, an upstream release checkout separate from this
project. Its observed state was `HEAD (no branch)` and an untracked `build.log`.
There is no need to switch the BART checkout to `main` to use it.

## Guided preparation

```bash
brew update
brew install gcc make fftw openblas libpng flock
git clone --branch v1.0.00 --depth 1 https://codeberg.org/mrirecon/bart.git bart-1.0.00
```

The clone was performed within `~/software`. Versions are in `local-macos.md`.
The instructed `Makefile.local` recipe used GCC/G++ 16, `MACPORTS=0`, `OPENBLAS=1`,
`CUDA=0`, `OMP=0`, Homebrew FFTW/OpenBLAS prefixes, and libpng include/library paths.
The actual local file should be preserved before claiming byte-for-byte build
provenance; selected flags were confirmed by `bart version -V`.

Build command:

```bash
gmake -j4 > build.log 2>&1
```

Ricardo returned successful `./bart version` and `./bart version -V` output and
subsequent synthetic results. The complete build log/exit status is not reproduced
here. This was a familiarization configuration, not a performance-tuned evaluation
build or a completed BART test-suite run.

## Session activation

```bash
export BART_TOOLBOX_PATH="$HOME/software/bart-1.0.00"
export PATH="$BART_TOOLBOX_PATH:$PATH"
command -v bart
bart version
```

These session exports do not modify shell startup files. Permanent shell configuration
has not been established by the returned evidence.

## Python setup used

```bash
brew install python@3.13
/opt/homebrew/bin/python3.13 -m venv "$HOME/bart-learning/.venv"
source "$HOME/bart-learning/.venv/bin/activate"
python -m pip --require-virtualenv install numpy
```

Observed NumPy: 2.5.4. Visualization later used:

```bash
python -m pip --require-virtualenv install matplotlib "numpy==2.5.4"
```

Observed Matplotlib: 3.11.2. Unpinned historical installation commands do not
promise to recreate identical future versions; preserve dependency snapshots.
