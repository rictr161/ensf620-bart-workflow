# Manual Cartesian 3D Compressed-Sensing Tutorial

This tutorial describes the manual Cartesian 3D compressed-sensing procedure
for the confirmed synthetic case: a BART-generated 64 × 64 × 64 Shepp–Logan
phantom with one channel. Array axis 0 represents readout, and axes 1 and 2
represent the phase dimensions.

It covers preparation, regeneration verification, BART reconstruction,
structural checks, visual and quantitative reference comparisons, and local
execution records.

| File pair | Role |
|---|---|
| `reference.hdr` / `reference.cfl` | Preserved synthetic reference volume. |
| `kspace_full.hdr` / `kspace_full.cfl` | Fully sampled Cartesian k-space generated from the reference. |
| `mask2d.hdr` / `mask2d.cfl` | Prepared two-dimensional phase mask before repetition. |
| `mask3d.hdr` / `mask3d.cfl` | Three-dimensional mask repeated along the readout axis. |
| `kspace_undersampled.hdr` / `kspace_undersampled.cfl` | K-space after applying the binary mask. |
| `sensitivities.hdr` / `sensitivities.cfl` | Constant single-channel sensitivity map. |
| `reconstruction.hdr` / `reconstruction.cfl` | Reconstructed volume in `RECONSTRUCTION_OUTPUT_DIR`. |

Use a new preparation directory, separate from any fully sampled 3D
preparation or reconstruction output directory. The confirmed example values
are specific to this manual case and do not define universal automation
defaults.

## 1. Environment and Working Directory

Requirements: an installed BART executable, Python with NumPy and Matplotlib,
and this repository's `scripts/check_preparation_pair_3d.py` and
`scripts/check_fourier_numpy.py`. See
[the documented macOS setup](../../environment/local-macos.md) for the recorded
installation.

Open a terminal and start one Bash session:

```bash
bash
```

Run the remaining blocks in that same session. Copy the contents of code
blocks, without the Markdown fence markers. The paths below are examples
matching the recorded local layout. Adjust them before continuing and use
absolute paths. `$HOME` expands to your home directory.

```bash
cd "$HOME/projects/ensf620-bart-workflow" || exit "$?"
REPO="$(pwd -P)"
BART="$HOME/software/bart-1.0.00/bart"
PYTHON="$HOME/bart-learning/.venv/bin/python"
PREPARATION_DIR="$HOME/bart-learning/bart-workflow-preparations/generation-3d-cs-01"
RECONSTRUCTION_OUTPUT_DIR="$HOME/bart-learning/bart-workflow-reconstructions/manual-3d-cs-01"
```

Use a new `PREPARATION_DIR` when establishing the case. After its initial
verification, the existing preparation may be reused. Every reconstruction
must use a new `RECONSTRUCTION_OUTPUT_DIR` separate from the preparation.

The checks below reject missing executables or repository files before any
data-processing command runs:

```bash
if [ ! -x "$BART" ] || [ ! -x "$PYTHON" ] ||
   [ ! -f "$REPO/scripts/check_preparation_pair_3d.py" ] ||
   [ ! -f "$REPO/scripts/check_fourier_numpy.py" ]; then
    printf 'ERROR: check the configured executables and repository files.\n' >&2
    exit 1
fi
"$PYTHON" -c 'import numpy, matplotlib' || exit "$?"
"$BART" version -V || exit "$?"
"$PYTHON" --version || exit "$?"
uname -srm || exit "$?"
```

Copy the displayed version and platform information into the execution record
when the complete procedure is documented. This block does not execute any
compressed-sensing reconstruction.

## 2. Create and Preserve the Reference Phantom

Create the new preparation directory. Its parent may already exist; the
preparation directory itself must be new.

```bash
mkdir -p "$(dirname "$PREPARATION_DIR")" || exit "$?"
mkdir "$PREPARATION_DIR" || exit "$?"
```

Generate the confirmed 3D reference:

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

`phantom` generates BART's synthetic Shepp–Logan phantom. `-3` selects the 3D
case, and `-x 64` sets the three spatial dimensions to 64. The final argument
is the output base path; BART writes the `.hdr` and `.cfl` pair.

Expected output: `reference.hdr` and `reference.cfl` in
`PREPARATION_DIR`. Validate that pair before generating k-space:

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

The checker verifies the first three dimensions, trailing singleton axes,
complex64 file size, and finite values. Preserve the reference pair unchanged.

## 3. Generate and Validate the Fully Sampled K-Space

Generate the fully sampled Cartesian k-space from the checked reference:

```bash
if "$BART" fft -u 7 \
    "$PREPARATION_DIR/reference" \
    "$PREPARATION_DIR/kspace_full" \
    > "$PREPARATION_DIR/kspace-full-fft.log" 2>&1; then
    printf 'SUCCESS: full k-space generation (exit code 0).\n'
else
    status=$?
    cat "$PREPARATION_DIR/kspace-full-fft.log" >&2
    printf 'ERROR: full k-space generation (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

`fft` performs the centered Fourier transform. `-u` requests unitary
normalization, and bitmask `7` selects array axes 0, 1, and 2. Thus this
operation transforms the complete 3D volume without undersampling. The
`kspace_full` base name distinguishes this preserved input from the later
undersampled k-space.

Expected output: `kspace_full.hdr` and `kspace_full.cfl`. Validate that pair:

```bash
if "$PYTHON" "$REPO/scripts/check_preparation_pair_3d.py" \
    "$PREPARATION_DIR" kspace_full \
    > "$PREPARATION_DIR/kspace-full-check.txt" 2>&1; then
    cat "$PREPARATION_DIR/kspace-full-check.txt"
    printf 'SUCCESS: full k-space check (exit code 0).\n'
else
    status=$?
    cat "$PREPARATION_DIR/kspace-full-check.txt" >&2
    printf 'ERROR: full k-space check (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

The validated `reference` and `kspace_full` pairs are the preserved inputs for
the later mask-preparation stage.

## 4. Generate and Validate the Sampling Mask

Generate the two-dimensional variable-density Poisson pattern:

```bash
if "$BART" poisson \
    -Y 64 -Z 64 \
    -y 2 -z 2 \
    -C 16 \
    -v \
    -s 620 \
    "$PREPARATION_DIR/mask2d" \
    > "$PREPARATION_DIR/mask2d-poisson.log" 2>&1; then
    printf 'SUCCESS: 2D mask generation (exit code 0).\n'
else
    status=$?
    cat "$PREPARATION_DIR/mask2d-poisson.log" >&2
    printf 'ERROR: 2D mask generation (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

`-Y 64 -Z 64` sets the two phase dimensions to match the corresponding
dimensions of the 3D volume. `-y 2 -z 2` specify the two per-axis
undersampling parameters; their nominal product is `2 × 2 = 4`, not a
guarantee of the effective acceleration. `-C 16` requests the confirmed
16 × 16 fully sampled central region in the phase plane. `-v` requests the
variable-density pattern, and `-s 620` fixes the seed for this confirmed
manual case. Regeneration will compare the generated masks to check
repeatability. No elliptical-sampling option is used, so the proposed
domain remains the complete square 64 × 64 phase plane. These values are
case-specific choices and are not presented as optimal.

The native output is expected to be `1 × 64 × 64`, with all later dimensions
singleton. Repeat that phase pattern along the readout axis:

```bash
if "$BART" repmat 0 64 \
    "$PREPARATION_DIR/mask2d" \
    "$PREPARATION_DIR/mask3d" \
    > "$PREPARATION_DIR/mask3d-repmat.log" 2>&1; then
    printf 'SUCCESS: 3D mask repetition (exit code 0).\n'
else
    status=$?
    cat "$PREPARATION_DIR/mask3d-repmat.log" >&2
    printf 'ERROR: 3D mask repetition (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

`repmat 0 64` repeats the same phase-selection plane 64 times along array axis
0, the readout axis. The expected output is `64 × 64 × 64`, with all later
dimensions singleton. It does not generate independent readout samples.

The following bounded Python check reads the two BART pairs directly because
the existing 3D reader expects `64 × 64 × 64` and is not suitable for the
native `mask2d` shape:

```bash
if "$PYTHON" - "$PREPARATION_DIR" \
    > "$PREPARATION_DIR/mask-check.txt" 2>&1 <<'PY'
from pathlib import Path
import sys

import numpy as np


COMPLEX64 = np.dtype("<c8")
EXPECTED_2D = (1, 64, 64)
EXPECTED_3D = (64, 64, 64)


def read_pair(directory: Path, name: str, expected_shape: tuple[int, ...]) -> np.ndarray:
    header = directory / f"{name}.hdr"
    binary = directory / f"{name}.cfl"
    if not header.is_file() or not binary.is_file():
        raise ValueError(f"{name}: expected .hdr and .cfl files")

    lines = [line.strip() for line in header.read_text().splitlines()]
    try:
        dimensions = tuple(
            int(value) for value in lines[lines.index("# Dimensions") + 1].split()
        )
    except (ValueError, IndexError) as exc:
        raise ValueError(f"{header}: invalid dimensions header") from exc

    if dimensions[: len(expected_shape)] != expected_shape or any(
        dimension != 1 for dimension in dimensions[len(expected_shape) :]
    ):
        raise ValueError(
            f"{header}: expected {expected_shape} with trailing singleton axes"
        )

    expected_bytes = int(np.prod(dimensions)) * COMPLEX64.itemsize
    if binary.stat().st_size != expected_bytes:
        raise ValueError(f"{binary}: file size does not match the header")

    values = np.fromfile(binary, dtype=COMPLEX64)
    if not np.isfinite(values).all():
        raise ValueError(f"{binary}: non-finite values detected")
    return values.reshape(expected_shape, order="F")


directory = Path(sys.argv[1])
mask2d = read_pair(directory, "mask2d", EXPECTED_2D)
mask3d = read_pair(directory, "mask3d", EXPECTED_3D)

if not np.isin(mask2d, (0 + 0j, 1 + 0j)).all() or not np.isin(
    mask3d, (0 + 0j, 1 + 0j)
).all():
    raise ValueError("mask values must be exactly 0 + 0j or 1 + 0j")

expected_mask3d = np.repeat(mask2d, 64, axis=0)
if not np.array_equal(mask3d, expected_mask3d):
    raise ValueError("mask3d does not exactly repeat mask2d along axis 0")

central = mask2d[0, 24:40, 24:40]
if not np.array_equal(central, np.ones((16, 16), dtype=np.complex64)):
    raise ValueError("mask2d central region 24:40, 24:40 is not fully active")

nonzero_count = int(np.count_nonzero(mask3d))
total_count = int(mask3d.size)
if not 0 < nonzero_count < total_count:
    raise ValueError("mask3d must contain both acquired and omitted samples")

sampling_fraction = nonzero_count / total_count
effective_acceleration = 1 / sampling_fraction

print(f"mask2d shape: {mask2d.shape}")
print(f"mask3d shape: {mask3d.shape}")
print(f"mask2d nonzero count: {int(np.count_nonzero(mask2d))}")
print(f"mask3d nonzero count: {nonzero_count}")
print(f"mask3d total count: {total_count}")
print(f"sampling_fraction: {sampling_fraction:.12g}")
print(f"effective_acceleration: {effective_acceleration:.12g}")
print("Binary values: validated as exactly 0 + 0j or 1 + 0j")
print("Central region: mask2d[0, 24:40, 24:40] fully active")
print("Axis 0 repetition: mask3d exactly matches 64 repetitions of mask2d")
PY
then
    status=0
else
    status=$?
fi

printf 'Mask-check exit code: %s\n' "$status" >> "$PREPARATION_DIR/mask-check.txt"
cat "$PREPARATION_DIR/mask-check.txt"
if [ "$status" -ne 0 ]; then
    printf 'ERROR: mask checks failed; preserve the record: %s\n' \
        "$PREPARATION_DIR/mask-check.txt" >&2
    exit "$status"
fi
```

The check confirms both expected shapes, trailing singleton axes, compatible
binary storage, finite values, exact repetition along the readout axis, and
the active central 16 × 16 region using zero-based phase indices `24:40`.
The central region is included once in the `mask3d` count. The reported
`sampling_fraction` and `effective_acceleration` are calculated from all
`64 × 64 × 64` mask entries; they are observed values and are not adjusted to
force an acceleration of 4.

## 5. Apply and Validate the Sampling Mask

Multiply the preserved fully sampled k-space by the prepared three-dimensional
binary mask:

```bash
if "$BART" fmac \
    "$PREPARATION_DIR/kspace_full" \
    "$PREPARATION_DIR/mask3d" \
    "$PREPARATION_DIR/kspace_undersampled" \
    > "$PREPARATION_DIR/kspace-undersampled-fmac.log" 2>&1; then
    printf 'SUCCESS: undersampled k-space generation (exit code 0).\n'
else
    status=$?
    cat "$PREPARATION_DIR/kspace-undersampled-fmac.log" >&2
    printf 'ERROR: undersampled k-space generation (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

`fmac` performs elementwise complex multiplication. Positions selected by the
mask retain the corresponding complex values from `kspace_full`; omitted
positions become zero. The output remains a `64 × 64 × 64` BART array and is
stored under a distinct name so that `reference`, `kspace_full`, `mask2d`, and
`mask3d` remain unchanged. The saved mask is still required to identify
acquired positions, including acquired positions whose k-space value happens
to be zero.

Validate the application using the existing `read_bart_3d` support function:

```bash
if "$PYTHON" - "$REPO" "$PREPARATION_DIR" \
    > "$PREPARATION_DIR/kspace-undersampled-check.txt" 2>&1 <<'PY'
from pathlib import Path
import sys

import numpy as np


repo = Path(sys.argv[1])
preparation_directory = Path(sys.argv[2])
sys.path.insert(0, str(repo / "scripts"))

from check_preparation_pair_3d import read_bart_3d


def read_prepared(name: str) -> np.ndarray:
    return read_bart_3d(str(preparation_directory / name))


kspace_full_path = preparation_directory / "kspace_full"
mask3d_path = preparation_directory / "mask3d"
kspace_undersampled_path = preparation_directory / "kspace_undersampled"

kspace_full = read_prepared("kspace_full")
mask3d = read_prepared("mask3d")
kspace_undersampled = read_prepared("kspace_undersampled")

