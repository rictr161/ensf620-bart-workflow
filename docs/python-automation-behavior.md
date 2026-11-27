# Proposed Python Automation Behavior

**Status:** Behavior consolidated after Task 7.3; FR-32 approved in Task 7.5  
**Scope:** Task 7.2, derived from the reviewed manual Cartesian 2D, Cartesian 3D,
and Cartesian 3D compressed-sensing procedures

This document derives observable workflow behavior from the reviewed manual
procedures and the applicable requirements in the
[product requirements document](../tasks/prd-bart-reconstruction-workflow.md).
It is not an execution record or an architecture specification. The first
implementation block is documented separately in
[`src/bart_workflow.py`](../src/bart_workflow.py). Module structure, function
signatures, configuration formats, and further defaults remain open.

## 1. Requirements and source procedures

The behavior below is bounded by these requirements:

- **FR-22:** Python automation must be provided for the agreed procedures after
  the manual procedures are established, reviewed, and executed.
- **FR-23:** A terminal-based entry point is required.
- **FR-24:** Reconstruction settings must be configurable without assuming that
  optimal settings can be inferred automatically.
- **FR-25–FR-26:** The reconstruction must accept compatible BART `.cfl/.hdr`
  inputs and must operate on prepared inputs without requiring phantom
  generation.
- **FR-27:** Input inspection, configuration, reconstruction, output handling,
  and optional figure generation must remain distinguishable.
- **FR-28–FR-30:** Source inputs must be preserved, outputs separated by run,
  and run information associated with effective settings.
- **FR-31:** Figure generation must be optional, non-interactive, and saved for
  later inspection.
- **FR-32:** Approved behavior requires explicit reporting of invalid inputs,
  unsupported conditions, and execution failures without silent fallbacks.
- **FR-38–FR-40:** Fully sampled Cartesian 2D, fully sampled Cartesian 3D,
  and Cartesian 3D CS must be supported through a non-interactive terminal
  workflow with configuration and error reporting.

For the December 1, 2026 delivery, Cartesian 2D CS is outside the agreed
scope, following Ricardo's 2026-11-23 decision superseding its earlier
inclusion. It may be considered as a future extension without an implementation
commitment. Multiple ESPIRiT map-set support is a separate unresolved
capability; radial remains out of scope.

The source procedures are [manual Cartesian 2D](./tutorials/manual-cartesian-2d.md),
[manual Cartesian 3D](./tutorials/manual-cartesian-3d.md), and
[manual Cartesian 3D compressed sensing](./tutorials/manual-cartesian-3d-cs.md).
They establish the sequence of preparation, input checks, BART reconstruction,
output checks, optional figure generation, comparison, and evidence recording.
Their example values are case-specific and do not establish universal defaults.

The current scope remains Cartesian reconstruction. Radial 2D and radial 3D
are possible future extensions only. The separation below between spatial
dimensionality, trajectory, sampling information, CS selection, and
sensitivity origin keeps that extension conceptually possible; it does not
design or implement radial support.

## 2. Scope and starting inputs

The reconstruction operation must be able to start with already prepared,
compatible BART inputs. It must not require every run to regenerate a phantom,
repeat a preparation, generate a sampling mask, or create sensitivity maps.
Preparation and regeneration are separate activities from reconstruction.

The primary reconstruction input is prepared k-space in a BART-compatible
representation. It may come from an acquisition that was already
undersampled. The workflow must use that prepared k-space as supplied; it must
not generate or apply a new undersampling operation as an implicit
reconstruction step.

Spatial dimensionality, trajectory, CS selection, sampling information, and
sensitivity origin are separate declarations and checks. The workflow must
allow a Cartesian 2D or Cartesian 3D declaration and check it against the
input axes and other supplied information. It must not infer that a stack of
2D slices is a spatial 3D acquisition, or infer a trajectory from dimensions.
For the December delivery, CS is supported for Cartesian 3D only; Cartesian
2D CS remains outside scope. A missing CS selection must not silently select a
simple FFT for every multichannel or undersampled input.

For some acquisitions Ricardo knows the linear acceleration factor used during
acquisition. That factor must be representable as explicit acquisition
information, with its meaning and the axes to which it applies stated. It is
distinct from an effective acceleration calculated from an observed sampling
pattern. The factor alone does not determine which positions were acquired.

Sampling-mask generation in the synthetic CS preparation is distinct from
representing sampling in already acquired data. For CS reconstruction, the
sampling source must be selected explicitly: use a supplied mask or request
BART `pattern` estimation from the prepared k-space. The estimation route uses
the same input k-space as later stages and must not modify or resample it. An
invalid or unavailable supplied mask must fail; it must not trigger estimation
as a fallback.

The BART `pattern` method estimates the support of nonzero k-space. Omitted
positions must contain exact zeros for this estimate to represent them
correctly; a truly acquired position whose values are zero across all channels
can be interpreted as omitted. The resulting mask must pass the same
dimension, binary-value, and k-space consistency checks as a supplied mask
before calibration or reconstruction. An independent mask file is therefore
not universal, but the saved `mask3d` remains the explicit source for
equivalence with the reviewed manual CS example. This does not expand the
current scope to native scanner formats; the scope remains compatible BART
inputs.

For the currently communicated acquisition information, Ricardo's known
linear acceleration factor applies to his 3D CS case. It remains acquisition
information rather than a complete description of acquired positions and
cannot substitute for the sampling positions identified by a mask.

