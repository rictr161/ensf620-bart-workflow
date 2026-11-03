# Manual Cartesian 2D Tutorial

This tutorial walks through a fully sampled, single-channel Cartesian 2D
reconstruction using a 64 × 64 synthetic phantom. It covers synthetic input
preparation, BART reconstruction, output checks, visual comparison, and a
preliminary quantitative comparison.

This guide uses a BART-generated **64 × 64, fully sampled, single-channel**
synthetic case, with all remaining dimensions singleton. The three central
operations are phantom generation, a forward Fourier transform, and an inverse
Fourier transform.

| File pair | Role |
|---|---|
| `reference.hdr` / `reference.cfl` | Known synthetic image, preserved for comparison. |
| `kspace.hdr` / `kspace.cfl` | Prepared input to reconstruction. |
| `reconstruction.hdr` / `reconstruction.cfl` | New reconstructed image, stored separately. |

**Choose your starting point:**

- **Already have a checked preparation:** configure Section 1, then continue at
  Section 5. The previously reported `generation-01` or `generation-02` can be
  selected. No new phantom or second generation is needed for that reconstruction.
- **Need to prepare a new case:** complete Sections 1–3, then continue at Section 5.
  Section 4 describes the separate regeneration check used to establish the
  synthetic case; it is not required for every reconstruction.

Use a text editor to keep the short record in Section 9 as you work. Preserve
existing preparations and use a new output directory for each reconstruction.

## 1. Environment and Working Directory

Requirements: an installed BART executable, Python with NumPy, and this
repository's `scripts/check_preparation_pair.py` and
`scripts/check_fourier_numpy.py`. The checker is specific to this 64 × 64 case.
See [the documented macOS setup](../../environment/local-macos.md) for the
recorded installation.

Open a terminal and start one Bash session:

```bash
bash
```

Run the remaining blocks in that same session. Copy the contents of code blocks,
without the Markdown fence markers. The paths below are **examples matching the
recorded local layout**, not required repository locations. Adjust them before
continuing and use absolute paths. `$HOME` expands to your home directory.

```bash
cd "$HOME/projects/ensf620-bart-workflow" || exit "$?"
REPO="$(pwd -P)"
BART="$HOME/software/bart-1.0.00/bart"
PYTHON="$HOME/bart-learning/.venv/bin/python"
PREPARATION_DIR="$HOME/bart-learning/bart-workflow-preparations/generation-01"
RECONSTRUCTION_OUTPUT_DIR="$HOME/bart-learning/bart-workflow-reconstructions/manual-2d-01"
```

For an existing preparation, select its actual directory. For a new preparation,
change `PREPARATION_DIR` to a new name, such as `generation-new-01`, before
Section 2. Select a new reconstruction directory outside the preparation
directory. Directory creation below rejects names that already exist.

Check the required executables and repository files:

```bash
if [ ! -x "$BART" ] || [ ! -x "$PYTHON" ] ||
   [ ! -f "$REPO/scripts/check_preparation_pair.py" ] ||
   [ ! -f "$REPO/scripts/check_fourier_numpy.py" ]; then
    printf 'ERROR: check the configured executables and repository files.\n' >&2
    exit 1
fi
"$PYTHON" -c 'import numpy' || exit "$?"
"$BART" version -V || exit "$?"
"$PYTHON" --version || exit "$?"
uname -srm || exit "$?"
```

Copy the displayed version and platform information into your record. Each
data-processing block below prints its exit code and stops this Bash session on
failure. Preserve any partial outputs and logs if that happens.

## 2. Create and Preserve the Reference Phantom

**Skip this section when using an existing checked preparation.**

Create the new preparation directory. Its parent may already exist; the
preparation directory itself must be new.

```bash
mkdir -p "$(dirname "$PREPARATION_DIR")" || exit "$?"
mkdir "$PREPARATION_DIR" || exit "$?"
```

Generate the reference. `phantom` creates the synthetic image, `-x 64` sets the
image size, and the final argument is the output base path, without an extension.

```bash
if "$BART" phantom -x 64 "$PREPARATION_DIR/reference" \
    > "$PREPARATION_DIR/phantom.log" 2>&1; then
    printf 'SUCCESS: reference generation (exit code 0).\n'
else
    status=$?
    cat "$PREPARATION_DIR/phantom.log" >&2
    printf 'ERROR: reference generation (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

Expected output: `reference.hdr` and `reference.cfl` in `PREPARATION_DIR`.
Check that pair before generating k-space:

```bash
if "$PYTHON" "$REPO/scripts/check_preparation_pair.py" \
    "$PREPARATION_DIR" reference > "$PREPARATION_DIR/reference-check.txt" 2>&1; then
    cat "$PREPARATION_DIR/reference-check.txt"
    printf 'SUCCESS: reference check (exit code 0).\n'