if not np.isin(mask3d, (0 + 0j, 1 + 0j)).all():
    raise ValueError("mask3d must contain only 0 + 0j and 1 + 0j")

acquired = mask3d == 1
omitted = mask3d == 0
acquired_count = int(np.count_nonzero(acquired))
omitted_count = int(np.count_nonzero(omitted))
if acquired_count == 0 or omitted_count == 0:
    raise ValueError("mask3d must contain both acquired and omitted positions")

acquired_match = np.array_equal(
    kspace_undersampled[acquired],
    kspace_full[acquired],
)
omitted_zero = np.all(kspace_undersampled[omitted] == 0)
if not acquired_match:
    raise ValueError("acquired k-space values differ from kspace_full")
if not omitted_zero:
    raise ValueError("omitted k-space values are not all zero")

print(f"kspace_full: {kspace_full_path}.hdr/.cfl")
print(f"mask3d: {mask3d_path}.hdr/.cfl")
print(f"kspace_undersampled: {kspace_undersampled_path}.hdr/.cfl")
print(f"kspace_full shape: {kspace_full.shape}")
print(f"mask3d shape: {mask3d.shape}")
print(f"kspace_undersampled shape: {kspace_undersampled.shape}")
print(f"Acquired positions: {acquired_count}")
print(f"Omitted positions: {omitted_count}")
print("Acquired-value equality: PASS (exact np.array_equal)")
print("Omitted-value zero check: PASS (exact np.all)")
print("This check validates mask application, not reconstruction quality.")
PY
then
    status=0
else
    status=$?
fi

printf 'Undersampled k-space check exit code: %s\n' "$status" \
    >> "$PREPARATION_DIR/kspace-undersampled-check.txt"
cat "$PREPARATION_DIR/kspace-undersampled-check.txt"
if [ "$status" -ne 0 ]; then
    printf 'ERROR: undersampled k-space checks failed; preserve the record: %s\n' \
        "$PREPARATION_DIR/kspace-undersampled-check.txt" >&2
    exit "$status"
fi
```

The check reuses the existing 3D reader for all three prepared pairs, confirms
the mask is binary and contains both acquired and omitted positions, and
verifies exact preservation and zeroing without numerical tolerances. It
validates preparation of the reconstruction input only; it does not evaluate
reconstruction quality.

## 6. Generate and Validate the Constant Sensitivity Map

Generate the confirmed ideal uniform sensitivity map:

```bash
if "$BART" ones 5 64 64 64 1 1 \
    "$PREPARATION_DIR/sensitivities" \
    > "$PREPARATION_DIR/sensitivities-ones.log" 2>&1; then
    printf 'SUCCESS: sensitivity-map generation (exit code 0).\n'
else
    status=$?
    cat "$PREPARATION_DIR/sensitivities-ones.log" >&2
    printf 'ERROR: sensitivity-map generation (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

`ones` generates a complex array whose values are `1 + 0j`. The leading `5`
is the number of dimensions specified by the command; it is not a mask or
bitmask. The next three sizes, `64 64 64`, correspond to the spatial volume.
The first trailing `1` is axis 3, representing one channel. The second
trailing `1` is axis 4, representing one set of sensitivity maps. Any later
axes are singleton. The constant value represents the ideal uniform
sensitivity selected for this example: it is not estimated by calibration and
does not introduce spatial variation. It is `1 + 0j` throughout the volume,
including the phantom background.

Validate the map with the existing 3D reader:

```bash
if "$PYTHON" - "$REPO" "$PREPARATION_DIR" \
    > "$PREPARATION_DIR/sensitivities-check.txt" 2>&1 <<'PY'
from pathlib import Path
import sys

import numpy as np


repo = Path(sys.argv[1])
preparation_directory = Path(sys.argv[2])
sys.path.insert(0, str(repo / "scripts"))

from check_preparation_pair_3d import read_bart_3d


sensitivities_path = preparation_directory / "sensitivities"
sensitivities = read_bart_3d(str(sensitivities_path))
if not np.all(sensitivities == (1.0 + 0.0j)):
    raise ValueError("sensitivities must equal 1 + 0j at every spatial position")

print(f"sensitivities: {sensitivities_path}.hdr/.cfl")
print(f"Spatial shape read: {sensitivities.shape}")
print("Constant-value check: PASS (exact np.all)")
print(
    "The reader returned the spatial representation after verifying "
    "trailing singleton axes in the header."
)
PY
then
    status=0
else
    status=$?
fi

printf 'Sensitivity-map check exit code: %s\n' "$status" \
    >> "$PREPARATION_DIR/sensitivities-check.txt"
cat "$PREPARATION_DIR/sensitivities-check.txt"
if [ "$status" -ne 0 ]; then
    printf 'ERROR: sensitivity-map check failed; preserve the record: %s\n' \
        "$PREPARATION_DIR/sensitivities-check.txt" >&2
    exit "$status"
fi
```