The synthetic reference image or volume and the corresponding fully sampled
k-space have separate roles. The documented visual and quantitative comparisons
use the reference and the reconstruction; they do not additionally require a
fully sampled k-space pair. For the CS example, `kspace_full` belongs to
synthetic preparation and to checking application of the sampling mask. It is
not required to reconstruct from `kspace_undersampled` or to perform those
image- or volume-level comparisons. By contrast, the fully sampled k-space is
the reconstruction input for the fully sampled Cartesian 2D and Cartesian 3D
cases. A reference is not a substitute for reconstruction k-space, and
`kspace_full` is not a replacement for the prepared undersampled input in the
CS case.

### Portability objective

The same automation code should be usable in Ricardo's local environment and
on ARC, with compatible dependencies and environment-specific configuration.
The code may be transferred through the repository or through a distribution
that preserves the required modules and resources; the concrete distribution
format remains open.

Input, output, and executable paths must be configurable and must not depend on
Ricardo's Mac directory structure. Python, its dependencies, and BART must be
prepared for the destination environment; the macOS virtual environment and
compiled executable must not be assumed to be reusable on ARC. The workflow
must be invocable from an ARC batch job with all configuration available before
execution begins. Environment and job-resource configuration must remain
distinguishable from reconstruction parameters.

Execution must not depend on windows or the interactive viewer. Effective
software versions and execution environment must be recorded. The current
workflow records the Python executable and version, imported NumPy version,
operating-system details and architecture, and configured BART executable.
After k-space validation and before any reconstruction operation, it queries
that executable with `version -V`; the command, exit code, response, and required
`bart-version.log` are associated with the `runtime-environment` stage.
Matplotlib's version is recorded only when the optional figure branch imports
it. This remains a portability objective pending execution verification on
ARC; it does not claim that ARC compatibility has been tested. Packaging,
installation, and launch details remain open.

## 3. Single non-interactive workflow entry

The automation should expose one non-interactive entry that receives readable
configuration and organizes the complete requested process. Without fixing a
future CLI or configuration format, its stages should be distinguishable as:

1. inspect the declared dimensionality, trajectory, inputs, sampling
   information, and sensitivity source;
2. after successful k-space inspection, record the runtime environment and
   query the configured BART executable with `version -V`; preserve the
   response in the required `bart-version.log` before any reconstruction
   operation;
3. when CS and `bart-pattern` are explicitly selected, run BART `pattern` on
   the inspected k-space, require and preserve its log, retain any produced
   output pair, and validate the mask only after a successful operation;
   otherwise validate the explicitly supplied mask. No implicit estimation
   or fallback is permitted;
4. check that the effective sampling mask is coherent with prepared k-space,
   including the configured calibration region when `ecalib` is requested;
5. for a selected route that uses sensitivities, either read supplied maps or
   check the inputs and reviewed requirements for a requested calibration;
6. for a requested `ecalib` route, execute calibration, preserve and check the
   generated maps, and then use the selected maps in `pics`;
7. translate the selected reconstruction behavior to the relevant BART
   operation and settings, then run `pics` when the selected procedure is CS;
8. check the reconstruction output;
9. record the result of each stage, including the requested and effective
   configuration, sampling source and mask, command, and separate
   operation/check outcomes.

The stages are conditional on the selected procedure. The reviewed fully
sampled, single-channel Cartesian FFT routes do not require sensitivity maps or
`ecalib`. A route that uses supplied sensitivities must check their
compatibility before reconstruction. A route that requests `ecalib` must not
check generated maps before calibration has produced them. In every
sensitivity-using route, the maps and map sets actually used must be recorded.

The same entry must be usable from a local invocation and from an ARC batch
job. All required configuration must be available before it begins. Environment
and job-resource settings remain distinct from reconstruction settings.

Sensitivity handling must permit either existing compatible maps or a request
to estimate maps with `ecalib`. Calibration requires suitable calibration data
and reviewed calibration parameters; it must not be assumed valid merely
because a k-space input exists. The number of acquired channels must be kept
distinct from the number of ESPIRiT map sets produced or selected for
reconstruction. Generated maps must be preserved, and the run record must
identify which map set or sets were actually used.

Later visualization of sensitivity maps is an independent operation. It must
read preserved maps, not repeat calibration or reconstruction, and must support
saved, non-interactive output without windows in ARC jobs.

## 4. Case behavior matrix

The following matrix separates computational reconstruction inputs from files
used to prepare or evaluate a case.

