# Manual Cartesian 3D Tutorial

This tutorial documents the preparation, regeneration verification, BART
reconstruction, and structural output checks for a fully sampled, single-channel
Cartesian 3D case using a 64 × 64 × 64 synthetic Shepp–Logan phantom.
It also documents visual and quantitative reference comparisons and the complete
execution record.

This guide uses a BART-generated **64 × 64 × 64, fully sampled, single-channel**
synthetic case. It does not simulate coil sensitivities, crop, or resample the
volume. The three central operations are phantom generation, a forward Fourier
transform over axes 0, 1, and 2, and an inverse Fourier transform.

| File pair | Role |
|---|---|
| `reference.hdr` / `reference.cfl` | Known synthetic volume, preserved for comparison. |
| `kspace.hdr` / `kspace.cfl` | Prepared input to reconstruction. |
| `reconstruction.hdr` / `reconstruction.cfl` | Future reconstructed volume, stored separately. |

**Choose your starting point:**

- **Establishing this 3D case for the first time:** complete Sections 1–4
  before continuing with reconstruction in Section 5.
- **Reusing an already verified preparation:** configure its actual paths in
  Section 1, then continue at Section 5. Use this route after the initial
  preparation and regeneration verification for the case have been completed.
  No new phantom or second generation is needed for each subsequent
  reconstruction.

Use a new preparation directory when preparing a new case and a new output
directory for each reconstruction.

## 1. Environment and Working Directory

Requirements: an installed BART executable, Python with NumPy, Matplotlib in the
selected `PYTHON` environment, and this repository's
`scripts/check_preparation_pair_3d.py` and
`scripts/check_fourier_numpy.py`. See [the documented macOS setup](../../environment/local-macos.md)
for the recorded installation.

Open a terminal and start one Bash session:

```bash
bash
```

Run the remaining blocks in that same session. Copy the contents of code blocks,
without the Markdown fence markers. The paths below are examples matching the
recorded local layout, not required repository locations. Adjust them before
continuing and use absolute paths. `$HOME` expands to your home directory.

```bash
cd "$HOME/projects/ensf620-bart-workflow" || exit "$?"
REPO="$(pwd -P)"
BART="$HOME/software/bart-1.0.00/bart"
PYTHON="$HOME/bart-learning/.venv/bin/python"
PREPARATION_DIR="$HOME/bart-learning/bart-workflow-preparations/generation-3d-01"
RECONSTRUCTION_OUTPUT_DIR="$HOME/bart-learning/bart-workflow-reconstructions/manual-3d-01"
```

For an existing checked preparation, select its actual directory. For a new
preparation, use a new `PREPARATION_DIR`. Always select a new reconstruction
directory outside the preparation directory. Directory creation below rejects
names that already exist.

The checks below reject missing executables or repository files before any
data-processing command runs:

```bash
if [ ! -x "$BART" ] || [ ! -x "$PYTHON" ] ||
   [ ! -f "$REPO/scripts/check_preparation_pair_3d.py" ] ||
   [ ! -f "$REPO/scripts/check_fourier_numpy.py" ]; then
    printf 'ERROR: check the configured executables and repository files.\n' >&2
    exit 1
fi
"$PYTHON" -c 'import numpy' || exit "$?"
"$BART" version -V || exit "$?"
"$PYTHON" --version || exit "$?"
uname -srm || exit "$?"
```

Copy the displayed version and platform information into the execution record
when the full procedure is documented. Each data-processing block below prints
its exit code and stops this Bash session on failure.

## 2. Create and Preserve the Reference Phantom

Create the new preparation directory. Its parent may already exist; the
preparation directory itself must be new.

```bash
mkdir -p "$(dirname "$PREPARATION_DIR")" || exit "$?"
mkdir "$PREPARATION_DIR" || exit "$?"
```

