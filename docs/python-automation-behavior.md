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
- **FR-38–FR-40:** The three agreed cases must be supported through a
  non-interactive terminal workflow with configuration and error reporting.

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
CS selection must be available for both Cartesian 2D and Cartesian 3D. A
missing CS selection must not silently select a simple FFT for every
multichannel or undersampled input.

For some acquisitions Ricardo knows the linear acceleration factor used during
acquisition. That factor must be representable as explicit acquisition
information, with its meaning and the axes to which it applies stated. It is
distinct from an effective acceleration calculated from an observed sampling
pattern. The factor alone does not determine which positions were acquired.

Sampling-mask generation in the synthetic CS preparation is distinct from
representing sampling in already acquired data. The workflow must not infer a
sampling pattern silently from nonzero k-space values, and must not select the
CS procedure solely because an input appears undersampled.

The workflow must have valid sampling information when the selected procedure
requires it. Its provenance may be a supplied mask, compatible sampling
indices or metadata, or an estimation method whose conditions have been
reviewed. An independent mask file is not a universal requirement. For
equivalence with the reviewed manual CS example, the saved `mask3d` is the
explicit sampling input and must remain available as such. This clarification
does not expand the current scope to native scanner formats; the current scope
remains compatible BART inputs.

For the currently communicated acquisition information, Ricardo's known
linear acceleration factor applies to his 3D CS case. It remains acquisition
information rather than a complete description of acquired positions.

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
software versions and execution environment must be recorded. This is a design
and portability objective pending verification through execution on ARC; it
does not claim that ARC compatibility has been tested. Packaging, installation,
and launch details remain open.

## 3. Single non-interactive workflow entry

The automation should expose one non-interactive entry that receives readable
configuration and organizes the complete requested process. Without fixing a
future CLI or configuration format, its stages should be distinguishable as:

1. inspect the declared dimensionality, trajectory, inputs, sampling
   information, and sensitivity source;
2. check that the declared sampling information is valid and coherent with the
   prepared k-space;
3. for a selected route that uses sensitivities, either read supplied maps or
   check the inputs and reviewed requirements for a requested calibration;
4. for a requested `ecalib` route, execute calibration, preserve and check the
   generated maps, and then use the selected maps in `pics`;
5. translate the selected reconstruction behavior to the relevant BART
   operation and settings, then run `pics` when the selected procedure is CS;
6. check the reconstruction output;
7. record the result of each stage, including the effective configuration and
   operational outcome.

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
| Cartesian 2D or 3D CS route | Prepared k-space BART pair, explicit valid sampling representation, and compatible sensitivity maps or reviewed calibration input. The reference is used for evaluation; `kspace_full` is not required for acquired-data reconstruction. | Declared dimensionality and axes, Cartesian trajectory, pair readability, finite values, valid sampling representation, sensitivity-map compatibility, and correspondence among data, sampling, and maps. | `pics` with the selected CS behavior translated to relevant BART settings. | Spatial dimensionality, Cartesian trajectory, CS selection, sampling provenance, known acquisition acceleration when available, sensitivity origin, map-set selection, reconstruction settings, and output location. Manual values are case-specific. | Separate reconstruction BART pair, preserved maps, and stage-by-stage execution record identifying maps used. | Saved reconstruction and map figures; later reference comparison. |

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
| CS selection | Explicit configuration | CS may be selected for Cartesian 2D or 3D. It must not be inferred solely from multichannel data, apparent undersampling, or missing CS configuration. |
| K-space input role and preparation status | Explicit configuration, with file checks | The supplied pair is the prepared reconstruction input. The workflow may check its structure but cannot infer its preparation history from dimensions alone. |
| Transform axes, normalization, centering, and reconstruction operation | Explicit configuration or reviewed case convention | These derive from the manual `fft` operations for the reviewed 2D and 3D cases, or from the reviewed `pics` operation for CS. The effective choices must be recorded. |
| Sampling representation and provenance | Explicit configuration, then checked | A supplied mask, compatible indices/metadata, or a reviewed estimation method identifies sampling. The workflow must not silently recover a mask from nonzero k-space values. |
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
- the sensitivity source, calibration data and parameters if `ecalib` was used,
  preserved generated maps, map-set selection, and maps used in reconstruction;
- the explicit values supplied by the user;
- values derived from reviewed conventions or valid input information;
- documented defaults actually used;
- the effective reconstruction settings;
- the invocation performed and its operational result;
- post-reconstruction checks and their separate results;
- optional figure-generation results and file identities;
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
result.

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

The applications of the reviewed comparison methods to automated results belong
to Tasks 7.10–7.12. This proposal introduces no new metric, tolerance, expected
result, or pass/fail classification.

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
| A BART command fails during calibration or reconstruction | Record the failed operation and its diagnostics, then leave the existing run evidence available for review | Stage, invocation, operational result, diagnostics, effective settings, and affected output role | Preserve source inputs and any already produced results; do not reuse a prior output merely because it exists |
| A post-operation input, sensitivity-map, or reconstruction check fails | Record the failed check separately from the operation that produced the files | File identity, check performed, observed result, original operation result, and stage | Preserve produced files and prior evidence for review; do not relabel the operation as successful |
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
- Cartesian 2D and 3D routes with explicit reconstruction selection with or
  without CS;
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

The sampling-estimation method, Cartesian 2D CS, and multiple ESPIRiT map-set
capabilities remain unvalidated. Ricardo has reported both manual and local
automated execution of one synthetic Cartesian 3D multichannel CS case using
`ecalib` with one map set. The automated invocation returned `0`; its eight
recorded stages succeeded with code `0`, and the calibration and reconstruction
logs reported no log errors. Ricardo also reported `cmp` exit code `0` for the
manual-to-automated `sensitivities.cfl`, `eigenvalues.cfl`, and
`reconstruction.cfl` pairs. This is case-specific owner-reported evidence, not
general compatibility, ARC execution, convergence, or scientific quality
acceptance. These `cmp` checks are not automated comparisons to a synthetic
reference. Coil compression is not a universal requirement. The single entry
is not an additional manual procedure required by FR-22; its checks belong to
later implementation and execution tasks. Bounded manual checks for Cartesian
2D CS and for preservation, selection, and recording of multiple map sets
remain necessary before equivalence for those capabilities can be claimed.

Remaining implementation-stage decisions include the concrete supported input
boundary, admitted sampling-estimation methods, mandatory cross-input checks,
and specific configuration and evidence details without fixing interfaces or
formats.