| Case | Computational reconstruction inputs | Pertinent checks | Manual BART operation | Required configuration | Required outputs | Optional capability |
|---|---|---|---|---|---|---|
| Cartesian 2D, fully sampled FFT route | Prepared fully sampled `kspace` BART pair; a preserved reference may be retained separately for evaluation. | Declared 2D dimensionality coherent with input axes; compatible pair, supported dimensions for the reviewed fixture, expected complex data, finite values, and readable input. | Centered unitary inverse `fft` over axes 0 and 1 (`-i -u 3`). | Spatial dimensionality, Cartesian trajectory, k-space input, sampling status, transform settings, output location, and reviewed channel conditions. | Separate reconstruction BART pair and stage-by-stage execution record. | Saved reconstruction figure; later reference comparison. |
| Cartesian 3D, fully sampled FFT route | Prepared fully sampled 3D `kspace` BART pair; a preserved reference may be retained separately for evaluation. | Declared 3D dimensionality coherent with input axes; compatible pair, supported dimensions for the reviewed fixture, expected complex data, finite values, and readable input. | Centered unitary inverse `fft` over axes 0, 1, and 2 (`-i -u 7`). | Spatial dimensionality, Cartesian trajectory, k-space input, sampling status, transform settings, output location, and reviewed channel conditions. | Separate reconstruction BART pair and stage-by-stage execution record. | Saved slice figure; later reference comparison. |
| Cartesian 3D CS route | Prepared k-space BART pair, explicit valid sampling representation, and compatible sensitivity maps or reviewed calibration input. The reference is used for evaluation; `kspace_full` is not required for acquired-data reconstruction. | Declared dimensionality and axes, Cartesian trajectory, pair readability, finite values, valid sampling representation, sensitivity-map compatibility, and correspondence among data, sampling, and maps. | `pics` with the selected CS behavior translated to relevant BART settings. | Spatial dimensionality, Cartesian trajectory, CS selection, sampling provenance, known acquisition acceleration when available, sensitivity origin, map-set selection, reconstruction settings, and output location. Manual values are case-specific. | Separate reconstruction BART pair, preserved maps, and stage-by-stage execution record identifying maps used. | Saved reconstruction and map figures; later reference comparison. |

The matrix describes behavior derived from the reviewed examples, not unrestricted
support for every BART array shape, acquisition convention, mask encoding, or
coil configuration. The compatibility boundary for each implementation must be
reviewed before it is treated as supported.

## 5. Input inspection

Before reconstruction, the workflow should inspect the supplied inputs and
record what it can establish without inferring acquisition semantics:

1. Confirm that each required BART pair is available and readable.
2. Read and record declared dimensions, trailing dimensions, data representation,
   and storage information that the supported reader can establish.
3. Check that the binary content is consistent with the header and that values
   required by the selected procedure are finite.
4. Check compatibility among k-space, sampling information, and sensitivities
   for the CS procedure.
5. Preserve the distinction between facts observed in files and configuration
   decisions supplied by the user.

The existing support scripts are useful evidence for the current fixtures but
are not generic workflow readers. The 2D reader in
[`check_fourier_numpy.py`](../scripts/check_fourier_numpy.py) is explicitly
limited to a 64 × 64 single-channel fixture with trailing singleton axes and
the documented complex64 storage. The 2D pair checker delegates to that reader.
The 3D reader in
[`check_preparation_pair_3d.py`](../scripts/check_preparation_pair_3d.py) receives
a base path and is limited to a 64 × 64 × 64 fixture, trailing singleton axes,
and the documented storage conditions. The fixed catalog of recognized pair
labels belongs to that script's CLI `pair` argument, not to the
`read_bart_3d` function's base-path reader. These limitations must not be
presented as proof that all compatible BART inputs have been covered, nor
should the future workflow silently generalize them.

The reviewed dimensions and one-channel conditions are properties of the tested
synthetic cases. They are not universal restrictions unless a later compatibility
decision adopts them. Conversely, dimensions alone must not be treated as proof
of acquisition semantics, sampling history, or suitable reconstruction
parameters.

The declared spatial dimensionality must be checked against the selected axes
and the supported input representation. This check must not equate a 2D slice
stack with a spatial 3D acquisition. Trajectory and CS selection are separate
configuration facts and are not determined by the header alone.

## 6. Explicit configuration and observable information

| Information | Category | Meaning and provenance |
|---|---|---|
| Declared array dimensions and trailing axes | Read or checked directly | Obtained from the BART header and checked against the selected supported compatibility conditions. It describes stored array structure, not acquisition meaning. |
| Presence, readability, binary size, data representation, and finiteness | Read or checked directly | Established from the `.hdr`/`.cfl` pair and the supported reader/checker. These are input-integrity facts, not quality results. |
| Spatial dimensionality and corresponding input axes | Explicit configuration, then checked | Ricardo must declare 2D or 3D; the workflow checks coherence with the input axes and does not infer a 3D acquisition from a stack of 2D slices. |
| Trajectory | Explicit configuration | Cartesian is the current supported scope. Dimensions do not establish trajectory. Radial support is a future extension, not a current behavior. |
| CS selection | Explicit configuration | For the December 1 delivery, CS is supported for Cartesian 3D only. It must not be inferred solely from multichannel data, apparent undersampling, or missing CS configuration. Cartesian 2D CS may be considered as a future extension without a current implementation commitment. |
| K-space input role and preparation status | Explicit configuration, with file checks | The supplied pair is the prepared reconstruction input. The workflow may check its structure but cannot infer its preparation history from dimensions alone. |
| Transform axes, normalization, centering, and reconstruction operation | Explicit configuration or reviewed case convention | These derive from the manual `fft` operations for the reviewed 2D and 3D cases, or from the reviewed `pics` operation for CS. The effective choices must be recorded. |
| Sampling representation and provenance | Explicit configuration, then checked | The current terminal interface selects either a supplied mask or an explicit BART `pattern` estimate from the exact input k-space. The estimated nonzero support is checked like a supplied mask; missing samples must be exact zeros, and an acquired position zero across all channels can appear omitted. Invalid supplied masks fail without fallback. |
| Known acquisition acceleration factor | Explicit acquisition information when available | Ricardo may provide a linear factor and the axes to which it applies. It describes reported acquisition sampling, does not identify acquired positions, and must remain distinct from effective acceleration calculated from a pattern. |
| Effective acceleration from a sampling pattern | Derived value when a valid pattern is available | It is calculated from the reviewed sampling representation and its stated domain. It must not be substituted for a reported acquisition factor or treated as the same quantity. |
| Sensitivity origin and representation | Explicit configuration, then checked | The user may provide existing maps or request `ecalib`. Calibration requires suitable data and reviewed parameters. Channel count and the number of ESPIRiT map sets are distinct facts. |
| Reconstruction settings such as CS selection, regularization, iterations, step, wavelet, scaling, and mask use | Explicit configuration or documented default | A readable CS selection may translate internally to relevant BART settings. Defaults, if later accepted, must be documented, modifiable, and recorded; no new numerical values are selected here. |
| Output location and run identity | Explicit configuration or reviewed run convention | The destination must be separate from source inputs and distinguish one execution from another. The concrete naming and configuration mechanism remain open. |
| Omitted parameter values | Potential documented defaults, pending review | A default may be appropriate only where its meaning and intended use are documented. The value must be recorded as a default in the effective configuration. No new default is selected here. |
| Reference image/volume | Evaluation input, not an automatic reconstruction input | It preserves the known synthetic case and is paired with the reconstruction for the documented visual and quantitative comparisons. Those comparisons do not additionally require a fully sampled k-space pair. |
| Fully sampled k-space | Reconstruction input for fully sampled Cartesian 2D and Cartesian 3D; preparation input for the CS example | It is the prepared reconstruction input for the fully sampled cases. In the CS example, `kspace_full` belongs to synthetic preparation and mask-application checking; it is not required for reconstruction from `kspace_undersampled` or for reference-image/volume comparisons. |
| Calibration data and parameters | Explicit configuration, then checked | Data suitable for `ecalib` and reviewed calibration parameters must be identified before estimation. Their availability is not established by channel count alone. |
| ESPIRiT map-set selection | Explicit configuration, then checked | The run must distinguish acquired channels from the number of map sets and record which generated or supplied sets were used. |

