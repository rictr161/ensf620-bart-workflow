# Automated Cartesian BART Workflow

This guide describes the current terminal interface in
[`src/bart_workflow.py`](../../src/bart_workflow.py). One invocation coordinates
one reconstruction: it inspects the input, obtains or reads sampling and
sensitivity information when required, invokes BART, checks the reconstruction
output, and records the run. The workflow is non-interactive and does not
require a reference image.

The examples use the preserved synthetic preparations. They document how to
invoke the current implementation; they are not new execution evidence, and
the commands in this guide have not been run as part of preparing it.

## Supported routes and input limits

| Route | Current behavior |
|---|---|
| Fully sampled Cartesian 2D | Single-channel input; inverse BART FFT on spatial axes 0 and 1. |
| Fully sampled Cartesian 3D | Single-channel input; inverse BART FFT on spatial axes 0, 1, and 2. |
| Cartesian 3D CS with supplied inputs | Uses a supplied spatial mask and supplied sensitivity maps, then runs `pics`. |
| Cartesian 3D CS with generated inputs | Estimates a mask with `pattern`, estimates sensitivities with `ecalib`, and runs `pics` using one ESPIRiT map set. |

The FFT routes accept the declared number of leading spatial axes and require
all later axes to be singleton; they do not hard-code spatial sizes. They are
single-channel routes. For CS, axes 0–2 are spatial, axis 3 is the channel
dimension, axis 4 is the map-set dimension, and later axes must be singleton.
The implementation allows a positive channel count without fixing it to a
particular number, but supports exactly one map set. The spatial dimensions
must also be compatible with the selected mask and any `ecalib` settings.

`read_bart_array` can read a BART header/binary pair with positive dimensions;
that generic reader does not establish support for arbitrary acquisition
layouts, trajectories, series, or scanner data. Route-specific validation
still applies. Cartesian 2D CS, radial reconstruction, and 4D reconstruction
are not supported routes.

## Start from a clean terminal

The following paths match the recorded local macOS environment and preserved
synthetic preparations. Change `REPO` if your checkout is elsewhere, and use a
new `RUNS_ROOT` if you have already used the destinations below. The Python
environment and BART executable are referenced directly; this guide does not
include installation or update steps. The environment record reports Python
3.13.17 and BART v1.0.00; verify that the configured executables are available
in your current environment.

```bash
REPO="$HOME/projects/ensf620-bart-workflow"
PYTHON="$HOME/bart-learning/.venv/bin/python"
BART="$HOME/software/bart-1.0.00/bart"
PREPARATIONS="$HOME/bart-learning/bart-workflow-preparations"
RUNS_ROOT="$HOME/bart-learning/bart-workflow-reconstructions/automated-cartesian-tutorial-01"

KSPACE_2D="$PREPARATIONS/generation-01/kspace"
KSPACE_3D="$PREPARATIONS/generation-3d-01/kspace"
KSPACE_3D_CS="$PREPARATIONS/generation-3d-cs-01/kspace_undersampled"
MASK_3D_CS="$PREPARATIONS/generation-3d-cs-01/mask3d"
SENSITIVITIES_3D_CS="$PREPARATIONS/generation-3d-cs-01/sensitivities"
KSPACE_3D_CS_MULTICHANNEL="$PREPARATIONS/generation-3d-ecalib-01/kspace_undersampled"

OUT_2D="$RUNS_ROOT/cartesian-2d"
OUT_3D="$RUNS_ROOT/cartesian-3d"
OUT_3D_CS="$RUNS_ROOT/cartesian-3d-cs-original"
OUT_3D_CS_MULTICHANNEL="$RUNS_ROOT/cartesian-3d-cs-multichannel"
```

`--kspace`, `--sampling-mask`, and `--sensitivities` take BART base paths
without `.hdr` or `.cfl`; each input consists of the matching pair. Confirm
that the intended pairs are available and that the configured Python and BART
paths are correct before starting. The workflow creates each output directory,
including missing parent directories. The final directory passed to
`--output-directory` must not already exist; do not create it in advance.

## Run the four routes