else
    status=$?
    cat "$PREPARATION_DIR/reference-check.txt" >&2
    printf 'ERROR: reference check (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

The checker verifies the declared dimensions, singleton trailing axes, expected
complex64 file size, and finite values. Record the two command outcomes using
Section 9 and preserve the reference pair unchanged.

## 3. Generate and Validate the k-Space

**Skip this section when using an existing checked preparation.**

Transform the checked reference into k-space:

```bash
if "$BART" fft -u 3 "$PREPARATION_DIR/reference" "$PREPARATION_DIR/kspace" \
    > "$PREPARATION_DIR/forward-fft.log" 2>&1; then
    printf 'SUCCESS: k-space generation (exit code 0).\n'
else
    status=$?
    cat "$PREPARATION_DIR/forward-fft.log" >&2
    printf 'ERROR: k-space generation (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

`fft` performs the Fourier transform. `-u` selects unitary normalization and the
bitmask `3` selects axes 0 and 1. BART's default centered transform is retained.
The inputs and outputs are base paths identifying `.hdr` / `.cfl` pairs.

Expected output: `kspace.hdr` and `kspace.cfl`. Check the new pair:

```bash
if "$PYTHON" "$REPO/scripts/check_preparation_pair.py" \
    "$PREPARATION_DIR" kspace > "$PREPARATION_DIR/kspace-check.txt" 2>&1; then
    cat "$PREPARATION_DIR/kspace-check.txt"
    printf 'SUCCESS: k-space check (exit code 0).\n'
else
    status=$?
    cat "$PREPARATION_DIR/kspace-check.txt" >&2
    printf 'ERROR: k-space check (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

Record both outcomes. These pair checks establish basic readability and
structure; they do not evaluate reconstruction accuracy. Continue at Section 5
unless you are specifically performing the regeneration check in Section 4.

## 4. Regenerate and Compare the Synthetic Generations

This check asks whether repeating the preparation produces the same reference
and k-space files in the selected environment. It is separate from reconstruction.
The two previously reported generations already have the evidence summarized at
the end of this document.

When performing a new regeneration check:

1. Keep the first preparation path and select a new, unused second directory:

   ```bash
   FIRST_PREPARATION_DIR="$PREPARATION_DIR"
   PREPARATION_DIR="<ABSOLUTE_NEW_SECOND_PREPARATION_DIRECTORY>"
   ```

2. Replace the marker, then repeat **Sections 2 and 3 exactly**, using the same
   Bash session, BART executable, Python executable, and parameters. Do not repeat
   Section 1, which would reset the selected paths. Each section writes its logs
   into the currently selected `PREPARATION_DIR`.
3. After both preparations pass their checks, compare the four file pairs:

   ```bash
   {
       printf 'First preparation: %s\nSecond preparation: %s\n' \
           "$FIRST_PREPARATION_DIR" "$PREPARATION_DIR"
       for pair_file in reference.hdr reference.cfl kspace.hdr kspace.cfl; do
           if cmp "$FIRST_PREPARATION_DIR/$pair_file" "$PREPARATION_DIR/$pair_file"; then
               printf 'MATCH: %s (exit code 0)\n' "$pair_file"
           else
               status=$?
               if [ "$status" -eq 1 ]; then
                   printf 'DIFFERENT: %s (exit code 1)\n' "$pair_file"
               else
                   printf 'ERROR: %s (exit code %s)\n' "$pair_file" "$status"
               fi
           fi
       done
   } > "$PREPARATION_DIR/regeneration-comparison.txt" 2>&1 || exit "$?"
   cat "$PREPARATION_DIR/regeneration-comparison.txt"
   ```

   Interpret each file independently: `MATCH` means byte-identical content;
   `DIFFERENT` means different content; `ERROR` means an operational comparison
   error. Preserve the comparison record in the second preparation directory.

4. Select the first preparation again before continuing to reconstruction:

   ```bash
   PREPARATION_DIR="$FIRST_PREPARATION_DIR"
   ```

Record the observed outcomes, including differences or errors. Exact matches
describe those two preparations only, not reconstruction quality or general
reproducibility.

## 5. Reconstruct the Case with BART