Values such as 64 × 64, 64 × 64 × 64, one channel, the reviewed Fourier
bitmasks, the Poisson settings, the CS mask, and the reviewed `pics` settings
describe the documented manual cases. They must not be promoted to universal
defaults or interpreted as optimal settings.

## 7. Reconstruction invocation and output handling

The future workflow should perform a non-interactive sequence with all required
configuration available before reconstruction begins:

1. Resolve the declared dimensionality, trajectory, CS selection, prepared
   inputs, sampling-information provenance, sensitivity source, explicit
   settings, and output destination.
2. Inspect and validate inputs before invoking BART, including sampling and
   sensitivity checks.
3. If the selected route uses sensitivities, read and check supplied maps or
   perform the separately requested and reviewed `ecalib` calibration, then
   preserve and check generated maps before using them.
4. Translate a simple CS selection to the relevant BART settings and invoke the
   operation corresponding to the reviewed procedure, without
   generating a new phantom or applying new undersampling to supplied k-space.
5. Keep source `.hdr`/`.cfl` pairs unchanged.
6. Write the reconstruction into a distinct run location.
7. Check the produced reconstruction using checks appropriate to the supported
   compatibility boundary.
8. Record each stage, the effective configuration, maps used, operational
   result, and post-reconstruction check separately.

The output check establishes structural/readability conditions for the supported
fixture; it does not establish agreement with a reference, convergence, or
quality acceptance. A later reference comparison is a separate operation.

An exit code must describe the operation that produced it. A reconstruction
command's result must not be inferred from the later existence of output files,
and a later check's result must not be substituted for the reconstruction
operation's result.

## 8. Run association and evidence traceability

Each run needs enough recorded information to associate the output with:

- the selected case and the prepared input identities;
- the declared spatial dimensionality, input axes, Cartesian trajectory, and CS
  selection;
- the reference or fully sampled preparation identity when used for evaluation;
- the sampling-information source and its stated meaning for CS;
- for BART `pattern`, the input k-space, command, actual exit code, required
  log, generated mask pair, and separate mask-check result;
- the sensitivity source, calibration data and parameters if `ecalib` was used,
  preserved generated maps, map-set selection, and maps used in reconstruction;
- the explicit values supplied by the user;
- values derived from reviewed conventions or valid input information;
- documented defaults actually used;
- the effective reconstruction settings;
- the invocation performed and its operational result;
- the Python executable and version, imported NumPy version, operating-system
  details and architecture, configured BART executable, and BART version-query
  command, exit code, response, and associated log;
- post-reconstruction checks and their separate results;
- optional figure-generation results and file identities, including the
  Matplotlib version when it is imported for that requested operation;
- failures, corrections, unresolved conditions, and limitations.

This information must remain reviewable without overwriting source inputs or
confusing a later comparison with the reconstruction itself. The concrete
manifest, record-file names, and configuration format are implementation
decisions for later review; this proposal specifies the information, not its
storage schema.

## 9. Optional figures and evaluation boundaries

Figure generation is optional. When requested, it must save files and operate
without windows, dialogs, or interactive questions. It must report the inputs,
display-relevant settings, generated file identity, and its own operational
result. Matplotlib is loaded only for a requested figure, and its version is
recorded within that optional stage.

A reconstruction figure can show the produced reconstruction without requiring a
reference. A comparative figure requires an identified reference and must state
that it is a comparison presentation. Neither type of figure is a human
inspection record by itself. Figure generation is not visual acceptance and does
not establish reconstruction quality.

Sensitivity-map visualization is a separate optional operation. It reads
preserved supplied or generated maps and must not repeat calibration or
reconstruction. It must save non-interactive output and must not introduce
windows into ARC batch jobs.

