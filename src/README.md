# Workflow Source

The first implementation block is in `bart_workflow.py`. It exposes the
reusable `run_reconstruction` function and a terminal entry point for the
reviewed fully sampled Cartesian 2D and 3D inverse-FFT routes and Cartesian 3D
compressed sensing with either supplied sensitivity maps or explicitly
requested `ecalib` calibration.

The implementation accepts prepared BART `.hdr`/`.cfl` k-space, validates
declared dimensions and companion inputs, invokes BART with argument lists, and
records stage results and effective settings in a separate run directory. The
`manual-cartesian-3d-cs` profile is an explicit example profile from the
reviewed tutorial; it is not a universal default.

The 3D CS route checks channel axis 3, one map set on axis 4, and singleton
later axes without hard-coding spatial dimensions or channel count. Its
sampling source is explicitly selected as a provided spatial mask or a BART
`pattern` estimate; the effective mask applies across channels and the
configured calibration region must also be fully sampled. FFT routes remain
single-channel. Cartesian 2D CS is outside the December 1, 2026 delivery scope
and may be considered as a future extension without an implementation
commitment. Multiple ESPIRiT map sets are a separate unsupported capability.
No general reference-comparison CLI is implemented in this source block.
Ricardo separately evaluated the three existing synthetic automated outputs
using the tutorial blocks; those results are recorded under Task 7.11 and do
not make reference evaluation an integrated reconstruction step.
Optional reconstruction figures are implemented and have owner-reported local
executions for fully sampled Cartesian 2D and 3D; these case-specific results
are summarized below. Radial reconstruction remains out of scope. Ricardo's manual multichannel `ecalib` execution and a matching
local automated run are documented below.
This case-specific evidence does not claim compatibility with unreviewed BART
array layouts.