Each example invokes the workflow once and captures its process status in the
same terminal session. A nonzero result is a failure to investigate, not a
reason to silently retry with different settings. The workflow stops dependent
stages after a mandatory failure.

### 1. Cartesian 2D, fully sampled

```bash
if "$PYTHON" "$REPO/src/bart_workflow.py" \
  --kspace "$KSPACE_2D" \
  --output-directory "$OUT_2D" \
  --spatial-dimensionality 2 \
  --fft-normalization unitary \
  --bart-executable "$BART"
then
  cartesian_2d_exit_code=0
else
  cartesian_2d_exit_code=$?
fi
printf 'Cartesian 2D workflow exit code: %s\n' "$cartesian_2d_exit_code"
```

### 2. Cartesian 3D, fully sampled

```bash
if "$PYTHON" "$REPO/src/bart_workflow.py" \
  --kspace "$KSPACE_3D" \
  --output-directory "$OUT_3D" \
  --spatial-dimensionality 3 \
  --fft-normalization unitary \
  --bart-executable "$BART"
then
  cartesian_3d_exit_code=0
else
  cartesian_3d_exit_code=$?
fi
printf 'Cartesian 3D workflow exit code: %s\n' "$cartesian_3d_exit_code"
```

### 3. Cartesian 3D CS, supplied mask and sensitivities

This example uses the mask and sensitivity maps from the same preserved
preparation as the k-space. The `manual-cartesian-3d-cs` profile supplies the
reviewed synthetic `pics` settings.

```bash
if "$PYTHON" "$REPO/src/bart_workflow.py" \
  --kspace "$KSPACE_3D_CS" \
  --output-directory "$OUT_3D_CS" \
  --spatial-dimensionality 3 \
  --compressed-sensing \
  --sampling-source provided \
  --sampling-mask "$MASK_3D_CS" \
  --sensitivity-source provided \
  --sensitivities "$SENSITIVITIES_3D_CS" \
  --reconstruction-profile manual-cartesian-3d-cs \
  --bart-executable "$BART"
then
  cartesian_3d_cs_exit_code=0
else
  cartesian_3d_cs_exit_code=$?
fi
printf 'Cartesian 3D CS workflow exit code: %s\n' "$cartesian_3d_cs_exit_code"
```

### 4. Cartesian 3D multichannel CS, generated mask and sensitivities

This route starts from the prepared multichannel k-space. The workflow obtains
the sampling pattern and sensitivity maps within the invocation. It uses one
ESPIRiT map set; the number of coil channels is a separate dimension.

```bash
if "$PYTHON" "$REPO/src/bart_workflow.py" \
  --kspace "$KSPACE_3D_CS_MULTICHANNEL" \
  --output-directory "$OUT_3D_CS_MULTICHANNEL" \
  --spatial-dimensionality 3 \
  --compressed-sensing \
  --sampling-source bart-pattern \
  --sensitivity-source ecalib \
  --ecalib-calibration-region 64:16:16 \
  --ecalib-kernel-size 6:6:6 \
  --ecalib-threshold 0.001 \
  --ecalib-crop 0.8 \
  --ecalib-map-sets 1 \
  --reconstruction-profile manual-cartesian-3d-cs \
  --bart-executable "$BART"
then
  cartesian_3d_cs_multichannel_exit_code=0
else
  cartesian_3d_cs_multichannel_exit_code=$?
fi
printf 'Cartesian 3D multichannel CS workflow exit code: %s\n' \
  "$cartesian_3d_cs_multichannel_exit_code"
```

Reconstruction does not need a reference image. Reference comparisons are
separate evaluations and are not an option in this CLI.

## CLI arguments and settings

The required `--kspace`, `--output-directory`, and
`--spatial-dimensionality` arguments appear in the examples. The table below
summarizes the other inputs and settings accepted by the current parser.