The workflow must keep these activities separate:

1. reconstruction from prepared inputs;
2. reconstruction-to-reference comparison;
3. manual-to-automated route comparison.

The application of the reviewed comparison methods to automated results is
recorded under Tasks 7.10–7.12. Ricardo reported evaluating the three existing
synthetic automated outputs with the tutorial blocks; this did not add a
comparison CLI to `bart_workflow.py`. No new metric, tolerance, expected result,
or pass/fail classification was introduced.

## 10. Proposed FR-32 behavior

The following approved behavior describes explicit detection and preservation.
It does not add automatic retries, fallback parameter changes, complex recovery,
or silent cleanup.

| Detected condition | Proposed behavior | Information recorded | State of existing files and results |
|---|---|---|---|
| Required input files are absent, unreadable, malformed, or contain invalid values | Report the affected input and stop before using it | Input identity, expected role, read or validation detail, and stage | Preserve all existing source inputs; do not create a reconstruction result from the invalid input |
| Configuration is missing, contradictory, or incompatible with the declared dimensionality, trajectory, sampling information, or sensitivity route | Report the conflicting configuration and stop before reconstruction | Configuration categories, supplied values, selected case, and compatibility finding | Preserve source inputs and prior results; do not silently change parameters or select another route |
| Input conditions are not admitted by the supported workflow | Report the unsupported condition explicitly and stop before the unsupported operation | Observed dimensions, axes, channel/map information, trajectory, sampling source, and supported-condition description | Preserve inputs and prior results; do not silently generalize the supported boundary |
| BART is unavailable or cannot be invoked | Report the executable identity or availability failure before reconstruction | Configured executable path, requested operation, environment information, and diagnostic detail | Preserve inputs; do not create a success-shaped reconstruction result |
| The required BART version query returns non-zero or `bart-version.log` cannot be saved | Preserve the actual query result, report the log failure separately when applicable, and stop before dependent processing | Runtime-environment stage, configured executable, command, response when available, query exit code, requested log path, and log-write result | Preserve the run directory and any produced records; do not claim an unsaved log |
| A BART command fails during sampling-pattern estimation, calibration, or reconstruction | Record the failed operation and its diagnostics, then leave the existing run evidence available for review | Stage, invocation, actual operational result, diagnostics, effective settings, and affected output role | Preserve source inputs and any already produced results; do not reuse a prior output merely because it exists |
| A post-operation sampling-mask, sensitivity-map, or reconstruction check fails | Record the failed check separately from the operation that produced the files | File identity, check performed, observed result, original operation result, and stage | Preserve produced files and prior evidence for review; do not relabel the operation as successful |
| An output directory or expected output already exists | Report the collision and require an explicitly reviewed destination decision | Existing path, requested output role, selected case, and run identity | Do not overwrite or silently reuse the existing output |
| Optional reconstruction-figure or sensitivity-map-figure generation fails | Record the figure failure separately; do not treat it as a reconstruction failure solely because the optional operation failed | Figure request, source result identity, display settings, diagnostics, and figure-stage result | Preserve reconstruction, maps, and their records; retain the reconstruction result independently of the optional figure |

These behaviors preserve inputs and existing results, avoid silent parameter
changes, and prevent reuse based only on output existence. The reconstruction
and its mandatory checks produce exit code `0` only when both complete
successfully; a mandatory failure produces a non-zero exit code. A failure only
in optional figure generation is recorded and communicated as a separate
warning while preserving the success of a valid reconstruction. The single
workflow entry, accepted Cartesian route choices, explicit CS selection,
supplied or explicitly requested sampling information, sensitivity routes,
stage records, separated run directories, effective-parameter records, and
optional saved figures are behavior decisions consolidated in Task 7.3; they
are not claims of scientific validation.

## 11. Consolidated Task 7.3 decisions and remaining review

The following behavior decisions are accepted for the proposal after Ricardo's
review:

- one readable, non-interactive entry usable locally and from ARC;
- prepared k-space in a BART-compatible format;
- fully sampled Cartesian 2D and 3D routes, plus Cartesian 3D CS, selected
  explicitly;
- user-configurable processing parameters with documented, modifiable defaults
  where appropriate;
- automatic reading of available file information and internal compatibility
  checks;
- supplied sensitivities or explicitly requested `ecalib`, only for routes
  that need sensitivities;
- supplied sampling information or explicitly requested estimation through an
  admitted and checked method, with known acceleration kept separate from the
  sampling pattern;
- per-stage results, separate run directories, and effective-parameter records;
- optional figures and later visualization of saved results.

ARC usability here describes the non-interactive entry/interface objective; it
does not commit to generalized ARC deployment or batch support. The PRD's
2026-11-26 approved delivery scope includes one owner-reported ARC Slurm run for
one volume. Its script configuration and the limits of the available evidence
are recorded in the
[environment validation results](environment-validation-results.md); this
single report does not verify general ARC compatibility.

Ricardo has reported a local synthetic Cartesian 3D multichannel CS execution
using `bart-pattern` with `ecalib` and one map set. BART `version -V`,
`pattern`, `ecalib`, and `pics` each recorded exit code `0`; all 11 stage
records report success with code `0`. The generated mask passed checks and was
used by `pics`; the generated sensitivities were used in the same run. The
records include the effective profile, software/environment versions, a
successful structural output check, and a successful figure stage. Ricardo's
`cmp` between this reconstruction and an earlier automated reconstruction
using a supplied mask returned `0`. This is an automated-to-automated,
case-specific identity result, not a direct manual or synthetic-reference
comparison. The global CLI exit code and a new human visual inspection of the
figure were not reported.