Use the preparation selected in Section 1, or the one just completed. Continue
in the same Bash session; the commands use full paths and require no new `cd`.

Confirm the input and preserved reference, then create the new output directory:

```bash
for pair_file in reference.hdr reference.cfl kspace.hdr kspace.cfl; do
    if [ ! -f "$PREPARATION_DIR/$pair_file" ]; then
        printf 'ERROR: missing prepared file: %s\n' "$PREPARATION_DIR/$pair_file" >&2
        exit 1
    fi
done
mkdir -p "$(dirname "$RECONSTRUCTION_OUTPUT_DIR")" || exit "$?"
mkdir "$RECONSTRUCTION_OUTPUT_DIR" || exit "$?"
```

Reconstruct by applying the inverse Fourier transform to the prepared k-space:

```bash
if "$BART" fft -i -u 3 \
    "$PREPARATION_DIR/kspace" "$RECONSTRUCTION_OUTPUT_DIR/reconstruction" \
    > "$RECONSTRUCTION_OUTPUT_DIR/reconstruction.log" 2>&1; then
    printf 'SUCCESS: BART reconstruction (exit code 0).\n'
else
    status=$?
    cat "$RECONSTRUCTION_OUTPUT_DIR/reconstruction.log" >&2
    printf 'ERROR: BART reconstruction (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

`-i` selects the inverse transform. The unchanged `-u 3` uses unitary
normalization over axes 0 and 1, matching preparation. The bitmask `3` does not
mean a 3D acquisition.

Expected output: `reconstruction.hdr` and `reconstruction.cfl` in
`RECONSTRUCTION_OUTPUT_DIR`. The prepared reference and k-space remain unchanged.
Record the command and exit code. A successful command still needs the output
check below.

## 6. Check the Reconstruction Outputs

Read the new pair using the existing `read_bart_2d` reader. This inline block
imports the reader without calling the module's `main()` function. It checks
only `reconstruction`; it performs no additional inverse transform or metric.

```bash
if "$PYTHON" - "$REPO" "$RECONSTRUCTION_OUTPUT_DIR/reconstruction" \
    > "$RECONSTRUCTION_OUTPUT_DIR/reconstruction-check.txt" 2>&1 <<'PY'
import sys
from pathlib import Path

sys.path.insert(0, str(Path(sys.argv[1]) / "scripts"))
from check_fourier_numpy import read_bart_2d

read_bart_2d(sys.argv[2])
print("VALID: reconstruction (64 x 64, singleton trailing axes, correct size, finite values)")
PY
then
    cat "$RECONSTRUCTION_OUTPUT_DIR/reconstruction-check.txt"
    printf 'SUCCESS: reconstruction-output check (exit code 0).\n'
else
    status=$?
    cat "$RECONSTRUCTION_OUTPUT_DIR/reconstruction-check.txt" >&2
    printf 'ERROR: reconstruction-output check (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

Record the result. A passing check establishes readability, expected dimensions
and file size, and finite values for this fixture. It does not by itself
establish agreement with the reference; the visual and quantitative results are
recorded separately below.

## 7. Perform the Visual Comparison

Run the following block in the same Bash session and with the same `PYTHON`
selected in Section 1. It reads only the preserved reference and the
reconstruction output:

```bash
FIGURE_DIR="$RECONSTRUCTION_OUTPUT_DIR/figures-visual"
VISUAL_LOG="$RECONSTRUCTION_OUTPUT_DIR/visual-comparison.log"

if [ -e "$FIGURE_DIR" ]; then
    printf 'ERROR: figure directory already exists; stop without overwriting it: %s\n' \
        "$FIGURE_DIR" >&2
    exit 1
fi

if mkdir "$FIGURE_DIR"; then
    :
else
    status=$?
    printf 'ERROR: could not create the figure directory (exit code %s): %s\n' \
        "$status" "$FIGURE_DIR" >&2
    exit "$status"
fi

if "$PYTHON" - "$REPO" "$PREPARATION_DIR/reference" \
    "$RECONSTRUCTION_OUTPUT_DIR/reconstruction" "$FIGURE_DIR" \
    > "$VISUAL_LOG" 2>&1 <<'PY'
import platform
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

repo = Path(sys.argv[1])
reference_base = sys.argv[2]
reconstruction_base = sys.argv[3]
figure_dir = Path(sys.argv[4])
sys.path.insert(0, str(repo / "scripts"))

from check_fourier_numpy import read_bart_2d

reference = read_bart_2d(reference_base)
reconstruction = read_bart_2d(reconstruction_base)
reference_magnitude = np.abs(reference)
reconstruction_magnitude = np.abs(reconstruction)
reference_max = float(reference_magnitude.max())

if not np.isfinite(reference_max) or reference_max <= 0:
    raise ValueError("reference maximum magnitude must be finite and positive")

reconstruction_max = float(reconstruction_magnitude.max())
if not np.isfinite(reconstruction_max):
    raise ValueError("reconstruction maximum magnitude must be finite")

figure_path = figure_dir / "reference-reconstruction.png"
if figure_path.exists():
    raise FileExistsError(f"refusing to overwrite existing figure: {figure_path}")

figure, axes = plt.subplots(1, 2, figsize=(10, 4.5), constrained_layout=True)
for axis, values, title in (
    (axes[0], reference_magnitude, "Reference magnitude"),
    (axes[1], reconstruction_magnitude, "BART reconstruction magnitude"),
):
    image = axis.imshow(
        values.T,
        cmap="gray",
        origin="lower",
        aspect="equal",
        interpolation="none",
        vmin=0,
        vmax=reference_max,
    )
    axis.set_title(title)
    axis.set_xlabel("Array axis 0 index")
    axis.set_ylabel("Array axis 1 index")
figure.colorbar(image, ax=axes, label="Magnitude")
figure.savefig(figure_path, dpi=160)
plt.close(figure)

print(f"Reference input: {reference_base}.hdr/.cfl")
print(f"Reconstruction input: {reconstruction_base}.hdr/.cfl")
print(f"Python: {platform.python_version()}")
print(f"NumPy: {np.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
print("Display: abs(array).T, origin=lower, aspect=equal, interpolation=none")
print("Colormap: gray")
print(f"Shared magnitude limits: 0 to {reference_max:.9e}")
if reconstruction_max > reference_max:
    print(
        "WARNING: reconstruction magnitude exceeds the displayed reference "
        "maximum; those values are clipped in the figure."
    )
else:
    print("Reconstruction magnitude does not exceed the displayed range.")
print(f"Figure: {figure_path}")
print("Visual comparison figure generation completed.")
PY
then
    status=0
else
    status=$?
fi

printf 'Visual figure-generation exit code: %s\n' "$status" >> "$VISUAL_LOG"
cat "$VISUAL_LOG"
if [ "$status" -ne 0 ]; then
    printf 'ERROR: visual figure generation failed; preserve the log: %s\n' \
        "$VISUAL_LOG" >&2
    exit "$status"
fi
```

Expect one file at:

```text
$FIGURE_DIR/reference-reconstruction.png
```

The block records the selected input bases, Python/NumPy/Matplotlib versions,
display options, shared limits, warning status, figure path, and command result
in `$VISUAL_LOG`. Inspect the saved figure and record whether the principal
pattern appears in the same locations, along with visible intensity, contrast,
ringing, structure, or clipping. The transposition is visual only; it does not
modify either input or define a transformation for the quantitative comparison.
This block reads the images and generates a figure only. It does not calculate
metrics, perform an additional transform, or call the main comparison program.

## 8. Perform the Preliminary Quantitative Comparison

Calculate the complex relative L2 error between the preserved reference and the
corresponding BART reconstruction using the original complex arrays:

```text
||reconstruction - reference||₂ / ||reference||₂
```

Use the original complex values returned by `read_bart_2d`, flattened only
inside `relative_error`. Do not convert to magnitude, transpose, crop, mask,
align, rescale, or correct phase. The division by the reference norm belongs
to the metric and is not separate image normalization. Do not select a
tolerance or pass/fail criterion.

Run this block in the same Bash session and with the same `PYTHON` selected in
Section 1. Complete the reconstruction-output check in Section 6 first:

```bash
QUANTITATIVE_LOG="$RECONSTRUCTION_OUTPUT_DIR/quantitative-comparison.txt"

if [ -e "$QUANTITATIVE_LOG" ]; then
    printf 'ERROR: quantitative comparison record already exists; stop without overwriting it: %s\n' \
        "$QUANTITATIVE_LOG" >&2
    exit 1
fi

if "$PYTHON" - "$REPO" "$PREPARATION_DIR/reference" \
    "$RECONSTRUCTION_OUTPUT_DIR/reconstruction" \
    > "$QUANTITATIVE_LOG" 2>&1 <<'PY'
import platform
import sys
from pathlib import Path

import numpy as np

repo = Path(sys.argv[1])
reference_base = sys.argv[2]
reconstruction_base = sys.argv[3]
sys.path.insert(0, str(repo / "scripts"))

from check_fourier_numpy import read_bart_2d, relative_error

reference = read_bart_2d(reference_base)
reconstruction = read_bart_2d(reconstruction_base)
error = relative_error(reference, reconstruction)
reference_max = float(np.abs(reference).max())
reconstruction_max = float(np.abs(reconstruction).max())

print(f"Reference input: {reference_base}.hdr/.cfl")
print(f"Reconstruction input: {reconstruction_base}.hdr/.cfl")
print(f"Python: {platform.python_version()}")
print(f"NumPy: {np.__version__}")
print("Metric: ||reconstruction - reference||_2 / ||reference||_2")
print("Values: original complex arrays from read_bart_2d, flattened by relative_error")
print("Preprocessing: none; no magnitude conversion, transpose, crop, mask, alignment, scaling, or phase correction")
print(f"Reference maximum magnitude (visual-range diagnostic): {reference_max:.9e}")
print(f"Reconstruction maximum magnitude (visual-range diagnostic): {reconstruction_max:.9e}")
print(f"Complex relative L2 error: {error:.9e}")
print("No tolerance or pass/fail criterion applied.")
PY
then
    status=0
else
    status=$?
fi

printf 'Quantitative comparison exit code: %s\n' "$status" >> "$QUANTITATIVE_LOG"
cat "$QUANTITATIVE_LOG"
if [ "$status" -ne 0 ]; then
    printf 'ERROR: quantitative comparison failed; preserve the log: %s\n' \
        "$QUANTITATIVE_LOG" >&2
    exit "$status"
fi
```

Expect the record at:

```text
$RECONSTRUCTION_OUTPUT_DIR/quantitative-comparison.txt
```

The file records the selected inputs, Python and NumPy versions, metric
definition, effective no-preprocessing conditions, diagnostic maxima, numeric
error, and Python's exit code. A code `0` indicates that the calculation
completed operationally; the resulting value is a case-specific observed
difference, not general validation or a pass/fail decision. This block does
not generate a reconstruction or figure and does not invoke `main()` or the
complete Fourier-comparison program.

## 9. Record Commands, Configuration, Results, and Limitations

Use the following short record format, confirmed for this tutorial. Keep notes
in a text editor from the start and add each command's
actual outcome immediately after running it. Copy the terminal's reported exit
code and keep the diagnostic files produced above.

- For a new preparation, save its record as `preparation-record.txt` in that
  preparation directory. Both generations need their own records if regenerating.
- For reconstruction, preserve the records produced in
  `RECONSTRUCTION_OUTPUT_DIR`: `reconstruction.log`,
  `reconstruction-check.txt`, `visual-comparison.log`,
  `figures-visual/reference-reconstruction.png`, and
  `quantitative-comparison.txt`.
- Keep the selected preparation's existing records and paths as references; do
  not change them. A cumulative `run-record.md` is optional and is not required
  to complete this execution. If one exists, locate it in the reconstruction
  output directory and preserve it without treating it as a substitute for the
  stage-specific records.

```markdown
# Manual Cartesian 2D Run Record

- Date/time and time zone: <observed value>
- Operator: <name>
- Repository location and revision/local changes, if known: <details>
- BART executable and version/build: <actual values>
- Python executable/version, NumPy version if recorded, and platform: <actual values>
- Selected preparation: <absolute path; link to its record>
- Reconstruction output, if performed: <absolute path>
- Effective settings: <actual phantom command, dimensions, channels, sampling, FFT options>

| Step actually performed | Exact command/invocation | Exit code | Observation | Log/evidence link |
|---|---|---:|---|---|
| <step> | <command> | <observed code> | <observed result> | [Evidence](<relative-path>) |

- Produced files: <actual files>
- Regeneration comparison, if performed: <record path and each file's result/code>
- Visual comparison: <approved method not executed / observed figures and findings>
- Quantitative comparison: <approved method not executed / actual method and result>
- Failures, corrections, and unresolved issues: <observations or none reported>
- Limitations: <what this execution did and did not demonstrate>
```

Add one table row per executed operation. Mark stages not performed as
`NOT_EXECUTED`; do not label them failed or fill them with historical successes.
An exit code of `0` describes command success, not a reconstruction-quality
criterion. Keep human visual observations separate from figure-generation
command outcomes. Record the approved visual and quantitative methods separately
from their execution results.