The existing reader checks the header dimensions, trailing singleton axes,
complex64 file size, and finite values before returning the spatial
representation. The exact equality check then verifies the specified
constant map without a numerical tolerance.

## 7. Regenerate and Compare the Complete Preparation

This section checks whether repeating Sections 2–6 produces the same six
prepared file pairs in the same environment. It is a preparation
reproducibility check, not a reconstruction-quality evaluation.

Before regenerating, preserve the first preparation and select a new
preparation directory:

```bash
FIRST_PREPARATION_DIR="$PREPARATION_DIR"
PREPARATION_DIR="$HOME/bart-learning/bart-workflow-preparations/generation-3d-cs-02"
```

Keep both paths unchanged and explicit. In the same Bash session, repeat
Sections 2–6 exactly, using the same `BART`, `PYTHON`, confirmed parameters,
and seed. Do not repeat Section 1: it would reset the initial path variables.
Both preparations must complete all generation and validation checks before
the comparison below. The first preparation remains in
`FIRST_PREPARATION_DIR`; the second preparation is in the current
`PREPARATION_DIR`.

Compare all corresponding `.hdr` and `.cfl` files. The block records every
comparison before stopping for review:

```bash
REGENERATION_COMPARISON="$PREPARATION_DIR/regeneration-comparison.txt"
comparison_requires_review=0
different_headers=()

{
    printf 'First preparation: %s\n' "$FIRST_PREPARATION_DIR"
    printf 'Second preparation: %s\n' "$PREPARATION_DIR"
    printf 'Both preparations were required to pass Sections 2–6 before comparison.\n'
    printf '\n'

    for pair_name in \
        reference \
        kspace_full \
        mask2d \
        mask3d \
        kspace_undersampled \
        sensitivities; do
        for extension in hdr cfl; do
            first_file="$FIRST_PREPARATION_DIR/$pair_name.$extension"
            second_file="$PREPARATION_DIR/$pair_name.$extension"
            if cmp "$first_file" "$second_file"; then
                printf 'MATCH: %s.%s (exit code 0)\n' "$pair_name" "$extension"
            else
                status=$?
                comparison_requires_review=1
                if [ "$status" -eq 1 ]; then
                    printf 'DIFFERENT: %s.%s (exit code 1)\n' \
                        "$pair_name" "$extension"
                    if [ "$extension" = "hdr" ]; then
                        different_headers[${#different_headers[@]}]="$pair_name"
                    fi
                else
                    printf 'ERROR: %s.%s (exit code %s)\n' \
                        "$pair_name" "$extension" "$status"
                fi
            fi
        done
    done
} > "$REGENERATION_COMPARISON" 2>&1 || exit "$?"

cat "$REGENERATION_COMPARISON"
```

The loop performs twelve comparisons: `.hdr` and `.cfl` for each of the six
pairs. It captures each `cmp` result immediately, records all results, and
sets an accumulated review indicator without stopping at the first
difference or error.

For every header recorded as `DIFFERENT`, register the unified diff and its
exit code in the same comparison record:

```bash
{
    for pair_name in "${different_headers[@]}"; do
        first_header="$FIRST_PREPARATION_DIR/$pair_name.hdr"
        second_header="$PREPARATION_DIR/$pair_name.hdr"
        printf 'Header diff: %s.hdr\n' "$pair_name"
        header_diff_status=0
        diff -u "$first_header" "$second_header" || header_diff_status=$?
        printf 'Header diff exit code: %s.hdr (exit code %s)\n' \
            "$pair_name" "$header_diff_status"
        if [ "$header_diff_status" -ne 1 ]; then
            comparison_requires_review=1
        fi
    done
} >> "$REGENERATION_COMPARISON" 2>&1 || exit "$?"

cat "$REGENERATION_COMPARISON"
```

The header review may resolve differences only when all six `.cfl`
comparisons report `MATCH` with exit code `0`, no original comparison reports
`ERROR`, both preparations completed Sections 2–6, and the header changes are
limited to expected generation-directory paths in `# Command` and `# Files`.
Dimensions, BART version, options, seed where applicable, base names, and
input/output functions must otherwise remain equal. Preserve the original
`DIFFERENT` results and all files without modification. Any other difference
or operational error remains pending review.

If any original comparison or header review still requires attention, stop
without restoring the first preparation:

```bash
if [ "$comparison_requires_review" -ne 0 ]; then
    printf 'ERROR: regeneration comparison requires review; preserve both preparations and the record: %s\n' \
        "$REGENERATION_COMPARISON" >&2
    exit 1
fi
```

After a satisfactory comparison and any documented header review, restore the
first preparation for later work:

```bash
PREPARATION_DIR="$FIRST_PREPARATION_DIR"
printf 'Restored preparation: %s\n' "$PREPARATION_DIR"
```