A separate earlier manual and local automated synthetic Cartesian 3D
multichannel CS case used `ecalib` with one map set and a supplied mask. Its
automated invocation returned `0`; its eight recorded stages succeeded with
code `0`, and the calibration and reconstruction logs reported no log errors.
Ricardo also reported `cmp` exit code `0` for the direct manual-to-automated
`sensitivities.cfl`, `eigenvalues.cfl`, and `reconstruction.cfl` pairs. These
results are case-specific; they do not establish general compatibility, ARC
execution, convergence, or scientific quality acceptance, and the comparisons
are not automated comparisons to a synthetic reference.

The `bart-pattern` route has thus been exercised in one reported case, but
general correctness of the sampling-estimation method remains unestablished.
Preservation, selection, and recording of multiple ESPIRiT map sets remain a
separate unsupported capability. Cartesian 2D CS is outside the December 1
delivery scope and may be considered as a future extension without an
implementation commitment; its earlier bounded checks are not delivery
blockers. Coil compression is not a universal requirement. The single entry
is not an additional manual procedure required by FR-22.

The initial implementation selects and documents concrete checks and settings
for its supported scope. PRD questions about expanding compatibility beyond
that boundary, admitting additional sampling-estimation methods, and future
configuration or evidence formats remain open.

## 12. Automated reference evaluation: method and reported results

Reference evaluation is optional and separate from reconstruction. A
reconstruction can run without a reference; when a suitable reference is
unavailable, including for acquired data, comparison is omitted without error
and no reference is fabricated. The reported evaluation applies the reviewed
methods in the [manual 2D](./tutorials/manual-cartesian-2d.md),
[manual 3D](./tutorials/manual-cartesian-3d.md), and
[manual 3D CS](./tutorials/manual-cartesian-3d-cs.md) tutorials to existing
automated outputs only:

| Case | Reference base | Existing automated reconstruction base | Visual method |
|---|---|---|---|
| Cartesian 2D | `generation-01/reference` | `automated-2d-01/reconstruction` | Side-by-side full-image magnitudes |
| Cartesian 3D | `generation-3d-01/reference` | `automated-3d-01/reconstruction` | Three orthogonal central-plane pairs |
| Cartesian 3D CS | `generation-3d-cs-01/reference` | `automated-3d-cs-01/reconstruction` | Three orthogonal central-plane pairs |

Use the corresponding tutorial visual and quantitative blocks, changing only
the input bases and output destinations. The 2D reader
[`read_bart_2d`](../scripts/check_fourier_numpy.py) is limited to the reviewed
64 × 64 single-channel fixture. For both 3D cases, reuse
[`read_bart_3d`](../scripts/check_preparation_pair_3d.py) and
[`relative_error`](../scripts/check_fourier_numpy.py) for the documented
64 × 64 × 64 single-channel fixtures. Do not include
`automated-3d-pattern-ecalib-01`: a compatible scalar reference for that
multichannel calibration result has not been established.

The 2D figure compares `abs(array).T` for reference and reconstruction using a
shared grayscale range from zero to the reference maximum. The 3D figures
compare the three zero-based central planes at index 32 on each axis, with
reference and reconstruction in separate rows and the same shared range.
Retain the tutorial presentation (`origin="lower"`, equal aspect, no
interpolation), array-index labels, and its magnitude-range diagnostics.
Do not assign anatomical orientation to array axes. Transposition is for
display only. Record figure generation separately from any human visual
observation; neither a generated figure nor an observation is a quality
acceptance result.

For each case, calculate the relative L2 error on the complete original
complex arrays:

```text
||reconstruction - reference||₂ / ||reference||₂
```

Use the tutorial readers and `relative_error`; retain their shape/storage
handling, finite and nonzero reference-norm checks, and finite-result check.
Do not convert to magnitude, transpose, crop, mask, align, rescale, or correct
phase. The reference norm is the metric denominator, not a separate
normalization. Report the observed value without adding a tolerance or pass/fail
classification.

The existing reconstruction pairs, logs, and stage records were left unchanged.
Ricardo reported the evaluations under
`$HOME/bart-learning/bart-workflow-reconstructions/automated-reference-evaluations/`:

| Case | Evaluation directory | Relative L2 error | Calculation / figure exit codes | Reported observation and display limit |
|---|---|---:|---|---|
| Cartesian 2D | `cartesian-2d-TAT46E` | `1.442448308e-07` | `0` / `0` | Ricardo saw no evident visual differences; limit `1`. Figure: `figures-visual/reference-reconstruction.png`. |
| Cartesian 3D | `cartesian-3d-EqHsLn` | `1.729089800e-07` | `0` / `0` | Ricardo saw no visual differences in the reviewed figure; limit `2`, with small exceedances in all three displayed cuts. Figure: `figures-visual/reference-reconstruction-orthogonal.png`. |
| Cartesian 3D CS, original single-channel case | `cartesian-3d-cs-hBicqH` | `2.473308708e-01` | `0` / `0` | Ricardo observed a noisier appearance than the reference and an appearance similar to the manual result; limit `2`, while the reconstruction global maximum was `2.851191679`. Figure: `figures-visual/reference-reconstruction-orthogonal.png`. |