Generate the 3D reference. `phantom -3` selects the 3D Shepp–Logan phantom,
`-x 64` sets its cubic spatial size, and the final argument is the output base
path without an extension:

```bash
if "$BART" phantom -3 -x 64 "$PREPARATION_DIR/reference" \
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
if "$PYTHON" "$REPO/scripts/check_preparation_pair_3d.py" \
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

The 3D checker verifies the first three header dimensions, singleton trailing
axes, the expected little-endian complex64 file size, and finite values.
Preserve the reference pair unchanged.

## 3. Generate and Validate the k-Space

Transform the checked reference into fully sampled Cartesian k-space:

```bash
if "$BART" fft -u 7 "$PREPARATION_DIR/reference" "$PREPARATION_DIR/kspace" \
    > "$PREPARATION_DIR/forward-fft.log" 2>&1; then
    printf 'SUCCESS: k-space generation (exit code 0).\n'
else
    status=$?
    cat "$PREPARATION_DIR/forward-fft.log" >&2
    printf 'ERROR: k-space generation (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

`fft` performs a centered Fourier transform with unitary normalization. The
bitmask `7` selects axes 0, 1, and 2. The inputs and outputs are base paths
identifying `.hdr` / `.cfl` pairs.

Expected output: `kspace.hdr` and `kspace.cfl`. Check the new pair:

```bash
if "$PYTHON" "$REPO/scripts/check_preparation_pair_3d.py" \
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

The reference and k-space are now prepared and checked. These pair checks
establish basic readability and structure; they do not evaluate reconstruction
accuracy. When establishing this 3D case for the first time, continue with
Section 4 to verify regeneration before reconstruction.

## 4. Regenerate and Compare the Synthetic Generations

This check asks whether repeating the preparation produces the same reference
and k-space files in the selected environment. It is separate from
reconstruction. The `.hdr` files can contain generation-specific paths in
`# Command` and `# Files` even when their dimensions, BART version, options,
input/output functions, and stored arrays are the same.

When performing a new regeneration check:

1. Keep the first preparation path and select a new, unused second directory:

   ```bash
   FIRST_PREPARATION_DIR="$PREPARATION_DIR"
   PREPARATION_DIR="$HOME/bart-learning/bart-workflow-preparations/generation-3d-02"
   ```

2. Repeat **Sections 2 and 3 exactly**, using the same Bash session, BART
   executable, Python executable, and parameters. Do not repeat Section 1,
   which would reset the selected paths. Each section writes its logs into the
   currently selected `PREPARATION_DIR`.
3. After both preparations pass their checks, compare the four corresponding
   files:

   ```bash
   comparison_requires_review=0
   {
       printf 'First preparation: %s\nSecond preparation: %s\n' \
           "$FIRST_PREPARATION_DIR" "$PREPARATION_DIR"
       for pair_file in reference.hdr reference.cfl kspace.hdr kspace.cfl; do
           if cmp "$FIRST_PREPARATION_DIR/$pair_file" "$PREPARATION_DIR/$pair_file"; then
               printf 'MATCH: %s (exit code 0)\n' "$pair_file"
           else
               status=$?
               comparison_requires_review=1
               if [ "$status" -eq 1 ]; then
                   printf 'DIFFERENT: %s (exit code 1)\n' "$pair_file"
               else
                   printf 'ERROR: %s (exit code %s)\n' "$pair_file" "$status"
               fi
           fi
       done
   } > "$PREPARATION_DIR/regeneration-comparison.txt" 2>&1 || exit "$?"
   cat "$PREPARATION_DIR/regeneration-comparison.txt"
   if [ "$comparison_requires_review" -ne 0 ]; then
       printf 'ERROR: one or more preparation comparisons require review; stop before reconstruction.\n' >&2
       exit 1
   fi
   ```

   Interpret each file independently: `MATCH` means byte-identical content;
   `DIFFERENT` means different content; `ERROR` means an operational comparison
   error. Preserve the comparison record in the second preparation directory.

