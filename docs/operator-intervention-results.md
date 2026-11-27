# Operator Intervention Results

## 1. Purpose and scope

This report records the results of Task 9.5, **Calculate and review
operator-intervention outcomes**, using Ricardo's reported executions and
subsequent confirmations under the approved
[operator-intervention protocol](./operator-intervention-protocol.md) and
[recording checklist](./operator-intervention-checklist.md).

Across four paired synthetic cases, counted operator actions decreased from
**26 for the prescribed manual procedures to 12 for the automated workflows**:
**14 fewer actions, or a 53.85% aggregate reduction**. This result measures
action counts within the defined protocol. Operator time, computational
resource use, and reconstruction-quality equivalence were not measured by
this comparison.

There was one reported manual execution and one reported automated execution
for each case in the same local macOS environment with BART v1.0.00. The cases
were fully sampled Cartesian 2D, fully sampled Cartesian 3D, the original
single-channel Cartesian 3D CS example, and an extended Cartesian 3D CS case
with eight channels, sampling-pattern estimation, and ESPIRiT calibration with
one map set.

## 2. Counting and calculation method

An intervention is one submitted operation or check block, or one fixed human
review, as defined before measurement. It is not an individual keystroke,
shell line, chat message, or internal software operation.

The counts include the prescribed pre-run and final reviews in both routes.
They also include separately submitted manual directory creation, BART
invocations, output checks, and intermediate reviews when applicable. Internal
workflow operations and checks add no separate human interventions.

One-time setup, prior synthetic-data preparation, learning and development,
and study-ledger annotation are excluded. No separate configuration-edit or
operational-evidence-preservation actions were reported in these runs; the
submitted invocation blocks supplied the settings and retained the records.

For manual count **M** and automated count **A**, with M greater than zero:

```text
Absolute reduction   = M - A
Percentage reduction = 100 × (M - A) / M
```

The aggregate percentage uses the totals across cases. It is not the simple
average of the four case percentages. Displayed percentages are rounded to
two decimal places; the workbook retains the unrounded calculations.

## 3. Results

| Case | Manual, M | Automated, A | Difference, M − A | Reduction |
|---|---:|---:|---:|---:|
| Cartesian 2D | 5 | 3 | 2 | 40.00% |
| Cartesian 3D | 5 | 3 | 2 | 40.00% |
| Cartesian 3D CS original | 5 | 3 | 2 | 40.00% |
| Cartesian 3D CS multichannel, with `pattern` and `ecalib` | 11 | 3 | 8 | 72.73% |
| **All four pairs** | **26** | **12** | **14** | **53.85%** |

The aggregate calculation is `100 × (26 − 12) / 26`.

## 4. Where the counts come from

### 4.1 First three cases: five manual actions versus three automated actions

Each of the first three manual routes had the following five counted actions:

1. Review the inputs, destination, route, and frozen settings before execution.
2. Create the manual run directory through the separate directory block.
3. Invoke BART for reconstruction.
4. Launch the independent reconstruction-output check.
5. Review the final execution records.

Each corresponding automated route had three counted actions:

1. Perform the pre-run review.
2. Invoke the complete workflow.
3. Review the final execution records.

Directory creation and output checking occur inside the automated invocation.
They therefore do not require additional operator submissions in this
procedure.

### 4.2 Extended multichannel case: eleven manual actions versus three automated actions

| Manual action | Count |
|---|---:|
| Pre-run review | 1 |
| Separate run-directory creation | 1 |
| BART invocations: `pattern`, `ecalib`, and `pics` | 3 |
| Independent checks: `CHK1`, `CHK2`, and `CHK3` | 3 |
| Intermediate reviews: `MID1` and `MID2` | 2 |
| Final review | 1 |
| **Total** | **11** |

The automated route retained **three human actions**: pre-run review,
complete-workflow invocation, and final review. The program coordinated the
sampling-pattern estimation, calibration, reconstruction, and intermediate
checks within that invocation.

This case had the largest observed reduction: eight actions, or 72.73%.
Adding `pattern` and `ecalib` increased the number of operations and checks
that the prescribed manual procedure required the operator to coordinate,
while the automated entry remained one invocation.

### 4.3 Totals by counted action category