Each directory contains `quantitative-comparison.txt`,
`visual-comparison.log`, and its figure under `figures-visual/`. The records
report Python `3.13.17`, NumPy `2.5.4`, and Matplotlib `3.11.2`. The display
limit warnings did not change the figure-generation exit codes. The quantitative
values match the previously reported manual-to-reference values at the
displayed precision, but these are separate evaluations of the automatic
outputs, not the prior manual-to-automated binary comparisons.

The manual-to-reference results remain those recorded under Tasks 4.4–4.5,
5.8, and 6.8; the manual-to-automated `.cfl` identity checks remain under Task
7.8. Ricardo executed the blocks and inspected the reported figures; ChatGPT
reviewed the results and guided the executions. These observations cover the
reviewed views, not every slice, and establish no general scientific quality
acceptance. No multichannel `ecalib` reference comparison was performed. No
reconstruction CLI feature was added: reference evaluation remains optional
and is performed separately with the existing tutorial support.

## 13. Proposed manual–automated comparison conditions

These are the conditions proposed under Task 8.1 and explicitly approved by
Ricardo under Task 8.2. The approval covers the matched inputs, effective
settings, output pairs, and reuse of the historical evidence; it does not
change the approvals of the numerical method recorded in Section 14. Reuse
the preserved preparations and route results rather than requesting new
reconstructions. Paths in the following records are relative to
`/Users/ricardoaguilar/bart-learning/bart-workflow-reconstructions/`.

| Case | Shared prepared inputs and interpretation | Effective reconstruction operation/settings | Manual output | Automated output |
|---|---|---|---|---|
| Cartesian 2D | `generation-01/kspace`; the documented 64 × 64, single-channel fixture, interpreted over axes 0 and 1 | Centered unitary inverse FFT, `fft -i -u 3` | `manual-2d-01/reconstruction` | `automated-2d-01/reconstruction` |
| Cartesian 3D | `generation-3d-01/kspace`; the documented 64 × 64 × 64, single-channel fixture, interpreted over axes 0, 1, and 2 | Centered unitary inverse FFT, `fft -i -u 7` | `manual-3d-01/reconstruction` | `automated-3d-01/reconstruction` |
| Cartesian 3D CS, original single-channel case | `generation-3d-cs-01/kspace_undersampled` and that preparation's `mask3d` and `sensitivities`; the documented 64 × 64 × 64, single-channel interpretation | `pics`: FISTA, wavelet `dau2`, regularization `W:7:0:0.01`, iteration limit `100`, step `0.95`, random shift disabled, data scaling `1` | `manual-3d-cs-01/reconstruction` | `automated-3d-cs-01/reconstruction` |

Each route pair must use the same prepared file contents and dimensional
interpretation. Compare effective operations and values, not literal command
strings: for example, `-w 1` and `-w 1.0` express the same data-scaling value.
For CS, the mask, sensitivities, and every effective reconstruction setting
must correspond. The primary scientific outputs are the BART reconstruction
pairs (`.hdr` and `.cfl`), including their structure and complex data. Output
directories, logs, and provenance metadata may differ. Header path differences
expected from separate run directories must be retained and explained, not
removed to force equality. The approved output pair and history conditions do
not by themselves establish the comparison method; Ricardo's approval of that
method is documented in Section 14. No manual–automated L2 error is recorded.

### Existing records and limits

Task 7.8 records owner-reported `cmp` exit code `0` for the manual and
automated `reconstruction.cfl` files in all three pairs. Ricardo approved
reusing these historical results under the Task 8.2 conditions. They predate
formalization of Block 8 and were not produced under a prospectively approved
Block 8 protocol. The reported automated run directories contain the
reconstruction pair, `reconstruction.log`, and `stage-records.json`. The
previously shared automated `reconstruction.log` and `stage-records.json`
records contain the executed BART command arrays and effective settings for
the three cases. The original Python CLI strings and per-run repository
revisions are not established by the summary. Software-version coverage
should be attributed only to the records available for each run; the later
runtime-environment stage must not be assigned retrospectively to earlier
executions.

Manual records are case-specific: the 2D directory contains
`reconstruction.log`, output-check, visual-generation, and
quantitative-comparison records plus its existing `run-record.md`; the 3D
evidence includes the BART result and structural check, with a cumulative
`run-record.md` optional; the CS `run-record.md` links its local logs and
preparation records. These local records are outside the repository. The
historical `cmp` report names the compared `.cfl` pairs and code `0`; it does
not provide the exact shell command strings, separate `cmp` logs, or a direct
comparison of the two `.hdr` files.

Ricardo shared the contents of all six reconstruction headers for semantic
review. The manual and automated 2D headers both declare `64 × 64`, with
trailing axes equal to one, and `fft -i -u 3` on the same
`generation-01/kspace`. The 3D headers both declare `64 × 64 × 64`, with
trailing axes equal to one, and `fft -i -u 7` on the same
`generation-3d-01/kspace`. The original single-channel CS headers both
declare `64 × 64 × 64`, with trailing axes equal to one, and correspond to the
same `generation-3d-cs-01/kspace_undersampled`, `mask3d`, and `sensitivities`.
They record `--fista --wavelet dau2 -R W:7:0:0.01 -i 100 -s 0.95 -n`,
with `-w 1` manually and `-w 1.0` automatically; the effective scaling value
is the same. All six headers declare `BART v1.0.00` in `# Creator`. The
differences in `# Command` and `# Files` are the expected manual/automated
output-directory paths and are retained as provenance. This header evidence
establishes the version declared there, not a complete runtime-environment
record for the historical executions.