4. Select the first preparation again before continuing to reconstruction:

   ```bash
   PREPARATION_DIR="$FIRST_PREPARATION_DIR"
   ```

Record the observed outcomes, including differences or errors. Do not convert
an original `DIFFERENT` result into `MATCH`. If the comparison stops for review,
the comparison record is complete but the preparation is not yet cleared to
continue.

After the Bash session has ended, inspect headers independently with explicit
paths. Run each `diff -u` command separately; exit code `1` means that the
headers differ and must be reviewed, not that the command failed:
The paths below are examples. Replace them with the actual first and second
preparation directories recorded in `regeneration-comparison.txt` before
running either command.

```bash
diff -u \
    "$HOME/bart-learning/bart-workflow-preparations/generation-3d-01/reference.hdr" \
    "$HOME/bart-learning/bart-workflow-preparations/generation-3d-02/reference.hdr"
printf 'reference.hdr diff exit code: %s\n' "$?"

diff -u \
    "$HOME/bart-learning/bart-workflow-preparations/generation-3d-01/kspace.hdr" \
    "$HOME/bart-learning/bart-workflow-preparations/generation-3d-02/kspace.hdr"
printf 'kspace.hdr diff exit code: %s\n' "$?"
```

Save each complete diff and its exit code in the records already described in
Section 9. A documented review may clear the preparation only when both binary
comparisons (`reference.cfl` and `kspace.cfl`, each between generations) report
`MATCH` with exit code `0`, none of the four original comparisons reports
`ERROR`, and both preparations pass their structural checks. Header differences
must be limited to the expected generation-directory paths in `# Command` and
`# Files`. Dimensions, BART version, command options, file base names, and
input/output roles must otherwise match. Preserve the original header
`DIFFERENT` results. Any other difference or operational error remains pending
review.

To resume after an approved header review, start a new Bash session, configure
Section 1 with the existing first preparation selected and a new reconstruction
output directory, then continue at Section 5. This review concerns preparation
equality only; it does not establish reconstruction quality or general
reproducibility.

## 5. Reconstruct the Case with BART

Use the preparation selected in Section 1, or restore the first preparation
after completing Section 4. The selected reference and k-space remain unchanged.
Continue in the same Bash session; the commands use full paths and require no
new `cd`.

Confirm the prepared input and preserved reference, then create the new output
directory:

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

Reconstruct by applying the centered, unitary inverse Fourier transform to the
prepared 3D k-space:

```bash
if "$BART" fft -i -u 7 \
    "$PREPARATION_DIR/kspace" \
    "$RECONSTRUCTION_OUTPUT_DIR/reconstruction" \
    > "$RECONSTRUCTION_OUTPUT_DIR/reconstruction.log" 2>&1; then
    printf 'SUCCESS: BART reconstruction (exit code 0).\n'
else
    status=$?
    cat "$RECONSTRUCTION_OUTPUT_DIR/reconstruction.log" >&2
    printf 'ERROR: BART reconstruction (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

`-i` selects the inverse transform. `-u` requests unitary normalization, and
the bitmask `7` selects axes 0, 1, and 2. Omitting `-n` retains the centered
transform. The prepared reference and k-space remain unchanged.

Expected output: `reconstruction.hdr` and `reconstruction.cfl` in
`RECONSTRUCTION_OUTPUT_DIR`, with the command record in
`reconstruction.log`. The structural check for this output is defined in
Section 6.

## 6. Check the Reconstruction Output

Read and validate the new reconstruction pair:

```bash
if "$PYTHON" "$REPO/scripts/check_preparation_pair_3d.py" \
    "$RECONSTRUCTION_OUTPUT_DIR" reconstruction \
    > "$RECONSTRUCTION_OUTPUT_DIR/reconstruction-check.txt" 2>&1; then
    cat "$RECONSTRUCTION_OUTPUT_DIR/reconstruction-check.txt"
    printf 'SUCCESS: reconstruction-output check (exit code 0).\n'