The comparison record remains in the second preparation directory. If all
comparisons are `MATCH`, restore the first preparation within the current
session as shown above. If the procedure stops, Ricardo must review and
document the differences. Once they are resolved, open a new Bash session and
configure `BART`, `PYTHON`, `REPO`, `PREPARATION_DIR`, and
`RECONSTRUCTION_OUTPUT_DIR` directly with the existing first CS preparation.
Do not depend on variables from the terminated session, recreate either
preparation, repeat Sections 2–7, or overwrite their records. Continue with
Section 8.

## 8. Reconstruct the Confirmed CS Case with BART

Use the first preparation after its initial verification and any required
regeneration review. The preparation may be reused for later reconstructions,
but each reconstruction output must use a new directory separate from it.
When continuing after a stopped Section 7, configure the existing first
preparation and a new output directory directly in the new Bash session; do
not recreate the preparations or repeat the comparison.

Confirm the required prepared pairs and create a new reconstruction directory:

```bash
for pair_file in \
    reference \
    kspace_undersampled \
    mask3d \
    sensitivities; do
    if [ ! -f "$PREPARATION_DIR/$pair_file.hdr" ] ||
       [ ! -f "$PREPARATION_DIR/$pair_file.cfl" ]; then
        printf 'ERROR: missing prepared pair: %s\n' \
            "$PREPARATION_DIR/$pair_file" >&2
        exit 1
    fi
done

if [ -e "$RECONSTRUCTION_OUTPUT_DIR" ]; then
    printf 'ERROR: reconstruction directory already exists; choose a new path: %s\n' \
        "$RECONSTRUCTION_OUTPUT_DIR" >&2
    exit 1
fi
mkdir -p "$(dirname "$RECONSTRUCTION_OUTPUT_DIR")" || exit "$?"
mkdir "$RECONSTRUCTION_OUTPUT_DIR" || exit "$?"
```

Run the confirmed example reconstruction:

```bash
if "$BART" pics \
    --fista \
    --wavelet dau2 \
    -R W:7:0:0.01 \
    -i 100 \
    -s 0.95 \
    -n \
    -w 1 \
    -p "$PREPARATION_DIR/mask3d" \
    "$PREPARATION_DIR/kspace_undersampled" \
    "$PREPARATION_DIR/sensitivities" \
    "$RECONSTRUCTION_OUTPUT_DIR/reconstruction" \
    > "$RECONSTRUCTION_OUTPUT_DIR/reconstruction.log" 2>&1; then
    printf 'SUCCESS: BART CS reconstruction (exit code 0).\n'
else
    status=$?
    cat "$RECONSTRUCTION_OUTPUT_DIR/reconstruction.log" >&2
    printf 'ERROR: BART CS reconstruction (exit code %s).\n' "$status" >&2
    exit "$status"
fi
```

`--fista` selects FISTA, and `--wavelet dau2` selects the `dau2` wavelet.
`W:7:0:0.01` requests L1-wavelet regularization over axes 0–2, with no
additional threshold grouping through argument `0`, and weight `0.01`.
`-i 100` sets a maximum of 100 iterations; it does not guarantee convergence.
`-s 0.95` sets the iteration step selected for this example. `-n` disables
random wavelet shifting in `pics`, `-w 1` fixes the data scaling factor at
one, and `-p` supplies the preserved explicit `mask3d`. These values are
approved for this example only; the regularization weight is not an evaluation
tolerance and is not presented as optimal.

Expected output: `reconstruction.hdr` and `reconstruction.cfl` in the new
reconstruction directory. The BART exit code records the operational result
of the command.

## 9. Check the Reconstruction Output

Validate the new reconstruction pair with the existing 3D checker:

```bash
if "$PYTHON" "$REPO/scripts/check_preparation_pair_3d.py" \
    "$RECONSTRUCTION_OUTPUT_DIR" reconstruction \
    > "$RECONSTRUCTION_OUTPUT_DIR/reconstruction-check.txt" 2>&1; then
    status=0
else
    status=$?
fi

printf 'Reconstruction-check exit code: %s\n' "$status" \
    >> "$RECONSTRUCTION_OUTPUT_DIR/reconstruction-check.txt"
cat "$RECONSTRUCTION_OUTPUT_DIR/reconstruction-check.txt"
if [ "$status" -ne 0 ]; then
    printf 'ERROR: reconstruction check failed; preserve the record: %s\n' \
        "$RECONSTRUCTION_OUTPUT_DIR/reconstruction-check.txt" >&2
    exit "$status"
fi
```

The checker verifies that `reconstruction.hdr` and `reconstruction.cfl` exist,
declare spatial dimensions `64 × 64 × 64`, preserve singleton trailing axes,
have a binary size compatible with BART `complex64`, and contain finite values.
This establishes the expected output structure and readability only. It does
not measure agreement with the synthetic reference, demonstrate convergence
of `pics`, or introduce a reconstruction-quality criterion.