The Task 7.11 comparisons are automated-output-to-reference evaluations, not
manual–automated comparisons. Their visual observations concern the reported
reference figures and do not establish direct visual inspection of each
manual–automated pair. The multichannel `ecalib` manual–automated result is
complementary evidence for a separate case; the sampling-variant comparison is
automated-to-automated.

## 14. Approved manual–automated comparison method and reviewed results

Ricardo approved this method under Task 8.4. For each pair in Section 13,
compare the exact binary contents of the manual and automated
`reconstruction.cfl` files with `cmp`. The comparison conditions are the
preserved prepared inputs, compatible dimensional and complex-data
interpretation, corresponding effective operations/settings, and—for CS—the
same undersampled k-space, mask, and sensitivities. The structural checks
listed below and the six reviewed headers confirm the documented dimensions
and output pairing. No new reconstruction or post-approval binary comparison
is claimed; the reported `cmp` results are historical results reused under
the approved method.

| Case | Shared input and effective configuration | Structural checks and header review | Historical `.cfl` comparison |
|---|---|---|---|
| Cartesian 2D | `generation-01/kspace`; `fft -i -u 3`; the automated BART command array and effective settings are in `reconstruction.log` and `stage-records.json` | Manual `reconstruction-check.txt`: `VALID`, 64 × 64, singleton trailing axes, expected size, finite values (code `0`); automated structural check reported successful. Both headers declare matching dimensions, operation and input. | `manual-2d-01/reconstruction.cfl` vs `automated-2d-01/reconstruction.cfl`; historical `cmp` code `0` |
| Cartesian 3D | `generation-3d-01/kspace`; `fft -i -u 7`; the automated BART command array and effective settings are in `reconstruction.log` and `stage-records.json` | Manual structural output check `VALID` (code `0`); automated structural check reported successful. Both headers declare matching dimensions, operation and input. | `manual-3d-01/reconstruction.cfl` vs `automated-3d-01/reconstruction.cfl`; historical `cmp` code `0` |
| Cartesian 3D CS, original single-channel case | `generation-3d-cs-01/kspace_undersampled` with its `mask3d` and `sensitivities`; `--fista --wavelet dau2 -R W:7:0:0.01 -i 100 -s 0.95 -n`, with `-w 1` manually and `-w 1.0` automatically (same effective value). Automated command array/settings are in `reconstruction.log` and `stage-records.json`; the manual `run-record.md` links its settings and logs. | Manual structural check `VALID` (code `0`); automated structural check reported successful. Both headers declare matching dimensions, inputs, and effective CS settings. | `manual-3d-cs-01/reconstruction.cfl` vs `automated-3d-cs-01/reconstruction.cfl`; historical `cmp` code `0` |

Ricardo shared all six headers. They declare 64 × 64 (2D) or 64 × 64 × 64
(3D/CS), with later axes singleton, and each declares `BART v1.0.00` in
`# Creator`. The `# Command` and `# Files` route-specific path differences
correspond to the expected manual and automated output directories. They are
preserved and explained; they do not erase or excuse differences in dimensions,
effective options, or version fields. This is the version declared by the
headers, not a complete environment record for these executions. The recorded
historical comparison method is `cmp` on each listed file pair, with reported
code `0`; the exact original shell strings and separate `cmp` log paths were
not recorded and are not reconstructed here.

Interpret `cmp` as follows:

- Exit code `0`: the two `.cfl` files are byte-identical. Together with the
  reviewed compatible BART-pair structures, this supports identity of the
  reconstructed data for that pair.
- Exit code `1`: the files differ as binary data. This alone neither
  quantifies a numerical difference nor constitutes a scientific-quality
  failure.
- Exit code greater than `1`: the comparison encountered an operational
  problem; it establishes neither equality nor difference of the data.

### Direct visual route comparison

Ricardo opened the preserved figures and directly compared the manual and
automated reconstruction panels. His reported observation for all three cases
is that he did not identify visible differences between the manual and
automated panels in the views shown.

| Case | Manual figure | Automated figure | Scope of observation |
|---|---|---|---|
| Cartesian 2D | `manual-2d-01/figures-visual/reference-reconstruction.png` | `automated-reference-evaluations/cartesian-2d-TAT46E/figures-visual/reference-reconstruction.png` | The displayed 2D reconstruction panels |
| Cartesian 3D | `manual-3d-01/figures-visual/reference-reconstruction-orthogonal.png` | `automated-reference-evaluations/cartesian-3d-EqHsLn/figures-visual/reference-reconstruction-orthogonal.png` | The displayed central-plane reconstruction panels, not every slice |
| Cartesian 3D CS, original single-channel case | `manual-3d-cs-01/figures-visual/reference-reconstruction-orthogonal.png` | `automated-reference-evaluations/cartesian-3d-cs-hBicqH/figures-visual/reference-reconstruction-orthogonal.png` | The displayed central-plane reconstruction panels, not every slice |

These are direct manual-to-automated visual observations using existing
figures. They are not the Task 7.11 observations comparing an automated
reconstruction with its synthetic reference, and they do not convert the
binary identity result into a claim of visual inspection. The multichannel
`ecalib` manual–automated result remains complementary evidence for another
case; the sampling-variant comparison remains automated-to-automated.

The three `cmp` results were reported before formalization and approval of the
Block 8 method; they are explicitly reused as historical evidence, not
represented as post-approval executions. No manual–automated L2 error,
tolerance, or scientific pass/fail criterion is recorded. This route
comparison remains separate from reference evaluation and from future
operator-intervention measurement.
