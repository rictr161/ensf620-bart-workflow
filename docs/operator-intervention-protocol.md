# Operator-Intervention Measurement Protocol

**Status:** Approved by Ricardo in Task 9.2 on 2026-11-24; not yet applied to
measurement runs.

## 1. Purpose and scope

This protocol defines a prospective method for counting observable human
interventions in matched manual and automated synthetic reconstruction runs.
It addresses the operator-intervention question in PRD Section 8.4 and open
question 16. It does not measure reconstruction quality, route equivalence,
causality, or general user effort.

The four matched pairs are based on the reviewed synthetic procedures and
settings in the [Cartesian 2D tutorial](./tutorials/manual-cartesian-2d.md),
[Cartesian 3D tutorial](./tutorials/manual-cartesian-3d.md),
[Cartesian 3D CS tutorial](./tutorials/manual-cartesian-3d-cs.md), and the
reported multichannel `ecalib` and `pattern` cases in the
[task record](../tasks/tasks-bart-reconstruction-workflow.md). Existing
learning, development, debugging, and historical execution records are not
measurements under this protocol.

Ricardo approved the four pairs and counting rules in Task 9.2. Task 9.3
prepares the recording checklist. This protocol has not yet been applied to
measurement runs; it establishes no success threshold or result.

## 2. Approved matched cases and boundaries

In every pair, both routes use the same already-prepared synthetic input
identity, equivalent effective scientific settings, equivalent requested
outputs, the same local host, and the same BART build. Keep relevant resource
configuration comparable and record the actual OS/hardware, Python environment
for automation, BART version, and any known competing load, interruption, or
resource difference. Output directories may differ to keep runs separate. Do
not claim conditions were identical when they were not.

| Case | Proposed shared input and effective configuration | Route included in the count | Start and end of the measured run |
|---|---|---|---|
| Cartesian 2D | Prepared, fully sampled, single-channel 64 × 64 BART k-space. Centered, unitary inverse Fourier transform over spatial axes 0 and 1, as in the reviewed tutorial. | Manual BART inverse FFT versus one automated workflow invocation for the same reconstruction. | **Start:** first case-specific input/configuration review or run-configuration action, after tools and prepared data are ready. **End:** reconstruction output check and final review of the operation, check, effective settings, and operational record. |
| Cartesian 3D | Prepared, fully sampled, single-channel 64 × 64 × 64 BART k-space. Centered, unitary inverse Fourier transform over spatial axes 0, 1, and 2, as in the reviewed tutorial. | Manual BART inverse FFT versus one automated workflow invocation for the same reconstruction. | **Start:** first case-specific input/configuration review or run-configuration action, after tools and prepared data are ready. **End:** reconstruction output check and final review of the operation, check, effective settings, and operational record. |
| Cartesian 3D CS, original single-channel case | The prepared 64 × 64 × 64 single-channel undersampled BART k-space, supplied binary mask, and supplied constant sensitivity map. Use the reviewed `manual-cartesian-3d-cs` profile: FISTA, `dau2`, wavelet regularization on axes 0–2 with weight 0.01, 100 iterations, step 0.95, random shift disabled, and data scaling 1. Mask and sensitivity estimation are not part of this case. | Manual `pics` with the supplied mask and maps versus one automated workflow invocation with the same supplied inputs and profile. | **Start:** first case-specific input/configuration review or run-configuration action, after tools and prepared data are ready. **End:** reconstruction output check and final review of the operation, input/check results, effective settings, and operational record. |
| Cartesian 3D CS, multichannel extended case | Both routes start from the same prepared multichannel BART k-space (the reviewed synthetic case has eight channels). Do not supply a pre-generated mask or sensitivity maps to either route. Use BART `pattern`, check the resulting mask, run `ecalib` with calibration region 64:16:16, kernel 6:6:6, threshold 0.001, crop 0.8, and one ESPIRiT map set (`-m 1`); check the sensitivities, then run `pics` with the reviewed profile and effective settings listed above. | Manual `pattern` → mask check → `ecalib` → sensitivity check → `pics` versus one automated workflow invocation that performs those same stages. Pattern estimation and sensitivity estimation are included in both measured routes. | **Start:** immediately before the first case-specific configuration/input review or `pattern` operation, with tools and the same prepared multichannel k-space ready. **End:** after the reconstruction output check and final review of all stage results, effective settings, and operational record. The required mask and sensitivities must be obtained within this measured route. |