else
    status=$?
    cat "$RECONSTRUCTION_OUTPUT_DIR/reconstruction-check.txt" >&2
    printf 'ERROR: reconstruction-output check (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

The 3D checker verifies that `reconstruction.hdr` and `reconstruction.cfl`
exist, declare spatial dimensions `64 × 64 × 64`, preserve singleton trailing
axes, have a compatible complex64 binary size, and contain finite values. The
record is saved in `reconstruction-check.txt`.

These are structural checks only. A passing check establishes readability and
the expected output structure; it does not measure agreement with the
synthetic reference or reconstruction quality.

## 7. Perform the Visual Comparison

Run the following block in the same Bash session and with the same `PYTHON`
selected in Section 1. This section requires Matplotlib in that same Python
environment. It reads only the preserved reference and the reconstruction
output:

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

from check_preparation_pair_3d import read_bart_3d

reference = read_bart_3d(reference_base)
reconstruction = read_bart_3d(reconstruction_base)
reference_magnitude = np.abs(reference)
reconstruction_magnitude = np.abs(reconstruction)
reference_max = float(reference_magnitude.max())

if not np.isfinite(reference_max) or reference_max <= 0:
    raise ValueError("reference maximum magnitude must be finite and positive")

reconstruction_max = float(reconstruction_magnitude.max())
if not np.isfinite(reconstruction_max):
    raise ValueError("reconstruction maximum magnitude must be finite")

planes = (
    ("Plane 0-1, axis 2 = 32", lambda values: np.abs(values[:, :, 32]).T),
    ("Plane 0-2, axis 1 = 32", lambda values: np.abs(values[:, 32, :]).T),
    ("Plane 1-2, axis 0 = 32", lambda values: np.abs(values[32, :, :]).T),
)

figure_path = figure_dir / "reference-reconstruction-orthogonal.png"
if figure_path.exists():
    raise FileExistsError(f"refusing to overwrite existing figure: {figure_path}")

figure, axes = plt.subplots(
    2, 3, figsize=(13, 8), constrained_layout=True, squeeze=False
)
image = None
for column, (title, cut) in enumerate(planes):
    for row, values, label in (
        (0, reference, "Reference"),
        (1, reconstruction, "BART reconstruction"),
    ):
        displayed = cut(values)
        image = axes[row, column].imshow(
            displayed,
            cmap="gray",
            origin="lower",
            aspect="equal",
            interpolation="none",
            vmin=0,
            vmax=reference_max,
        )
        axes[row, column].set_title(f"{label}: {title}")
        axes[row, column].set_xlabel("Array index")
        axes[row, column].set_ylabel("Array index")
figure.colorbar(image, ax=axes, label="Magnitude")
figure.savefig(figure_path, dpi=160)
plt.close(figure)