| Argument | Purpose and when used | Requirement or source of value |
|---|---|---|
| `--compressed-sensing` | Selects the Cartesian 3D CS route instead of the FFT route. | Optional switch; off unless specified. |
| `--fft-normalization` | Selects FFT normalization for the fully sampled route. | Defaults to `unitary`; this implementation accepts only `unitary`. |
| `--sampling-source {provided,bart-pattern}` | Chooses a supplied mask or requests estimation with BART `pattern`. | CS only; defaults to `provided`. |
| `--sampling-mask PATH` | Supplies the spatial sampling mask. | Required with `--sampling-source provided`; do not pass with `bart-pattern`. |
| `--sensitivity-source {provided,ecalib}` | Chooses supplied maps or calibration with BART `ecalib`. | CS only; defaults to `provided`. |
| `--sensitivities PATH` | Supplies sensitivity maps. | Required with `--sensitivity-source provided`; do not pass with `ecalib`. |
| `--ecalib-calibration-region X:Y:Z` | Sets the centered calibration region. | Required when `--sensitivity-source ecalib` is selected. |
| `--ecalib-kernel-size X:Y:Z` | Sets the `ecalib` kernel. | Defaults to `6:6:6`; must fit both the k-space and calibration region. |
| `--ecalib-threshold FLOAT` | Sets the `ecalib` threshold. | Defaults to `0.001`; must satisfy `0 <= threshold < 1`. |
| `--ecalib-crop FLOAT` | Sets the `ecalib` crop value. | Defaults to `0.8`; must be between 0 and 1, inclusive. |
| `--ecalib-map-sets INT` | Selects the ESPIRiT map-set count. | Defaults to `1`; the implementation rejects any value other than `1`. |
| `--reconstruction-profile manual-cartesian-3d-cs` | Supplies the reviewed example's `pics` settings. | Optional; without a profile, provide all seven `--pics-*` values below. |
| `--pics-use-fista` / `--no-pics-use-fista` | Enables or disables FISTA. | Profile value: enabled. Explicit values override the profile. |
| `--pics-wavelet STRING` | Selects the `pics` wavelet. | Profile value: `dau2`; otherwise required for CS. |
| `--pics-regularization-weight FLOAT` | Sets the wavelet regularization weight. | Profile value: `0.01`; otherwise required for CS. |
| `--pics-iterations INT` | Sets the iteration count. | Profile value: `100`; otherwise required for CS. |
| `--pics-step FLOAT` | Sets the `pics` step. | Profile value: `0.95`; otherwise required for CS. |
| `--pics-disable-random-shift` / `--no-pics-disable-random-shift` | Selects whether to disable random shifting. | Profile value: disabled random shift; explicit values override the profile. |
| `--pics-data-scaling FLOAT` | Sets the data scaling value. | Profile value: `1.0`; otherwise required for CS. |
| `--bart-executable PATH` | Selects the BART executable. | Defaults to `bart`; the examples use the recorded local path. |
| `--save-figures` | Requests a non-interactive reconstruction figure. | Optional switch; no figure is requested by default. |

The `manual-cartesian-3d-cs` profile is a reviewed synthetic example, not a
universal scientific configuration. Explicit `--pics-*` arguments override
the corresponding profile values; for example, adding
`--pics-iterations 120` changes only the iteration setting. When no profile is
selected, the seven `pics` settings must all be supplied, and their values
must pass the workflow's validation.

The number of coil channels is not the number of ESPIRiT map sets. The current
CS route supports multiple channels but exactly one map set. In particular,
`--ecalib-map-sets 1` selects one set; it does not reduce a multichannel input
to one channel.

## Sampling and sensitivity inputs

### Sampling mask

- With `--sampling-source provided`, the workflow reads the supplied mask,
  checks its spatial shape and binary values, requires both acquired and
  omitted positions, and checks that omitted k-space positions are zero.
- With `--sampling-source bart-pattern`, the workflow runs
  `bart pattern <kspace> <output-directory>/sampling_mask`, then validates
  the generated mask before dependent stages use it. Do not also supply
  `--sampling-mask`.

The `pattern` route estimates support from nonzero k-space. A genuinely
acquired location whose values are zero across channels can therefore be
interpreted as omitted. A known acceleration factor alone does not identify
which positions were acquired. The CLI has no acceleration-factor or
trajectory argument, and this route does not resample or modify the input
k-space. For `ecalib`, the configured centered calibration region must be
fully sampled by the effective mask.

### Sensitivity maps