## 10. Generate the Visual Reference Comparison

Run this block in the same Bash session using the `PYTHON` configured in
Section 1. It reads the preserved reference and reconstruction using
the existing `read_bart_3d` support function and generates one non-interactive
2 × 3 figure. It does not modify the source files or complex arrays.

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
        (1, reconstruction, "CS reconstruction"),
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
print(f"Reference shape: {reference.shape}")
print(f"Reconstruction shape: {reconstruction.shape}")
print(f"Python: {platform.python_version()}")
print(f"NumPy: {np.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
print("Array axes: axis 0 readout, axes 1 and 2 phase; no anatomical orientation assigned")
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
print(f"Reference volume maximum magnitude: {reference_max:.9e}")
print(f"Reconstruction volume maximum magnitude: {reconstruction_max:.9e}")
print(
    "Reconstruction volume exceeds display limit: "
    f"{reconstruction_max > reference_max}"
)

for title, cut in planes:
    reference_slice_max = float(cut(reference_magnitude).max())
    reconstruction_slice_max = float(cut(reconstruction_magnitude).max())
    print(
        f"{title}: reference slice maximum={reference_slice_max:.9e}; "
        f"reconstruction slice maximum={reconstruction_slice_max:.9e}; "
        "reconstruction slice exceeds display limit="
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

The figure is saved at:

```text
$RECONSTRUCTION_OUTPUT_DIR/figures-visual/reference-reconstruction-orthogonal.png
```

The upper row contains reference slices and the lower row contains CS
reconstruction slices. The shared scale is zero through the full-volume
reference maximum. Values above that limit are visually saturated; this
observation does not by itself establish their cause.

The log records the input routes and shapes, effective Python, NumPy, and
Matplotlib versions, planes and presentation operations, shared limits,
full-volume maxima, per-slice maxima, exceedance indicators, figure route,
and generation exit code. The figure shows three magnitude slices only: it
does not inspect every voxel, check phase, or demonstrate `pics` convergence.
Generation remains separate from any visual observations Ricardo may record
after inspecting the saved figure. No visual pass/fail classification is
introduced.

## 11. Perform the Quantitative Reference Comparison

Run this block in the same Bash session using the `PYTHON` configured in
Section 1. It reads the preserved reference and reconstruction with the
existing 3D reader and imports only the required `relative_error` function.
It does not invoke the main program in `check_fourier_numpy.py` or generate
another reconstruction.

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
print("Reference read: valid")
print("Reconstruction read: valid")
reference_norm = float(np.linalg.norm(reference.ravel()))
if not np.isfinite(reference_norm) or reference_norm == 0:
    raise ValueError("reference L2 norm must be finite and nonzero")

error = relative_error(reference, reconstruction)
if not np.isfinite(error):
    raise ValueError("relative L2 error must be finite")

print(f"Reference input: {reference_base}.hdr/.cfl")
print(f"Reconstruction input: {reconstruction_base}.hdr/.cfl")
print(f"Reference shape: {reference.shape}")
print(f"Reconstruction shape: {reconstruction.shape}")
print("Stored data: complex64 in BART .cfl files")
print("Calculation arrays: complex128 returned by read_bart_3d")
print("Volume included: all complex values in the complete 64 x 64 x 64 volume")
print("Metric: ||reconstruction - reference||_2 / ||reference||_2")
print("Preprocessing: none; no magnitude conversion, visual slices, transpose, crop, mask, alignment, scaling, or phase correction")
print("Denominator: checked for finiteness and nonzero norm before division")
print("Result finiteness: checked after relative_error calculation")
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

The calculation uses the complete complex `64 × 64 × 64` volume, with no
preprocessing. `read_bart_3d` returns complex128 arrays after validating the
stored complex64 BART pairs. `relative_error` flattens those arrays for the
norm calculation, so all volume values participate without a dimension
specific adaptation. An exit code of `0` means that the calculation completed
operationally; it does not establish reconstruction-quality acceptance or
`pics` convergence. No historical result is copied or anticipated.

## 12. Record Commands, Configuration, Results, and Limitations

When Ricardo executes the procedure, preserve the two preparation directories,
the reconstruction directory, their local logs and figures, and the execution
notes outside the repository. Link the existing records from the execution
record instead of copying their contents.

- Each preparation must retain its six BART pairs:
  `reference.hdr/.cfl`, `kspace_full.hdr/.cfl`, `mask2d.hdr/.cfl`,
  `mask3d.hdr/.cfl`, `kspace_undersampled.hdr/.cfl`, and
  `sensitivities.hdr/.cfl`.
- Each preparation must retain its generation and checking records:
  `phantom.log`, `reference-check.txt`, `kspace-full-fft.log`,
  `kspace-full-check.txt`, `mask2d-poisson.log`, `mask3d-repmat.log`,
  `mask-check.txt`, `kspace-undersampled-fmac.log`,
  `kspace-undersampled-check.txt`, `sensitivities-ones.log`, and
  `sensitivities-check.txt`.
- Keep one `preparation-record.txt` in each preparation directory, using the
  format below with values from that generation.
- Keep `regeneration-comparison.txt` in the second preparation directory. It
  must preserve the original `MATCH`, `DIFFERENT`, and `ERROR` results, the
  `diff -u` output for reviewed headers, and the code recorded for each
  comparison and diff.
- In `RECONSTRUCTION_OUTPUT_DIR`, retain `reconstruction.hdr/.cfl`,
  `reconstruction.log`, and `reconstruction-check.txt`.
- Also retain `figures-visual/reference-reconstruction-orthogonal.png`,
  `visual-comparison.log`, and `quantitative-comparison.txt`.
- Keep these data, logs, figures, and execution notes in their local
  directories, outside the repository. A cumulative `run-record.md` remains
  optional; if it exists, it may be preserved and used without requiring
  another record.

The original regeneration results remain the authoritative comparison results:
human review of expected directory-path differences in headers is recorded as
review and does not change an original `DIFFERENT` result into `MATCH`.
The static figure-generation result remains separate from Ricardo's human
observations after inspecting the figure. Record the observed sampling
fraction and effective acceleration separately from the nominal product
`2 × 2 = 4`. Record the complex relative L2 error with its calculation
conditions, without a tolerance or a reconstruction-quality pass/fail
classification. Exit codes describe the operational result of each command
according to that command's documented meaning; they do not establish
scientific acceptance.

Use this brief reusable format. Replace every placeholder with actual
execution information; do not copy dates, metrics, or observations from the
earlier 2D or 3D cases. Mark a stage that was not performed as
`NOT_EXECUTED`, without assigning it exit code `0` or automatically calling it
failed.

```markdown
# Manual Cartesian 3D Compressed-Sensing Run Record

- Date/time and time zone: <actual value>
- Operator: <name>
- Repository revision and local changes, if known: <actual details>
- BART executable/version, Python executable/version, NumPy/Matplotlib versions, and platform: <actual values>
- First preparation: <absolute path; link to preparation-record.txt>
- Second preparation: <absolute path; link to preparation-record.txt>
- Reconstruction output: <absolute path>
- Preparation used as reconstruction input: <actual preparation path used>
- Effective settings: <actual phantom, dimensions, channel, mask, FFT, and pics settings>

| Step | Exact command/invocation | Exit code | Observation | Log/evidence link |
|---|---|---:|---|---|
| <step name> | <actual invocation or NOT_EXECUTED> | <actual code or NOT_EXECUTED> | <result> | [Evidence](<relative-path>) |

- Produced files: <actual pairs, logs, figure, and records>
- Regeneration headers: <original results, diff review, and human notes>
- Sampling fraction/effective acceleration: <observed values; nominal product kept separate>
- Visual figure generation: <actual result and figure link>
- Visual observations by Ricardo: <human observations after inspection / not recorded>
- Quantitative comparison: <actual error, conditions, and record link / NOT_EXECUTED>
- Failures, corrections, unresolved issues, and limitations: <actual notes>
```

For each executed operation, record the actual command, exit code, and
evidence. If an unexecuted stage is listed, retain its stage name and mark its
execution fields as `NOT_EXECUTED`; do not invent an exit code or generated
evidence.

## Appendix A. Optional Interactive Slice Inspection

For inspection of a single existing reconstruction without copying this
comparison block, see the separate
[interactive slice viewer](automated-cartesian-workflow.md#optional-interactive-slice-viewer).
The historical two-panel reference comparison below remains unchanged.

This optional inspection reads an existing Cartesian 3D CS reference and
reconstruction and opens an interactive Matplotlib window for manual review.
It requires an interactive Matplotlib backend in the `PYTHON` environment
selected in Section 1. This block does not select or change the global backend
configuration. If the selected backend is non-interactive or cannot open a
window, it reports an error instead of claiming that inspection succeeded.
The static figure in Section 10 uses `Agg` in a separate Python process; this
optional viewer does not change that non-interactive configuration.

Run this block in the same Bash session after configuring the CS paths in
Section 1:

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
            f"CS reconstruction: plane 0-1, axis 2 = {selected_index}"
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
    figure.suptitle("Interactive 3D CS plane 0-1 inspection")
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

This is optional manual inspection of existing CS reconstruction files. It
complements the saved static figure and the full-volume complex comparison,
does not create new data, saved figures, metrics, or records, and does not
replace the quantitative comparison. It is not a dependency of future
non-interactive automation and does not introduce a GUI dependency there.
Successful viewer termination only indicates that the window closed normally;
it does not establish that Ricardo inspected every slice or accepted the
reconstruction quality.