| Category | Manual | Automated |
|---|---:|---:|
| Execution | 10 | 4 |
| Check or review | 16 | 8 |
| Separate configuration actions | 0 | 0 |
| Separate operational-evidence recording actions | 0 | 0 |
| Manual correction actions | 0 | 0 |
| Recovery actions | 0 | 0 |
| **Counted human actions** | **26** | **12** |

No failures, manual corrections, or recovery actions were reported during
these measurement runs. A zero for a separate-action category means that no
such additional action was reported; it is not a claim about unobserved
activity.

## 5. Evidence and provenance

The [calculation workbook](./operator-intervention-results.xlsx)
contains two sheets:

- **Results:** formula-based case and category totals, absolute differences,
  percentage reductions, and counting notes.
- **Actions:** the 58-row evidence ledger, including action identifiers,
  categories, reported outcomes, evidence references, provenance notes, and
  a formula-derived count for each row.

Of the **38 counted human actions**, 28 are labelled `DOCUMENTED` from the
shared execution and review records, and 10 are labelled `OWNER_CONFIRMED`.
The latter comprise all eight pre-run reviews plus the manual directory
creation actions for Cartesian 3D and the original Cartesian 3D CS case.
Ricardo confirmed these after execution. This preserves their retrospective
confirmation status rather than claiming independent contemporaneous
observation.

The remaining 20 ledger rows describe 16 conditional actions for which no
separate action was reported and four software-only rows. They contribute
zero to the human-action totals. The workbook exposes an unresolved counted
action as `Pending` rather than silently treating it as zero.

The evidence retains gaps in numeric status transcription. In particular,
numeric directory-creation exit codes were not separately transcribed for
`C3D-M-DIR`, `CSO-M-DIR`, or `CSX-M-DIR`. The global Python-workflow exit codes
for the Cartesian 3D and original Cartesian 3D CS automated runs were not
separately transcribed, although their reported BART and stage records contain
successful results. No missing numeric code is manufactured from the
existence of an output file. These gaps do not remove the documented or
confirmed operator actions from the count.

The original run evidence is retained under Ricardo's local measurement root:

```text
$HOME/bart-learning/bart-workflow-reconstructions/operator-intervention-measurements/
```

| Case directory | Manual run | Automated run |
|---|---|---|
| `cartesian-2d` | `manual-01/` | `automated-01/` |
| `cartesian-3d` | `manual-01/` | `automated-01/` |
| `cartesian-3d-cs-original` | `manual-01/` | `automated-01/` |
| `cartesian-3d-cs-multichannel` | `manual-01/` | `automated-01/` |

Relevant records include BART headers, reconstruction logs, manual check
reports, automated `stage-records.json`, and the automated console log
`automated-01-workflow.log` beside each automated run directory. The extended
case also preserves pattern, sensitivity, and eigenvalue outputs and their
checks. The workbook retains the specific source references. Referencing
these paths does not mean that the original local logs or BART data are
bundled with this report.

## 6. Interpretation and limits

The results support a descriptive observation for these four paired cases:
the automated workflow required fewer operator actions under the approved
counting rules, with the largest reduction in the extended multichannel
procedure.

The magnitude depends on the fixed action granularity, including separate
manual directory creation, checks, and intermediate reviews. It should not be
presented as independent of those procedural choices. There was only one
pair per case, with no statistical analysis or repeated-trial estimate.

The experiment does not quantify elapsed time, operator effort, cognitive
load, or computational resource savings. Comparable competing system load
was not independently measured. It does not establish general causal
effects, compatibility with every acquisition, or successful ARC execution.

Reconstruction-to-reference evaluations and manual–automated output
comparisons are separate evidence. This intervention report does not impose
a new scientific tolerance or use action counts as a measure of image
quality.

## 7. Attribution and related records

Ricardo executed and reviewed the runs and supplied the evidence and
follow-up confirmations. ChatGPT consolidated the ledger into this report
and workbook and verified their arithmetic. Creating these artifacts did
not require a new BART reconstruction or a new measurement run.

- [Approved measurement protocol](./operator-intervention-protocol.md)
- [Measurement checklist](./operator-intervention-checklist.md)
- [Calculation workbook](./operator-intervention-results.xlsx)
- [Project task list](../tasks/tasks-bart-reconstruction-workflow.md)