The separate interactive [`view_bart_slices.py`](view_bart_slices.py) utility
opens an existing scalar reconstruction locally; see the
[viewer instructions](../docs/tutorials/automated-cartesian-workflow.md#optional-interactive-slice-viewer).
It is not part of the non-interactive reconstruction workflow.

## Terminal examples

Run the module from the repository root with a configured BART executable and
prepared input paths:

```text
python src/bart_workflow.py \
  --kspace /path/to/kspace \
  --output-directory /path/to/run-2d \
  --spatial-dimensionality 2 \
  --bart-executable /path/to/bart
```

## Runtime environment record

After successful k-space inspection and before `pattern`, `ecalib`, `fft`, or
`pics`, the workflow queries the configured BART executable with `version -V`.
The `runtime-environment` stage records the Python executable and version,
imported NumPy version, operating system/release/version and architecture,
configured BART executable, query command, exit code, and response. The complete
captured response is written to `bart-version.log`; the log is mandatory. A
nonzero query result or log-write failure stops dependent processing and is
recorded separately. The configured executable spelling is preserved, so `bart`
remains distinct from `./bart` in the invocation record.

## Optional reconstruction figures

Pass `--save-figures` to save a non-interactive PNG at
`figures/reconstruction.png` within the new run directory. Matplotlib is needed
only when this option is requested. The workflow uses `FigureCanvasAgg` and
does not open a window or change the caller's global Matplotlib backend.

For 2D, the figure shows the full reconstruction magnitude. For 3D, it shows
the three central orthogonal planes, with indices computed from the actual
spatial dimensions. Each plane is transposed for display and uses grayscale,
lower origin, equal aspect, and no interpolation; axes are labeled as array
indices without anatomical orientation. The 3D planes share magnitude limits
from zero to the volume maximum. An all-zero volume uses an explicit display
maximum of `1.0`. The figure stage records the effective limits, slice indices,
presentation settings, and confirmed output path in `stage-records.json`.
It records the Matplotlib version only when figures are requested and Matplotlib
is imported.
Figure generation follows the mandatory reconstruction output check. If it
fails, the stage and warning are recorded separately and a valid reconstruction
remains successful under FR-32.

Ricardo reported successful local `--save-figures` runs for Cartesian 2D and
3D FFT, with global exit code `0`. In `automated-2d-figures-01` and
`automated-3d-figures-01`, respectively, `stage-records.json` records
`reconstruction-figure` as `success` with exit code `0` and the output path
`figures/reconstruction.png`. The 2D figure shows the complete 64 × 64 image;
the 3D figure shows the three central planes of the 64 × 64 × 64 volume at
indices `[32, 32, 32]`. The records include magnitude limits and presentation
settings. Ricardo confirmed that both visualizations display correctly. This
is owner-reported evidence for normal figure generation in these two cases; it
does not establish all failure paths, comparison against a reference, or
completion of the automation block.

Example invocation:

```text
python src/bart_workflow.py \
  --kspace /path/to/kspace \
  --output-directory /path/to/run-3d-with-figure \
  --spatial-dimensionality 3 \
  --bart-executable /path/to/bart \
  --save-figures
```

The reviewed CS example uses the explicit profile and supplied preparation
pairs:

```text
python src/bart_workflow.py \
  --kspace /path/to/kspace_undersampled \
  --output-directory /path/to/run-3d-cs \
  --spatial-dimensionality 3 \
  --compressed-sensing \
  --sampling-mask /path/to/mask3d \
  --sensitivities /path/to/sensitivities \
  --reconstruction-profile manual-cartesian-3d-cs \
  --bart-executable /path/to/bart
```

## Cartesian 3D multichannel CS with `ecalib`

Sensitivity origin is selected explicitly. The default source is `provided`,
so existing invocations using `--sensitivities` continue to work. Use
`--sensitivity-source ecalib` to estimate maps within the same workflow. The
calibration region is required explicitly. The defaults for the other
calibration controls are kernel `6:6:6`, threshold `0.001`, crop `0.8`, and
one ESPIRiT set. One set is the supported case selection; the kernel,
threshold, and crop are BART starting values and may need adjustment for a
different acquisition. Requesting more than one map set is rejected. For this
route, each kernel dimension must fit the calibration region and k-space. A
kernel dimension of one is rejected when its spatial k-space axis is larger
than one, because this route requires sensitivity maps with the full spatial
shape of k-space; this is not a general BART restriction. The threshold must
satisfy `0 <= threshold < 1`.

The CS sampling source is also explicit:

- `--sampling-source provided` is the default and requires `--sampling-mask`.
  Existing calls that provide a mask remain compatible.
- `--sampling-source bart-pattern` estimates a mask with
  `bart pattern <kspace> <run-directory>/sampling_mask`. Do not also pass
  `--sampling-mask`. On successful estimation and log writing, the workflow
  validates the generated pair; dependent stages use that same effective mask
  for the `ecalib` center check and `pics -p` only after checks pass. A
  log-write failure blocks dependent stages. An unavailable or invalid
  provided mask fails; it never triggers estimation as a fallback.
- Cartesian FFT routes reject `bart-pattern`.

BART `pattern` estimates the support of nonzero k-space. Omitted positions must
be exact zeros; a truly acquired position whose values are zero in all channels
can be interpreted as omitted. The known acceleration factor does not identify
the sampled positions and cannot replace a mask. The source selection does not
modify or resample the input k-space. Reconstruction needs no reference image
or ground-truth metric.

Example using `bart-pattern` and the reviewed `ecalib`/`pics` settings:

```text
python src/bart_workflow.py \
  --kspace /path/to/kspace_undersampled \
  --output-directory /path/to/run-3d-cs-pattern \
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
  --bart-executable bart
```

For `bart-pattern`, the run requires `sampling-pattern.log` and preserves any
generated `sampling_mask` `.hdr`/`.cfl` pair. A log-write failure stops
dependent stages. The mask is available to dependent stages only after
validation. Stage records keep the requested source and mask argument separate
from the effective mask path, and record the k-space, command, actual BART
result, log result, and mask-check result.

Ricardo reports a separate manual `bart pattern` check with BART v1.0.00 on
the `generation-3d-ecalib-01/kspace_undersampled` input. The output header
declared `64 64 64` with later axes singleton. `cmp` between the generated mask
binary and the known `generation-3d-cs-01/mask3d` binary returned `0`. The
`bart pattern` exit code was not reported. This manual check does not establish
the automated route by itself; Ricardo has since reported the automated
`--sampling-source bart-pattern` execution below.

For `automated-3d-pattern-ecalib-01`, Ricardo reported using that synthetic
k-space with `bart-pattern`, no supplied mask, `ecalib`, no supplied
sensitivities, the `64:16:16` calibration region, kernel `6:6:6`, threshold
`0.001`, crop `0.8`, one map set, and the `manual-cartesian-3d-cs` profile.
Optional figures were requested. The BART `version -V`, `pattern`, `ecalib`,
and `pics` commands each recorded exit code `0`; all 11 stage records report
`success` with code `0`. The generated mask passed its checks and was used by
`pics`; `pics` also used the sensitivities generated by `ecalib` in that run
directory. The effective profile settings, software/environment versions,
successful reconstruction structural check, and figure record are present in
the reported records. The figure stage records Matplotlib `3.11.2` and
`figures/reconstruction.png` for the `64 × 64 × 64` volume at central indices
`[32, 32, 32]`. Log-write error fields were reported as `null`. The global CLI
exit code was not supplied, and Ricardo did not report a new human visual
inspection of this figure.

Ricardo also reported `cmp` exit code `0` for
`reconstruction.cfl` in `automated-3d-ecalib-01` versus
`automated-3d-pattern-ecalib-01`. This establishes byte-for-byte identity
between those two automated outputs for this case only; it is not a direct
manual or synthetic-reference comparison.

The following complete invocation uses the owner-reported synthetic inputs and
requires no session variables. Run it from the repository root, ensure `bart`
is available on `PATH` (or replace `bart` with its executable path), and choose
a destination that does not already exist:

```text
python src/bart_workflow.py \
  --kspace /Users/ricardoaguilar/bart-learning/bart-workflow-preparations/generation-3d-ecalib-01/kspace_undersampled \
  --output-directory /Users/ricardoaguilar/bart-learning/bart-workflow-reconstructions/automated-3d-ecalib-01 \
  --spatial-dimensionality 3 \
  --compressed-sensing \
  --sampling-mask /Users/ricardoaguilar/bart-learning/bart-workflow-preparations/generation-3d-cs-01/mask3d \
  --sensitivity-source ecalib \
  --ecalib-calibration-region 64:16:16 \
  --ecalib-kernel-size 6:6:6 \
  --ecalib-threshold 0.001 \
  --ecalib-crop 0.8 \
  --ecalib-map-sets 1 \
  --reconstruction-profile manual-cartesian-3d-cs \
  --bart-executable bart
```

The invocation requires k-space, a new output directory, declared
dimensionality, explicit CS selection, the saved sampling mask, a sensitivity
source, calibration region for `ecalib`, the reconstruction profile (or all
CS parameters explicitly), and an available BART executable. Kernel,
threshold, crop, and map-set count may be omitted on this route and use the
documented defaults. The profile supplies only the reviewed `pics` settings.

The run directory retains `bart-version.log`, `ecalib.log`, the generated
`sensitivities` and `eigenvalues` BART pairs, `reconstruction.log`, the
`reconstruction` pair, and `stage-records.json`. The records include actual
commands and BART exit codes, effective calibration and reconstruction
settings, file identities, and separate check results. Failed calibration or
mandatory checks stop dependent steps; produced files are preserved.

Ricardo reported the corresponding manual BART v1.0.00 run under
`manual-3d-ecalib-01`: calibration and reconstruction returned `0`, generated
maps passed structural checks, and the final volume passed the existing
structural checker. These are the manual results for this synthetic case; the
matching automated run and manual-to-automated comparisons are reported below.

The public function is
`run_reconstruction(ReconstructionConfig(...))`. The FFT normalization
default is the reviewed unitary convention. CS processing values are required
explicitly or supplied through the named manual example profile; the profile
is not a universal scientific default. Effective values and stage results are
recorded in the new run directory. The requested BART executable spelling is
preserved, so a PATH lookup such as `bart` remains distinct from an explicit
relative path such as `./bart`. Existing output directories are rejected
without writing into them; if no run directory can be created, the diagnostic
is reported without a stage-record path. The reconstruction log is mandatory:
if BART succeeds but that log cannot be saved, the reconstruction stage retains
BART's code, the log failure is recorded separately, and the overall result is
non-zero.

## Owner-reported checks

Ricardo reported successful in-memory syntax compilation and terminal `--help`
(exit code `0` for each). He also reported local 2D, 3D and 3D CS runs with
BART exit code `0`, successful structural checks, and `log_error: null`.
Terminal `cmp` checks against the corresponding manual `.cfl` outputs returned
`0` for all three pairs. These checks establish byte-for-byte equality only
for those reported local executions; they are distinct from the separate
tutorial-block comparisons to synthetic references reported under Task 7.11.
The reported existing-output guard rejected the
pre-existing destination and preserved its dummy record. An earlier Pylance
syntax-check request timed out and is inconclusive. These synthetic checks do
not establish general compatibility, all FR-32 behavior, or scientific quality
acceptance. Ricardo separately reports one ARC execution for an acquired 3D CS
input; the configuration, reporting limits, and local visual review are
documented in the
[environment validation results](../docs/environment-validation-results.md).
That report does not establish general ARC compatibility or equivalence with a
Mac reconstruction.

For the local multichannel 3D CS `ecalib` case, Ricardo reported that the
automated invocation returned `0`. `ecalib.log` records BART code `0` and
`-r 64:16:16 -k 6:6:6 -t 0.001 -c 0.8 -m 1`; `reconstruction.log` records
BART code `0` and `pics` with the generated sensitivities, supplied mask and
k-space, and `--fista --wavelet dau2 -R W:7:0:0.01 -i 100 -s 0.95 -n -w 1.0`. The
`stage-records.json` reports all eight stages successful with code `0`,
`log_error: null` for calibration and reconstruction, and the resolved
effective settings and generated-map paths. Ricardo's `cmp` comparisons
between the manual and automated directories returned `0` for
`sensitivities.cfl`, `eigenvalues.cfl`, and `reconstruction.cfl`. This is
owner-reported byte-for-byte identity for those three files in this case; it
is not an automated comparison to a synthetic reference and does not establish
general compatibility, convergence, or scientific quality acceptance. The
separate owner-reported ARC execution is summarized in the
[environment validation results](../docs/environment-validation-results.md);
it is not evidence that multiple ESPIRiT map sets or other inputs are supported.
