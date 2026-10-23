# Fully Sampled Synthetic 2D Fourier Comparison

## Scope

Learn BART command/file conventions and compare an independent inverse against a
known image. The case is 64 × 64, single-channel, fully sampled, with all remaining
dimensions one. It involves no scanner data, coil calibration, CS or GE extraction.

## Observed procedure

Within a new run folder:

```bash
bart phantom -x 64 reference
bart fft -u 3 reference kspace
bart fft -i -u 3 kspace reconstruction
bart nrmse -S reference reconstruction > nrmse.txt
```

Bitmask 3 selects array axes 0 and 1, not a 3D acquisition. The transforms were
centered and unitary. The header reports
`64 64 1 1 1 1 1 1 1 1 1 1 1 1 1 1`. BART NRMSE was `1.442448e-07`.

The independent checker reads complex64 data in Fortran order and converts to
complex128 for computation/comparison. It checks dimensions, byte count, finite
values and the nonzero reference norm. It does not invoke BART. Its inverse is:

```python
np.fft.fftshift(
    np.fft.ifft2(np.fft.ifftshift(kspace, axes=(0, 1)),
                 axes=(0, 1), norm="ortho"),
    axes=(0, 1),
)
```

This convention is recorded for the even-sized 64 × 64 fixture, not all possible
shapes/acquisitions. No fitted scale or phase adjustment is used. In each reported
"A vs B" relative error, B supplies the norm in the denominator.

## Proposed repository reproduction

The two scripts are now included in `scripts/`. This route has **not yet been
checked from the assembled repository or a clean checkout**. Execute the commands
in reviewed steps and stop at the first error; never overwrite the original run.

From the repository root, activate the existing practice environment:

```bash
REPO="$PWD"
source "$HOME/bart-learning/.venv/bin/activate"
export BART_TOOLBOX_PATH="$HOME/software/bart-1.0.00"
export PATH="$BART_TOOLBOX_PATH:$PATH"
RUN_DIR="$HOME/bart-learning/reproduction-$(date -u +%Y%m%dT%H%M%SZ)"
mkdir "$RUN_DIR" && cd "$RUN_DIR"
```

Confirm the directory, then run and check each command:

```bash
date -u "+%Y-%m-%dT%H:%M:%SZ" > started-utc.txt
bart version -V > bart-build.txt
bart phantom -x 64 reference
bart fft -u 3 reference kspace
bart fft -i -u 3 kspace reconstruction
bart nrmse -S reference reconstruction > nrmse.txt
python "$REPO/scripts/check_fourier_numpy.py"
```

Use the **new folder name printed by the checker** in the plotting command, not the
historical folder label. The command template is:

```text
python /absolute/path/to/repository/scripts/visualize_synthetic.py NEW_CHECK_DIRECTORY
```

Retain original reports and statuses. Missing outputs, exceptions and non-finite
values are not success. The current script measures errors without a numerical
acceptance threshold. A fresh installation also needs the recorded dependencies.

## Interpretation and limits

Observed errors were about 1e-7, without a formal pass/fail tolerance. Precision
differs between calculations; the smaller NumPy error is not a general ranking.
Magnitude figures alone do not establish equality of complex arrays.

This is an independent inverse on BART-generated k-space, not an independent
analytical generator or verification of experimental orientation. Generalization
requires further reviewed fixtures and failure cases; they were not executed here.

The original run predates this project's first commit. Do not claim it ran from
that commit retroactively. Imports are now present; review, commit and rerun from
a recorded revision to establish repository-linked reproduction evidence.

See [observed evidence](../../results/familiarization-2d-20261023/README.md).