With `--sensitivity-source provided`, pass the matching BART base path using
`--sensitivities`. With `--sensitivity-source ecalib`, the workflow runs BART
`ecalib` on the same k-space and uses the resulting maps for `pics`; do not
also pass `--sensitivities`. The ecalib region is required, and its dimensions
and kernel must be compatible with the input. The region and kernel are
positive triplets; each kernel dimension must fit the region and the input,
and a kernel dimension of one is unsupported on a spatial axis larger than
one. The workflow checks sensitivity spatial dimensions, channel count, the
single-map-set constraint, and that maps are not completely zero. The
implementation uses one ESPIRiT map set.

## Outputs and review

Every successful run writes a reconstruction pair and operational records
under its new output directory. CS routes additionally produce the artifacts
shown below when that source is selected.

| Route | Outputs and operation logs |
|---|---|
| Cartesian 2D or 3D FFT | `reconstruction.hdr` and `reconstruction.cfl`; `bart-version.log`, `reconstruction.log`, and `stage-records.json`. |
| CS with supplied mask and maps | Reconstruction pair and the common logs/records; supplied mask and maps remain at their input locations and are not copied into the run directory. |
| CS with `bart-pattern` and `ecalib` | Reconstruction pair; `sampling_mask.hdr`/`sampling_mask.cfl`, `sensitivities.hdr`/`sensitivities.cfl`, `eigenvalues.hdr`/`eigenvalues.cfl`; `bart-version.log`, `sampling-pattern.log`, `ecalib.log`, `reconstruction.log`, and `stage-records.json`. |

Run records and logs include:

- `stage-records.json`, with the requested configuration and an ordered stage
  list including status, exit code, and applicable effective settings,
  commands, paths, or errors.
- `bart-version.log`, containing the configured BART `version -V` response.
  The version query and log are mandatory.
- `reconstruction.log` for the BART reconstruction invocation.
- `sampling-pattern.log` when the workflow runs `pattern`.
- `ecalib.log` when the workflow runs `ecalib`.

Inspect the printed global outcome and exit code first, then read the stage
records and relevant logs. The CLI prints `SUCCESS` when mandatory operations,
the structural output check, and required records succeed. On failure it
prints an `ERROR` message and points to `stage-records.json` when one could be
saved; a failure before the output directory is created, or a failure to save
records, may leave no diagnostic record.

The workflow refuses an existing output directory; it does not overwrite or
reuse it. Mandatory failures stop dependent stages, return nonzero, and
preserve files already produced. There is no automatic retry or fallback
between supplied and generated sampling or sensitivity sources. Optional
figure generation is requested with `--save-figures` and writes
`figures/reconstruction.png`; Matplotlib is needed only for this option. A
figure-only failure is reported separately and does not invalidate a valid
reconstruction.

The workflow's output check is structural (including supported shape and
finite-value checks), not an image-quality acceptance test. A successful
process exit does not by itself establish scientific quality or equivalence
to a reference. Generated sensitivity maps are retained in the run directory
for later file-level review. The workflow does not provide a sensitivity-map
visualization feature.

## Acquired data and ARC

The examples in this guide use synthetic BART preparations. Before applying a
route to an acquired volume, establish its dimensions and axis meanings,
sampling information, channel layout, sensitivity-map requirements, and
effective reconstruction parameters. Do not infer a mask or trajectory from
an acceleration factor alone.

The `manual-cartesian-3d-cs` profile reflects the reviewed synthetic example;
it is not a reproduction of a colleague's acquisition protocol. That protocol
must be checked separately against the input and the settings actually
supported and used here.

For another machine, configure paths to the Python environment, BART
executable, inputs, and a new output directory for that environment. ARC
execution and laboratory batch processing have not been verified and remain
outside this guide. The examples describe one non-interactive reconstruction
per invocation.

## Related documentation

- [Workflow source notes](../../src/README.md)
- [Python automation behavior](../python-automation-behavior.md)
- [Synthetic 2D procedure](../../tests/synthetic_2d/README.md)
- [Automation implementation and evidence task](../../tasks/tasks-bart-reconstruction-workflow.md)