print(f"Reference input: {reference_base}.hdr/.cfl")
print(f"Reconstruction input: {reconstruction_base}.hdr/.cfl")
print(f"Python: {platform.python_version()}")
print(f"NumPy: {np.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
print("Array shape: (64, 64, 64); disk order: Fortran (order='F')")
print("Displayed planes, zero-based indices:")
for title, _ in planes:
    print(f"- {title}")
print(
    'Display: np.abs(V[:, :, 32]).T, np.abs(V[:, 32, :]).T, '
    'np.abs(V[32, :, :]).T'
)
print('Presentation: origin="lower", aspect="equal", interpolation="none"')
print("Colormap: gray")
print(f"Shared magnitude limits: 0 to {reference_max:.9e}")
if reconstruction_max > reference_max:
    print(
        "Global reconstruction magnitude exceeds the shared upper limit; "
        "this does not by itself establish clipping in every displayed slice."
    )
else:
    print("Global reconstruction magnitude does not exceed the shared upper limit.")

for title, cut in planes:
    reference_slice_max = float(cut(reference_magnitude).max())
    reconstruction_slice_max = float(cut(reconstruction_magnitude).max())
    print(
        f"{title}: reference slice maximum={reference_slice_max:.9e}; "
        f"reconstruction slice maximum={reconstruction_slice_max:.9e}; "
        f"reconstruction slice exceeds display limit="
        f"{reconstruction_slice_max > reference_max}"
    )
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

The block generates one file at:

```text
$FIGURE_DIR/reference-reconstruction-orthogonal.png
```

The figure contains reference slices in the top row and reconstruction slices
in the bottom row. It uses zero-based array indices and applies the same
display transformation and presentation options to both volumes. The visual
operation does not modify the source files or the complex arrays reserved for a
future quantitative comparison.

The log records the selected planes, presentation options, shared magnitude
limits, global maximum comparison, and per-plane maximum comparison. A global
reconstruction excess is reported separately from whether each displayed slice
exceeds the upper display limit. This visual comparison does not calculate a
metric, select a tolerance, or establish a pass/fail criterion.

## 8. Perform the Quantitative Reference Comparison

Calculate the complex relative L2 error between the preserved reference and the
corresponding BART reconstruction using every complex value in the full volume:

```text
||reconstruction - reference||₂ / ||reference||₂
```

The `.cfl` files store complex64 values. `read_bart_3d` validates the files,
preserves BART storage order with `order="F"`, and returns complex128 arrays for
the calculation. Use the original complex arrays for the complete
`64 × 64 × 64` volume. Do not convert to magnitude, use visual slices,
transpose, crop, mask, align, rescale, or correct phase. The denominator check
and finite-result check are provided by the existing `relative_error` function;
the denominator is validated before division and the result is validated after
the calculation. Do not select a tolerance or pass/fail criterion.

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

from check_preparation_pair_3d import read_bart_3d
from check_fourier_numpy import relative_error

reference = read_bart_3d(reference_base)
reconstruction = read_bart_3d(reconstruction_base)
error = relative_error(reference, reconstruction)
reference_norm = float(np.linalg.norm(reference.ravel()))

print(f"Reference input: {reference_base}.hdr/.cfl")
print(f"Reconstruction input: {reconstruction_base}.hdr/.cfl")
print(f"Reference shape: {reference.shape}")
print(f"Reconstruction shape: {reconstruction.shape}")
print("Stored data: complex64 in BART .cfl files")
print("Calculation arrays: complex128 returned by read_bart_3d")
print("Volume included: all complex values in the complete 64 x 64 x 64 volume")
print("Metric: ||reconstruction - reference||_2 / ||reference||_2")
print("Preprocessing: none; no magnitude conversion, visual slices, transpose, crop, mask, alignment, scaling, or phase correction")
print("Denominator: checked by relative_error before division")
print("Result finiteness: checked by relative_error after calculation")
print(f"Reference L2 norm (diagnostic): {reference_norm:.9e}")
print(f"Python: {platform.python_version()}")
print(f"NumPy: {np.__version__}")
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

The file records the selected inputs, shapes, stored and calculation
precisions, complete-volume complex comparison, formula, no-preprocessing
conditions, denominator and result checks, versions, observed error, and
Python's exit code. A code `0` indicates that the calculation completed
operationally. The result is a case-specific observed difference, not general
validation or a pass/fail decision. This block does not generate a
reconstruction or figure and does not invoke the main comparison program.

## 9. Record Commands, Configuration, Results, and Limitations

Use the following short record format while executing the procedure. Keep notes
in a text editor from the start and add each executed operation's actual outcome
immediately afterward. Keep preparation and regeneration records and all
reconstruction-stage logs and figures in their local execution directories,
outside the repository. Refer to those files from the run record instead of
duplicating their contents.

- For preparation, save `preparation-record.txt` in each preparation directory.
  The first and second generations need separate records when regeneration is
  performed.
- Preserve `regeneration-comparison.txt` in the second preparation directory
  and record its actual path.
- For reconstruction, preserve these files in `RECONSTRUCTION_OUTPUT_DIR`:
  `reconstruction.log`, `reconstruction-check.txt`,
  `visual-comparison.log`,
  `figures-visual/reference-reconstruction-orthogonal.png`, and
  `quantitative-comparison.txt`.
- Record commands, effective parameters, executable and library versions,
  selected paths, produced files, observations, and exit codes. Link to the
  existing logs and figures rather than copying their output into the record.
- Keep figure-generation results separate from Ricardo's visual observations.
  The figure-generation log records the command outcome and display settings;
  human observations are recorded separately after inspecting the saved figure.
- Record the observed quantitative result and its calculation conditions without
  applying a tolerance or pass/fail classification.
- A cumulative `run-record.md` is optional and is not required for this
  procedure. If it exists, preserve it in the local execution directory and do
  not treat it as a substitute for the stage-specific records.

```markdown
# Manual Cartesian 3D Run Record

- Date/time and time zone: <observed value>
- Operator: <name>
- Repository location and revision/local changes, if known: <details>
- BART executable and version/build: <actual values>
- Python executable/version, NumPy version, Matplotlib version if recorded, and platform: <actual values>
- First preparation: <absolute path; link to its record>
- Second preparation, if regeneration was performed: <absolute path; link to its record>
- Regeneration comparison: <record path; each file's observed result and code>
- Reconstruction output: <absolute path>
- Effective settings: <actual phantom command, dimensions, channels, sampling, FFT options>

| Step actually performed | Exact command/invocation | Exit code | Observation | Log/evidence link |
|---|---|---:|---|---|
| <step> | <command> | <observed code> | <observed result> | [Evidence](<relative-path>) |

- Produced files: <actual files>
- Visual figure generation: <approved method not executed / observed command result and figure link>
- Visual observations by Ricardo: <observations after inspecting the saved figure / not recorded>
- Quantitative comparison: <approved method not executed / observed result and record link>
- Failures, corrections, and unresolved issues: <observations or none reported>
- Limitations: <what this execution did and did not demonstrate>
```

Add one table row per executed operation. Mark stages not performed as
`NOT_EXECUTED`; do not label them failed or fill them with historical results
from the 2D case. An exit code of `0` describes command success, not a
reconstruction-quality criterion. Keep preparation, regeneration,
reconstruction, structural checks, figure generation, visual observations, and
quantitative results distinguishable through their local records and links.

## Appendix A. Optional Interactive Slice Inspection

This optional inspection reads an existing reference and reconstruction and
opens an interactive Matplotlib window for manual review. It requires an
interactive Matplotlib backend in the `PYTHON` environment selected in
Section 1. This block does not select or change the global backend
configuration. If the selected backend is non-interactive or cannot open a
window, it reports an error instead of claiming that inspection succeeded.

Run this block in the same Bash session after configuring the paths in Section 1:

```bash
if "$PYTHON" - "$REPO" "$PREPARATION_DIR/reference" \
    "$RECONSTRUCTION_OUTPUT_DIR/reconstruction" <<'PY'
import sys
from pathlib import Path

import numpy as np

repo = Path(sys.argv[1])
reference_base = sys.argv[2]
reconstruction_base = sys.argv[3]
sys.path.insert(0, str(repo / "scripts"))

try:
    import matplotlib
    from matplotlib.backends import backend_registry
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Slider

    resolved_backend, gui_framework = backend_registry.resolve_backend(
        matplotlib.get_backend()
    )
    supported_gui_frameworks = {
        "macosx",
        "qt",
        "qt5",
        "tk",
        "wx",
        "gtk3",
        "gtk4",
    }
    print(f"Resolved Matplotlib backend: {resolved_backend}")
    print(f"Resolved GUI framework: {gui_framework}")
    if gui_framework not in supported_gui_frameworks:
        raise RuntimeError(
            f"Resolved GUI framework {gui_framework!r} for backend "
            f"{resolved_backend!r} is not supported by this optional appendix; "
            "a supported desktop GUI backend is required."
        )

    from check_preparation_pair_3d import read_bart_3d

    reference = read_bart_3d(reference_base)
    reconstruction = read_bart_3d(reconstruction_base)
    reference_magnitude = np.abs(reference)
    reconstruction_magnitude = np.abs(reconstruction)
    reference_max = float(reference_magnitude.max())

    if not np.isfinite(reference_max) or reference_max <= 0:
        raise ValueError("reference maximum magnitude must be finite and positive")

    if not np.isfinite(reconstruction_magnitude).all():
        raise ValueError("reconstruction magnitude must contain finite values")

    initial_index = 32
    figure, axes = plt.subplots(1, 2, figsize=(10, 4.5))
    figure.subplots_adjust(bottom=0.22, wspace=0.25)

    def displayed(values: np.ndarray, index: int) -> np.ndarray:
        return values[:, :, index].T

    images = (
        axes[0].imshow(
            displayed(reference_magnitude, initial_index),
            cmap="gray",
            origin="lower",
            aspect="equal",
            interpolation="none",
            vmin=0,
            vmax=reference_max,
        ),
        axes[1].imshow(
            displayed(reconstruction_magnitude, initial_index),
            cmap="gray",
            origin="lower",
            aspect="equal",
            interpolation="none",
            vmin=0,
            vmax=reference_max,
        ),
    )
    axes[0].set_xlabel("Array axis 0 index")
    axes[0].set_ylabel("Array axis 1 index")
    axes[1].set_xlabel("Array axis 0 index")
    axes[1].set_ylabel("Array axis 1 index")

    def update(index: float) -> None:
        selected_index = int(round(index))
        images[0].set_data(displayed(reference_magnitude, selected_index))
        images[1].set_data(displayed(reconstruction_magnitude, selected_index))
        axes[0].set_title(f"Reference: plane 0-1, axis 2 = {selected_index}")
        axes[1].set_title(
            f"Reconstruction: plane 0-1, axis 2 = {selected_index}"
        )
        figure.canvas.draw_idle()

    update(initial_index)
    colorbar = figure.colorbar(images[1], ax=axes, label="Magnitude")
    colorbar.mappable.set_clim(0, reference_max)

    slider_axis = figure.add_axes((0.15, 0.08, 0.7, 0.04))
    slider = Slider(
        slider_axis,
        "Axis 2 index",
        valmin=0,
        valmax=63,
        valinit=initial_index,
        valstep=1,
    )
    slider.on_changed(update)
    figure.suptitle("Interactive plane 0-1 inspection")
    plt.show(block=True)
except (ImportError, OSError, RuntimeError, ValueError) as exc:
    print(f"ERROR: interactive slice inspection unavailable: {exc}", file=sys.stderr)
    raise SystemExit(1)
PY
then
    printf 'SUCCESS: interactive viewer closed normally (exit code 0).\n'
else
    status=$?
    printf 'ERROR: interactive slice inspection failed (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

The viewer uses the complete reference-volume maximum as a fixed shared display
limit from zero through navigation. Magnitudes above that maximum saturate
visually. It applies the same transposed plane display, `origin="lower"`,
`aspect="equal"`, `interpolation="none"`, and gray colormap to both panels,
without assigning anatomical orientation to the array axes.

This is optional manual inspection of an existing reconstruction. It complements
the saved static figure and the full-volume complex comparison, does not create
new data, figures, metrics, or records, and is not a dependency of future
non-interactive automation or a mandatory condition for closing the executed
case. Successful viewer termination only indicates that the window closed
normally; it does not establish that Ricardo inspected every slice or reached a
visual conclusion.