Use the settings already established in the linked procedures and reported
synthetic runs; do not infer new scientific values. Before the first measured
pair, record the exact input identity and the effective settings for both
routes, including the resolved `pics` profile values and the multichannel
calibration values. The `-m 1` setting selects one map set, not one channel:
the extended case remains multichannel. Multiple map sets are neither a case
nor a prerequisite for this measurement.

The measurement begins only after initial environment setup and synthetic
input generation are complete. It includes the case-specific configuration,
operations needed to obtain the requested outputs and checks, and operational
evidence recording. It excludes figures and comparisons against a reference;
this exclusion was approved in Task 9.2. The broader
[project context](./project-context.md) mentions runtime and memory as planned
secondary outcomes for a later evaluation. They are not required outcomes of
this operator-intervention protocol and are not proposed for measurement here.

## 3. Intervention unit and counting rules

Count observable human actions, not effort proxies. Each counted intervention
receives exactly one primary category:

1. **Configuration** — one independently performed edit-and-save transaction
   for a named run-configuration artifact or setting block. Before measurement,
   name the artifact/block for each run and record its planned fields. Multiple
   fields changed in the same transaction count once; a later independent
   edit-and-save transaction counts again. Do not combine separate transactions
   after seeing results. If all values are supplied directly in a single
   invocation and no separate configuration transaction occurs, that invocation
   has no additional configuration intervention.
2. **Execution** — one invocation or one previously defined block submitted
   once as a unit. A documented multi-line block submitted at once is one
   execution intervention, regardless of its line count. In the extended case,
   manual `pattern`, `ecalib`, and `pics` count as three interventions only
   when the operator submits them separately. If they are grouped in one
   previously defined block and submitted at once, they count as one.
   The automated workflow invocation counts as one; its internal calls and
   stages do not create additional human interventions. Fix the grouping
   before measuring and never change it retrospectively to favor either route.
3. **Check or review** — one independently launched human-operated check, or
   one of the fixed review blocks below. An automatically executed check is
   not a human review. If a person launches an independent check and later
   reviews its result as a separate action, count both once. Do not count the
   same action again as execution.
4. **Operational evidence recording** — one complete run-record
   assembly/save transaction per run when a person must gather, enter, copy,
   or preserve the required operational evidence. Define the record bundle
   before measuring; multiple fields or files gathered and saved together in
   that transaction count once. A separately saved required log/result outside
   that bundle is another recording intervention. Software-generated logs or
   records alone do not count. Do not count a save twice when it is already
   part of the submitted invocation or the defined record transaction.
5. **Correction** — one distinct human action that changes a setting or
   corrects a problem. Record the correction once in this category rather than
   counting that same action again as configuration or checking.
6. **Recovery** — one distinct human action to restore or resume a run after an
   interruption or failure, excluding any correction or invocation already
   counted separately. A recovery action is not the failed attempt itself.

An invocation's parameters do not automatically add configuration or decision
interventions. If parameters are entered in the same submitted invocation,
they are part of that single execution action. An independently edited and
saved configuration is a separate configuration intervention. Do not count
keystrokes, lines of code, time spent, or software-only operations.

### Fixed review blocks

The automated workflow validates intermediate results before running dependent
stages and proceeds or stops without requesting human intervention. These
internal validations are not human reviews. Do not add pauses to the
non-interactive program or require artificial interventions to equalize the
routes. Human review of automated results takes place after its invocation has
finished or stopped.

Before collecting counts, keep these human review blocks unchanged for both
routes:

- **Pre-run block (all cases):** one review of the prepared input identity,
  case route, output destination, and frozen effective configuration before
  the first reconstruction operation. For the original CS case, this also
  reviews the supplied mask and sensitivity inputs.
- **Final block (all cases):** one review of the requested output check,
  operation outcomes, effective settings, and available operational records
  after the route has finished or stopped. For the multichannel extended case,
  this block also reviews the `pattern` result and its mask check (dimensions,
  binary values, and consistency with prepared k-space), the `ecalib` result
  and sensitivity check (compatibility with the multichannel input and one
  map set), and the reconstruction result.

Human intermediate reviews in the manual procedure, if they are part of the
planned route and actually occur, are additional check/review interventions.
Their exact checkpoints must be defined before measurement in the Task 9.3
checklist. Do not require the automated route to pause for equivalent
intermediate human reviews.

Each listed review block is one intervention when performed. A separately
launched independent check is an additional check/review intervention. If the
operator must revisit a block later, record that as another intervention;
do not merge separate review visits. Software-only checks remain excluded
even when their results are available for human review.

## 4. Parameters and decisions recorded separately

