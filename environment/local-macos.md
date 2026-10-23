# Local Computing Environment — macOS

Consolidated: 2026-10-23. Values come from Ricardo's terminal outputs unless marked
as hardware reports. They are not independently queried by the assistant and do
not claim these are the latest publicly available versions.

The current Mac replaces the Windows/WSL environment in the historical proposal.
No TALC environment has been verified by these local outputs.

| Component | Reported/observed value | Evidence |
| --- | --- | --- |
| Computer | MacBook Pro | Author; exact year/size not recorded |
| Chip | Apple M5 | Author |
| Installed memory | 24 GB | Author; not peak application use |
| macOS | 26.7.1, build 25G241 | `sw_vers` |
| Architecture | arm64 | `uname -m` |
| Developer directory | `/Library/Developer/CommandLineTools` | `xcode-select --print-path` |
| Homebrew path | `/opt/homebrew/bin/brew` | Command lookup |
| Homebrew | 7.0.10 | Version output |
| Git | 2.54.0 (Apple Git-157) | Version output |
| GNU Make | 4.4.1; aarch64-apple-darwin25.0.0 | Version output |
| GCC | 16.2.0 | Homebrew and BART output |
| FFTW | 3.3.11 | Homebrew inventory |
| OpenBLAS | 0.3.34 | Homebrew inventory |
| libpng | 1.6.59 | Homebrew inventory |
| flock | 0.4.0 | Homebrew inventory |
| BART | v1.0.00 | Version output |
| BART short commit | 37f3c5f | Terminal prompt; full hash pending |
| Practice Python | 3.13.17 | Virtual-environment output |
| NumPy | 2.5.4 | Import and comparison report |
| Matplotlib | 3.11.2 | Plotting report |

## BART flags

```text
BART_VERSION=v1.0.00
GCC_VERSION=16.2.0
CUDA=0
ACML=0
FFTWTHREADS=1
OMP=0
TENSORFLOW=0
MPI=0
```

OMP=0 does not establish single-thread execution: FFTW thread support is enabled.
Actual thread use, runtime and peak memory were not measured in this practice.

## Python

Initially `python3` resolved to Apple Command Line Tools Python 3.9.6 and could not
import NumPy. A separate Homebrew Python 3.13 environment was created at
`~/bart-learning/.venv`; the active interpreter ends in `.venv/bin/python`.
The Apple interpreter was not replaced. Do not move/commit the virtual environment.
Its compatibility with the laboratory extractor is not established.

The supplied direct dependency files are not full locks. The imported snapshots
are included as `python-requirements-verification.txt` and
`python-requirements-visualization.txt`, together with `bart-build.txt`.
The shared diff shows package-version entries in these snapshots, not private
direct URLs. Final review remains the author's responsibility. Fresh setup and
clean-checkout reproduction remain pending.
