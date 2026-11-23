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
later axes without hard-coding spatial dimensions or channel count. A spatial
sampling mask is applied across channels and must be supplied explicitly; the
configured calibration region must also be fully sampled. FFT routes remain
single-channel. Cartesian 2D CS, multiple ESPIRiT map sets,
sampling-pattern estimation, figures, automated comparisons, and radial
reconstruction remain outside this block. Ricardo's manual multichannel
`ecalib` execution and a matching local automated run are documented below.
This case-specific evidence does not claim compatibility with unreviewed BART
array layouts.

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

The run directory retains `ecalib.log`, the generated `sensitivities` and
`eigenvalues` BART pairs, `reconstruction.log`, the `reconstruction` pair, and
`stage-records.json`. The records include actual commands and BART exit codes,
effective calibration and reconstruction settings, file identities, and
separate check results. Failed calibration or mandatory checks stop dependent
steps; produced files are preserved.

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
`0` for all three pairs. These results establish byte-for-byte equality only
for those reported local executions; they are not automated comparisons to the
synthetic references. The reported existing-output guard rejected the
pre-existing destination and preserved its dummy record. An earlier Pylance
syntax-check request timed out and is inconclusive. These checks do not
establish ARC execution, general compatibility, all FR-32 behavior, or
scientific quality acceptance.

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
general compatibility, ARC execution, convergence, or scientific quality
acceptance.