Maintain a parameter record and a decision record separately from the
intervention record. Neither record is added to the intervention total.

- **Previously established values:** identify settings fixed by the reviewed
  synthetic procedure and the case-specific profile, separately from any
  values newly supplied during a run.
- **Operator-introduced values:** record the actual case/input selection,
  output destination, explicit invocation parameters, and any independently
  saved configuration. The fact that a value was introduced does not make it
  an additional intervention if it was part of an already-counted invocation
  or configuration transaction.
- **Profile-resolved values:** record the selected profile and every effective
  value it resolves to. Software resolution is not an intervention; selecting
  a profile within an invocation is part of that invocation.
- **Decisions actually made:** record the selected route and input source,
  whether mask/maps are supplied or produced within the route, whether any
  correction or recovery was chosen, and any deviation from the frozen
  procedure. Record the decision even when it coincides with a counted
  configuration or execution action, but do not add it again to the count.

If a value or decision differs from the approved plan, preserve the original
attempt and record the reason and action. Do not silently substitute a
favorable attempt or retrospectively redefine a configuration, execution, or
review block.

## 5. Failures, corrections, recovery, and exclusions

Retain every intervention that produces a failure. Record the failed operation
or check and its result separately from any correction and recovery actions.
A failed invocation still counts once as an execution intervention. A later
invocation is another execution intervention; a separate parameter/configuration
change is counted once as a correction, and any further distinct recovery
action is counted once as recovery. Do not assign one human action to multiple
categories.

Exclude:

- prior learning;
- development and debugging;
- initial tool/environment setup;
- prior synthetic-input generation;
- software-only operations, including automatic checks and internal wrapper
  calls;
- actions performed only to annotate or calculate the study's intervention
  count.

The preparation exclusion does not apply to `pattern` estimation or
`ecalib` in the multichannel extended case. Those operations and their required
checks are inside the measured route.

Distinguish ordinary operational evidence from study-only annotation.
Preserving a required log, result, or run record is operational evidence and
counts when it requires a human action under the recording rule above.
Transcribing counts into the study's analysis table is study-only annotation
and is excluded.

## 6. Equivalent operational evidence

The file formats may differ between routes, but retain equivalent information
for each run:

- case and route identity, prepared input identity, and output identity;
- actual commands/invocations and associated logs, selected profile,
  operator-entered settings, and effective settings (including
  profile-resolved values);
- software and local environment information needed to identify the run;
- each required operation and check result, kept distinct;
- requested and produced outputs;
- failures, corrections, recovery actions, and deviations;

Before measurement, define the run-record bundle as the complete set of
information listed above for one run. If a person assembles and saves that
bundle as one transaction, count one operational-evidence intervention. If
required artifacts must be saved separately outside that transaction, count
each distinct human save once. This is the operational run record, not the
study-only count worksheet. Preserve original logs and failed-attempt evidence;
do not treat absent outputs or records as success. The two routes must retain
comparable information even when one writes structured stage records and the
other uses command logs and separate check records.

Keep the intervention record as separate study documentation, outside the
operational run-record bundle. Its preparation and the calculation or
transcription of intervention totals are excluded from the intervention count,
as specified in Section 5.

## 7. Approved outcomes and interpretation

For each matched case, report manual and automated intervention counts by
primary category, then:

- **Manual total:** `M`.
- **Automated total:** `A`.
- **Signed difference:** `M - A` (positive, zero, or negative).
- **Percentage reduction:** `100 × (M - A) / M`, only when `M > 0`; otherwise
  report it as not applicable.
- **Separately identified incidents:** failures, corrections, and recovery
  actions, with their records and without counting any action twice.

The signed difference may be zero or negative; do not change counting rules
based on the result. Do not define a success threshold. One matched pair per
case is a descriptive observation of those executions only; it establishes
neither causality nor a general advantage for users, operators, or acquisitions.

## 8. Task 9.2 approval record

Ricardo explicitly approved this protocol on 2026-11-24. The approval covers:

- the four cases and one matched manual–automated pair per case;
- each route's measurement boundaries and comparable local conditions;
- counting observable human actions, with invocation/block grouping fixed
  before measurement;
- one human pre-run review and one human final review for both routes, with
  planned manual intermediate reviews recorded when they occur;
- separating operational run records from study annotations;
- retaining and separately identifying failures, corrections, and recovery;
- the stated exclusions and comparison formulas, without assuming a reduction
  or setting a success threshold.

The protocol is approved for preparing the checklist and future measurements.
This approval does not mean that any measurement run has been performed.
