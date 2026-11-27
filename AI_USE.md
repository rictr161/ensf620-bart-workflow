# AI Use Record

This file records material AI assistance, the information used, review decisions
and the evidence available for each activity. The entries describe what was known
at their respective checkpoints. Current project status is summarized in the
[README](README.md#current-status); AI access and authority are defined by the
[accepted contract](docs/DATA_CONTRACT.md) and its
[decision register](docs/DATA_CONTRACT_DECISIONS.md). Collaboration guidance is
maintained in the [Copilot instructions](.github/copilot-instructions.md) and
[handoff](docs/copilot-handoff.md).

Entries use the same eight fields and are ordered by record date, newest first.
A consolidation date can cover earlier activities. Entries with the same date do
not establish an execution order. The blank form at the end is a template, not
an activity record.

## 2026-11-26 — Final delivery evidence consolidation

**Date:** Prepared on 2026-11-26.

**Tool/model and access mode:** Copilot in VS Code consolidated owner-supplied
execution reports and authorized repository documentation. No laboratory
files or private execution records were accessed.

**Inputs:** Ricardo's report of local acquired-data runs, a clean separated
local Python environment, one ARC Slurm execution, transfer of its BART output
pair, and successful local visual review. The ARC script configuration and
the repository's existing synthetic, comparison, and operator-intervention
records were used as context.

**Assistance and affected files:** Ricardo prepared the environments, ran the
local commands and ARC job, transferred the output files, and reviewed the
reconstruction. ChatGPT explained the workflow, prepared instructions, and
guided the checks. Copilot consolidated the documentation in
`docs/environment-validation-results.md`, `tasks/tasks-bart-reconstruction-workflow.md`,
`tasks/prd-bart-reconstruction-workflow.md`, `README.md`, `docs/project-context.md`,
`docs/copilot-handoff.md`, `docs/input-inventory.md`, `docs/open-questions.md`,
`docs/data-and-ai-boundaries.md`, `docs/python-automation-behavior.md`,
`docs/tutorials/automated-cartesian-workflow.md`, `src/README.md`,
`configs/README.md`, `environment/README.md`, and `environment/local-macos.md`,
and added this record.

**Corrections and decisions:** The approved delivery scope includes the
documented synthetic and comparison evidence in Blocks 7–9, owner-reported
local use with acquired BART inputs, use from a separate clean local Python
environment with the existing BART installation, one ARC Slurm run for one
volume, and download and local visual review of its reconstruction pair.
Batch processing of all laboratory data, multiple ESPIRiT map sets, 2D CS,
and non-Cartesian trajectories remain outside this delivery. Scripted ARC
settings are distinguished from execution records; no unprovided status,
resource, version, or revision values were inferred.

**Execution and evidence:** Copilot made documentation-only changes. No
reconstruction, project Python, installation, or experimental test was run.
Read-only Git status, diff, and whitespace checks were used to prepare the
documentation review; the results are reported in the session response.

**Limitations:** Local and ARC execution details are owner-reported. No
numeric exit codes, Slurm ID, resource measurements, effective ARC versions,
or per-run Git revisions are claimed. No Mac-to-ARC output equivalence,
general input validation, image-quality acceptance, or ground-truth comparison
is established. The owner-reported “listo todo perfecto” refers to the ARC
pair download and local visual review.

## 2026-11-26 — Reusable interactive slice viewer

**Date:** Prepared on 2026-11-26.

**Tool/model and access mode:** Copilot reviewed authorized repository
source and documentation and prepared a separate local viewer. Exact model
identifiers were not recorded.

**Inputs:** The accepted access policy, project instructions, existing BART
reader, interactive manual-tutorial appendices, workflow and environment
documentation, and task status. No laboratory data or private execution
records were accessed.

**Assistance and affected files:** Copilot added `src/view_bart_slices.py`
and updated the automated workflow tutorial, the two 3D tutorial appendices,
`src/README.md`, and this record.

**Corrections and decisions:** The viewer is separate from the non-interactive
reconstruction workflow, reads a user-supplied BART base path, supports
scalar 2D/3D arrays and optional user-supplied voxel spacing, and does not
run BART or generate outputs. Existing reference-comparison blocks remain
unchanged. No task status was changed.

**Execution and evidence:** No commands, Python, tests, BART, installations,
or GUI windows were run or opened for this change.

**Review and related revision:** The reader interface and the existing
appendices were reviewed by reading the repository files; the new code and
documentation were reviewed statically. No reconstruction or GUI behavior is
claimed as verified by execution.

**Limitations:** At the time this entry was prepared, Ricardo still needed to
review and run focused synthetic checks, including GUI availability, axis
navigation, singleton slices, spacing, invalid inputs, and error handling.
Clean-checkout usage and ARC were not verified at that checkpoint; Blocks 7–9
were closed and Block 10 remained open then. The later Block 10 closure and
owner-reported ARC use are recorded separately above.

## 2026-11-24 — Automated Cartesian workflow tutorial

**Date:** Prepared on 2026-11-24.

**Tool/model and access mode:** Copilot reviewed repository source and
documentation and drafted user-facing documentation. No commands, Python,
BART, tests, installations, or Git operations were performed. Exact model
identifiers were not recorded.

**Inputs:** `src/bart_workflow.py`, `src/README.md`, the project README, the
automation task record, the local macOS and BART environment records, the
synthetic 2D procedure, and existing synthetic execution reports.

**Assistance and affected files:** Copilot created
`docs/tutorials/automated-cartesian-workflow.md` and updated `README.md`,
`tasks/tasks-bart-reconstruction-workflow.md`, and this record. The
implementation, tutorials describing manual procedures, PRD, parameters, and
execution records were not changed.

**Corrections and decisions:** The guide documents the four routes and their
actual CLI arguments, input validation limits, profile behavior, outputs,
logs, and failure handling as found in the current source. It distinguishes
coil channels from ESPIRiT map sets, identifies the profile as a synthetic
example, and does not make a reference comparison part of reconstruction.

**Execution and evidence:** The guide's sample invocations were not executed.
This documentation work adds no new reconstruction, comparison, or ARC
execution evidence.

**Review and related revision:** CLI names, accepted values, defaults,
configuration validation, BART command construction, stage records, and
output paths were checked by reading the implementation and existing
documentation. The README and Task 7.6 note link the guide while distinguishing
document drafting from execution of its examples.

**Limitations:** The existence and readiness of the local synthetic input
pairs and new output destinations were not checked. The guide does not verify
acquired-data suitability, clean-checkout reproduction, ARC execution, or
laboratory batch processing.

## 2026-11-24 — Operator-intervention measurement closure

**Date:** Consolidated on 2026-11-24 from Ricardo's reported execution evidence,
follow-up confirmations, and the existing results artifacts.

**Tool/model and access mode:** Copilot reviewed the authorized repository
documents and consolidated the task records. ChatGPT guided the checks and
prepared the results report, workbook, and calculations. Ricardo executed,
reviewed, and confirmed the actions. No commands, Python, BART, tests,
installations, or Git operations were performed for this documentary
consolidation. Exact model identifiers were not recorded.

**Inputs:** Block 9 of the task list; the intervention results report and
workbook; the approved protocol and checklist; Task 4.6 evidence and the
manual Cartesian 2D tutorial; and the recent AI-use record format. Only
repository documents were consulted.

**Assistance and affected files:** Copilot updated
`tasks/tasks-bart-reconstruction-workflow.md`,
`docs/operator-intervention-results.md`, and this record. The report's two
workbook links now point to the existing workbook directly under `docs/`;
neither the workbook nor its location was changed.

**Corrections and decisions:** Tasks 9.0–9.6 are recorded complete. Task 9.4
attributes the eight reported executions and associated reviews to Ricardo.
Task 9.5 preserves the reported case and aggregate action counts and links the
results report. Task 9.6 cites the earlier 2D tutorial evidence. Untranscribed
numeric exit codes remain unspecified.

**Execution and evidence:** The repository report records four manual–automated
pairs, with totals of 26 manual and 12 automated actions, a difference of 14,
and a 53.85% aggregate reduction. Its 58-row ledger contains 38 counted actions:
28 documented and 10 subsequently confirmed by Ricardo. This consolidation
performed no reconstruction or new measurement.

**Review and related revision:** The action-count results were checked against
the approved protocol and checklist. Task 4.6 and the tutorial support the
finding that the initial 2D tutorial and preliminary comparison were completed
independently of the later intervention protocol. The Excel file's repository
location was confirmed as `docs/operator-intervention-results.xlsx`.

**Limitations:** The results describe action counts under the approved
protocol only; they do not establish time savings, image quality, causality,
general advantage, or ARC performance. The report retains the missing numeric
status transcriptions and the retrospective confirmation status of ten
counted actions. No local measurement directories were accessed.

## 2026-11-24 — Manual–automated route comparison and Block 8 closure

**Date:** Consolidated on 2026-11-24 from Ricardo's explicit approvals and his
report of direct visual inspection of the three preserved manual–automated
pairs.

**Tool/model and access mode:** Copilot reviewed the authorized task and
behavior records and consolidated the documentation. ChatGPT reviewed the
header contents and results Ricardo shared, guided the visual inspection, and
prepared the instruction for this update. Ricardo executed the procedures and
checks reported in the existing records and inspected the figures. Copilot did
not access the local reconstruction directories or open the figures. No
commands, Python, BART, tests, installations, or Git operations were run for
this documentary update. Exact model identifiers were not recorded.

**Inputs:** Ricardo's explicit approvals of the Task 8.2 conditions and Task
8.4 binary method; his report of `cmp` code `0` for all three historical
`reconstruction.cfl` pairs; the contents and comparison of all six
reconstruction headers; and his direct visual observations and the supplied
figure locations. Existing Task 7.8, Task 7.11, and behavior records were
consulted. No local execution files or figures were opened or copied into the
repository.

**Assistance and affected files:** Copilot updated
`docs/python-automation-behavior.md`, `tasks/tasks-bart-reconstruction-workflow.md`,
and this record. No code, reconstruction parameter, PRD, tutorial, README, or
local execution record was changed.

**Corrections and decisions:** Tasks 8.4–8.7 and Block 8.0 are recorded
complete. The three historical `.cfl` comparisons remain identified as
pre-Block 8 executions reused transparently under the approved conditions and
method; they are not described as new comparisons. Ricardo's current visual
inspection of the manual and automated reconstruction panels is recorded
separately. The original single-channel CS case with supplied sensitivities is
the Block 8 case; the multichannel `ecalib` and automated-to-automated
sampling-variant cases remain separate. The automatic workflow operator guide
remains future work.

**Execution and evidence:** Ricardo reported that the six headers declare
matching dimensions for each pair: `64 × 64` for 2D and `64 × 64 × 64` for 3D
and CS, with later axes singleton. The corresponding header commands identify
`fft -i -u 3`, `fft -i -u 7`, and, for CS,
`--fista --wavelet dau2 -R W:7:0:0.01 -i 100 -s 0.95 -n`, with `-w 1`
manually and `-w 1.0` automatically. The three cases use their documented
shared preparations; CS uses the same `mask3d` and `sensitivities`. All six
headers declare `BART v1.0.00` in `# Creator`; expected manual/automated output
paths differ in `# Command` and `# Files`. Ricardo's earlier `cmp` results for
the three `.cfl` pairs were each code `0`. He also reported no visible
differences between the manual and automated panels in the displayed figures
for all cases; the 3D observations concern the displayed central planes.

**Review and related revision:** The task review confirms each pair's shared
inputs, effective configuration, requested and produced outputs, structural
checks, historical binary result, header interpretation, visual observation,
and limits are recorded. The automated command arrays and effective settings
are available in the previously shared `reconstruction.log` and
`stage-records.json` records. Header-declared BART version is not treated as a
complete runtime-environment record. Task 7.11 reference evaluations and
observations remain distinct from the direct route comparison.

**Limitations:** The binary comparisons are historical and predate prospective
Block 8 approval. The visual observation covers only the views shown, not every
3D or CS slice. No manual–automated L2 error, tolerance, scientific acceptance,
or operator-intervention measurement is claimed. Original Python CLI strings,
per-run repository revisions, and a complete runtime-environment record for
the earlier runs are not established here.

## 2026-11-23 — Automated synthetic reference evaluations and Block 7 review

**Date:** Later consolidation on 2026-11-23 from Ricardo's report of visual and
quantitative evaluations for the three synthetic automated reconstructions.
Earlier records dated the same day preserve their own checkpoint status.

**Tool/model and access mode:** Copilot consolidated the documentation and
reviewed the task evidence. ChatGPT reviewed the reported results, guided the
executions, and prepared the instruction for this update. Ricardo executed the
tutorial comparison blocks and inspected the figures. Copilot did not access
the local evaluation directories. No Python, BART, test, installation, or Git
command was run for this documentary update. Exact model identifiers were not
recorded.

**Inputs:** Ricardo's reported comparison errors, command results, visual
observations, environment versions, display-limit diagnostics, and local
evaluation-directory names, together with the existing Task 7.10 proposal and
project documentation. No evaluation data, logs, or figures were copied into
the repository.

**Assistance and affected files:** Copilot updated
`tasks/tasks-bart-reconstruction-workflow.md`,
`docs/python-automation-behavior.md`, `src/README.md`, `README.md`, and this
record. No code, parameters, tutorials, PRD, or local execution records were
changed.

**Corrections and decisions:** The evaluations are described as use of the
existing tutorial blocks on the existing automatic reconstructions, not as a
new comparison CLI or an integrated `bart_workflow.py` operation. Task 7.11
records Ricardo's execution and review; Task 7.12 records the evidence review.
Block 7.0 is complete because Tasks 7.1–7.12 are complete. Tasks 8.0 onward
remain open, and `docs/automated-workflow.md` remains a future guide that has
not been created. Reference comparison remains optional for reconstruction;
no reference is fabricated for real acquisitions.

**Execution and evidence:** Ricardo reported using the existing reference and
automated reconstruction pairs for Cartesian 2D, Cartesian 3D, and the original
single-channel Cartesian 3D CS case. The evaluation root is
`$HOME/bart-learning/bart-workflow-reconstructions/automated-reference-evaluations`:
`cartesian-2d-TAT46E` recorded relative L2 error `1.442448308e-07`,
`cartesian-3d-EqHsLn` recorded `1.729089800e-07`, and
`cartesian-3d-cs-hBicqH` recorded `2.473308708e-01`. Each calculation and
figure-generation code was `0`. Each directory contains
`quantitative-comparison.txt`, `visual-comparison.log`, and the corresponding
figure under `figures-visual/`. Records report Python `3.13.17`, NumPy `2.5.4`,
and Matplotlib `3.11.2`. Ricardo reported no evident visual differences for
2D and 3D; for CS he observed a noisier appearance than the reference and an
appearance similar to the manual result. Display limits were `1` for 2D and
`2` for 3D and CS; the 3D log records small exceedances in each displayed
cut, and the CS reconstruction global maximum was `2.851191679`. These
warnings did not change figure-generation codes. Results match the previously
reported manual-to-reference errors at the displayed precision. They remain
separate from the earlier manual-to-automated binary identity comparisons.

**Review and related revision:** The task review confirms that the three
automated-to-reference evaluations are documented separately from manual
reference results and manual-to-automated `.cfl` comparisons, with all reported
calculation and figure-generation codes recorded. No failures were reported.

**Limitations:** The results are case-specific. Human observations concern
only the reviewed figures, not every slice, and are not scientific acceptance.
No tolerance, quality threshold, general validation, ARC execution, or
multichannel `ecalib` reference comparison is established. The local evaluation
data, figures, and records remain outside the repository.

## 2026-11-23 — Automated pattern/`ecalib` evidence and Task 7.7–7.9 review

**Date:** Consolidated on 2026-11-23 from Ricardo's report of the automated
Cartesian 3D CS `bart-pattern`/`ecalib` run and his reconstruction-file
comparison.

**Tool/model and access mode:** Copilot applied this documentation
consolidation; the earlier code implementation is recorded in prior entries.
ChatGPT performed the static review, reviewed the logs and
`stage-records.json` shared by Ricardo, and guided the checks. Ricardo executed
the commands and supplied the reported results. Copilot did not access the
local execution directory. No Python, BART, test, installation, or Git command
was run during this documentary update. Exact model identifiers were not
recorded.

**Inputs:** Ricardo's supplied run configuration, log and stage-record
summaries, `cmp` result, and the existing task, source, behavior, and project
status documentation. No experimental data or additional local files were
accessed.

**Assistance and affected files:** Copilot updated
`tasks/tasks-bart-reconstruction-workflow.md`, `src/README.md`,
`docs/python-automation-behavior.md`, the directly outdated status in
`README.md`, and this record. No implementation, parameter, or local record was
changed.

**Corrections and decisions:** The new `bart-pattern`/`ecalib` run is recorded
as case-specific execution evidence. Its reconstruction `cmp` is explicitly
identified as automated-to-automated, not manual-to-automated or
reference-based. The 7.7 matrix separates static review from Ricardo's
execution evidence. Tasks 7.7, 7.8, and 7.9 are marked complete against their
current criteria; Tasks 7.10–7.12 and the overall 7.0 block remain open.

**Execution and evidence:** Ricardo reported BART `version -V`, `pattern`,
`ecalib`, and `pics` exit codes of `0`; all 11 stages reported `success` and
code `0`. He reported a successful structural output check, effective CS
settings, BART/Python/NumPy/platform versions, and a successful figure record
for `figures/reconstruction.png`. Log-write error fields were reported as
`null`. The global CLI exit code was not provided. Ricardo's `cmp` returned
`0` between `reconstruction.cfl` files in the prior supplied-mask automated
run and the new pattern-estimated automated run. No new human visual review of
the figure was reported.

**Review and related revision:** Static review covered explicit sampling-source
guards, validation before calibration, use of the same effective mask by
`pics`, runtime environment/version association, output-directory protections,
and optional non-interactive figures. Pylance's successful static check is
recorded separately from Ricardo's executions. The review also retained
historical direct manual-to-automated comparisons for the three delivery cases
and for the earlier multichannel `ecalib` case.

**Limitations:** Results are limited to the reported synthetic runs. The new
automated-to-automated `cmp` is not a manual or reference comparison. No global
CLI result or new visual inspection is claimed. This work does not establish
scientific quality, general compatibility, or ARC execution; Tasks 7.10–7.12
remain subsequent work.

## 2026-11-23 — Runtime environment and software-version records

**Date:** Consolidated on 2026-11-23 from Ricardo's request to add runtime
environment and software-version records to the existing BART workflow.

**Tool/model and access mode:** Copilot edited the workflow and documentation.
ChatGPT statically reviewed the changes. No Python, BART, test, installation, or
Git command was run. Pylance diagnostics for `src/bart_workflow.py` reported no
errors. Exact model identifiers were not recorded.

**Inputs:** The reviewed workflow and directly related documentation, the
approved sampling-source and optional-figure behavior, and the task-planning
record. No local execution directory, experimental file, or private input was
accessed by the assistant.

**Assistance and affected files:** Copilot updated `src/bart_workflow.py`,
`src/README.md`, `docs/python-automation-behavior.md`,
`tasks/tasks-bart-reconstruction-workflow.md`, `README.md`,
`docs/project-context.md`, `docs/copilot-handoff.md`, and this record. The final
operator guide `docs/automated-workflow.md` remains planned and was not created.

**Corrections and decisions:** After k-space validation, the
`runtime-environment` stage records the active Python executable/version,
imported NumPy version, operating-system details and architecture, and configured
BART executable. It queries that exact executable with `version -V`, records
the command, exit code and response, and requires `bart-version.log`; a query or
log-write failure stops dependent processing and is recorded without claiming
an unsaved log. Matplotlib's version is captured only when the optional figure
path imports it. The module description now accurately distinguishes pattern
estimation from phantom generation or retrospective undersampling. Task 7.6 is
marked complete based on implementation review; Tasks 7.7 and 7.8 remain open,
and no later comparison task was advanced.

**Execution and evidence:** No runtime execution was performed. In particular,
the new BART version query and the automated `bart-pattern` route have not been
run in this update. Previously reported executions predate the new
runtime-environment stage and were not changed or presented as evidence for it.

**Review and related revision:** Static review covered stage ordering, use of
the configured BART executable without resolving away its configured spelling,
captured command output, mandatory-log and protected-stage-record handling,
optional Matplotlib import/version capture, and updated status descriptions.
Pylance diagnostics reported no errors; this is static evidence only.

**Limitations:** The implementation has not been exercised after this change.
Task 7.7 static-check coverage and Task 7.8 owner-run execution review remain
pending. This update establishes neither ARC compatibility nor scientific
reconstruction acceptance. The final operator guide remains planned until the
interface is settled.

## 2026-11-23 — Explicit BART sampling-source implementation

**Date:** Consolidated on 2026-11-23 from Ricardo's request to add an explicit
sampling-information source to the existing Cartesian 3D CS workflow and from
his report of a manual BART `pattern` check.

**Tool/model and access mode:** Copilot edited the workflow and documentation.
ChatGPT statically reviewed the implementation and guided the changes.
Ricardo supplied the manual-check evidence. No Python, BART, test, install, or
Git command was run during this update. Exact model identifiers were not
recorded.

**Inputs:** The existing workflow and documentation, Ricardo's scope decisions,
and his report for `generation-3d-ecalib-01/kspace_undersampled` and
`sampling-check-CCWi6Z/sampling_mask`. No local execution directory or file
was accessed by the assistant.

**Assistance and affected files:** Copilot updated `src/bart_workflow.py`,
`src/README.md`, `docs/python-automation-behavior.md`,
`tasks/tasks-bart-reconstruction-workflow.md`, and this record. The final
`docs/automated-workflow.md` guide remains planned for after the command-line
interface is settled; it was not created in this update.

**Corrections and decisions:** The CLI and reusable configuration now select
`provided` or `bart-pattern`, defaulting to `provided`. An explicitly selected
pattern is estimated from the same inspected k-space used downstream; invalid
provided masks do not trigger fallback estimation. The generated pair is
validated before the calibration-region check and reconstruction, and the
same effective mask is used by `ecalib` and `pics`. The feature is documented
as estimation of nonzero k-space support, with exact-zero and all-channel-zero
limitations. Cartesian 2D CS, radial, and multiple map sets remain outside
delivery scope.

**Execution and evidence:** Ricardo reported manually running
`bart pattern <kspace_undersampled> <sampling_mask>` with BART v1.0.00. The
reported output header declares `64 64 64`, later axes singleton, and creator
`BART v1.0.00`. `cmp` between the generated mask `.cfl` and the known
`generation-3d-cs-01/mask3d` `.cfl` returned `0`. Ricardo did not provide the
`bart pattern` process exit code. This manual command and comparison do not
establish execution of the automated `--sampling-source bart-pattern` route.

**Review and related revision:** Static review covered explicit option
validation, mask estimation before mask checks and `ecalib`, shared use of the
effective mask, the mandatory log and stage-result handling, and documentation
of requested versus effective settings. No execution-based verification was
performed.

**Limitations:** The automated pattern route remains to be executed and
reviewed under Task 7.8. The implementation does not yet explicitly record
effective software versions and execution environment as specified by the
portability objective. Task 7.6 remains partial for that concrete gap; it is
not being held open solely for the Task 7.8 execution. The final operator guide
is deferred until the interface is settled.

## 2026-11-23 — Optional reconstruction figure execution evidence

**Date:** Consolidated on 2026-11-23 from Ricardo's report of local 2D and 3D
figure-enabled executions and visual review.

**Tool/model and access mode:** Copilot implemented the optional figure
generation in the existing workflow. ChatGPT statically reviewed the
implementation and guided the checks. Ricardo executed the commands and
reviewed the generated figures. Exact model identifiers were not recorded.

**Inputs:** Ricardo's reported runs to `automated-2d-figures-01` and
`automated-3d-figures-01`, including their `stage-records.json` summaries and
visual review. The assistant did not access the local run directories or
generated files.

**Assistance and affected files:** Copilot updated `src/README.md`,
`tasks/tasks-bart-reconstruction-workflow.md`, and this record to consolidate
the reported evidence. No code, tutorial, parameter, or local execution record
was modified during this documentation update.

**Corrections and decisions:** The earlier statement that execution of
`--save-figures` remained pending is superseded by Ricardo's reported normal
2D and 3D runs. The task states and delivery scope, including the exclusion of
Cartesian 2D CS, remain unchanged.

**Execution and evidence:** Ricardo reported that both full workflow
invocations with `--save-figures` returned global exit code `0`. Each
`stage-records.json` records `reconstruction-figure` with status `success`,
exit code `0`, and `figures/reconstruction.png` within its run directory. The
2D figure displays the full 64 × 64 image. The 3D figure displays three
central planes of a 64 × 64 × 64 volume at indices `[32, 32, 32]`. The records
include magnitude scale and presentation settings. Ricardo confirmed that
both visualizations function correctly.

**Review and related revision:** ChatGPT performed static review and guided
the checks; Ricardo executed and reviewed the outputs; Copilot implemented
the option and applied this documentary consolidation. The behavior note was
reviewed and left unchanged because it contains no stale implementation or
execution-status claim.

**Limitations:** This is owner-reported local evidence for normal figure
generation in two FFT cases. It does not establish every error path, reference
comparison, scientific quality acceptance, or completion of the automation
block. Task 7 remains open.

## 2026-11-23 — December delivery scope adjustment

**Date:** Recorded on 2026-11-23 from Ricardo's decision to remove Cartesian
2D compressed sensing from the December 1, 2026 delivery scope.

**Tool/model and access mode:** Ricardo supplied the scope decision and
identified the published base as commit `713db75` on
`planning/ai-dev-tasks`. Copilot updated documentation only; no commands or
Git operations were run.

**Inputs:** Ricardo's scope decision and the reviewed PRD, task list, automation
behavior note, source README, project README, and existing AI-use record.

**Assistance and affected files:** Copilot applied the scope clarification in
`tasks/prd-bart-reconstruction-workflow.md`,
`tasks/tasks-bart-reconstruction-workflow.md`,
`docs/python-automation-behavior.md`, `src/README.md`, `README.md`, and this
record. No code, tutorial, execution result, or local record was modified.

**Corrections and decisions:** The December 1 delivery cases are fully sampled
Cartesian 2D without CS, fully sampled Cartesian 3D without CS, and Cartesian
3D CS using supplied sensitivities or explicitly requested `ecalib`.
Cartesian 2D CS is no longer a delivery requirement; it may be considered as a
future extension without an implementation commitment. This supersedes its
earlier inclusion in the planned scope without deleting that historical record.
Multiple ESPIRiT map-set support remains a separate unresolved capability;
radial remains out of scope. The existing program rejection of 2D CS and the
recorded manual and automated evidence are unchanged.

**Execution and evidence:** This was a documentation-only scope decision. No
implementation, reconstruction, comparison, or test was performed. Existing
case-specific manual and automated evidence remains recorded in its original
entries and task notes.

**Review and related revision:** Task checkboxes were preserved. Optional
figures remain optional per run, while their support remains an automation
requirement under FR-31. ARC usability is an interface objective; deployment
or execution in ARC is not required for this delivery under the PRD and remains
unverified.

**Limitations:** This decision does not implement or execute Cartesian 2D CS,
resolve support for multiple ESPIRiT map sets, establish general scientific
validation, or verify ARC execution.

## 2026-11-22 — Manual and automated multichannel CS calibration evidence

**Date:** Consolidated on 2026-11-22 from Ricardo's reports of the manual and
automated Cartesian 3D multichannel compressed-sensing executions and their
comparison.

**Tool/model and access mode:** ChatGPT statically reviewed the implementation
and guided Ricardo's execution and comparisons. Ricardo executed the commands
and supplied the results. Copilot implemented and corrected the route and
applied this documentary consolidation. Exact model identifiers were not
recorded.

**Inputs:** Ricardo's supplied summary for the synthetic preparation
`$HOME/bart-learning/bart-workflow-preparations/generation-3d-ecalib-01`,
the preserved mask in
`$HOME/bart-learning/bart-workflow-preparations/generation-3d-cs-01/mask3d`,
and Ricardo's summaries of the manual run under
`$HOME/bart-learning/bart-workflow-reconstructions/manual-3d-ecalib-01` and
automated run under
`$HOME/bart-learning/bart-workflow-reconstructions/automated-3d-ecalib-01`.
The assistant did not access those local directories or execution artifacts.

**Assistance and affected files:** Copilot implemented and corrected the
multichannel CS/`ecalib` route in `src/bart_workflow.py`, documented the options
and example in `src/README.md`, and updated the related automation behavior
note in `docs/python-automation-behavior.md` and progress/evidence in
`tasks/tasks-bart-reconstruction-workflow.md`. ChatGPT statically reviewed the
implementation and guided Ricardo's executions and comparisons. Ricardo
executed the commands and supplied the results. Copilot applied this
documentary consolidation to `src/README.md`,
`docs/python-automation-behavior.md`, `tasks/tasks-bart-reconstruction-workflow.md`,
and this record; the implementation code was not modified in this consolidation.

**Corrections and decisions:** The implemented extension keeps the existing
terminal entry point and function and adds an explicit sensitivity source:
provided maps or requested `ecalib`. The new 3D CS route supports channel axis 3
and one map set on axis 4, matches sensitivity spatial/channel dimensions to
k-space, uses one spatial mask across channels, and preserves generated
sensitivities and eigenvalues. The calibration region is explicit; kernel,
threshold, crop and set-count defaults are recorded in the source README.
Sampling-pattern estimation, multiple map sets, CS 2D and radial reconstruction
remain unsupported here. The existing reconstruction profile and supplied-map
calls remain available.

**Execution and evidence:** Ricardo reported BART v1.0.00 and a 64 × 64 × 64
k-space with eight channels and singleton later axes. The preserved mask
check reported 37,312 acquired and 224,832 omitted spatial positions, exact
acquired-value equality across all eight channels, zeros at omitted positions,
and a fully sampled 64 × 16 × 16 center. The reported `ecalib` invocation used
`-r 64:16:16 -k 6:6:6 -t 0.001 -c 0.8 -m 1` and returned `0`. Sensitivity and
eigenvalue pairs passed dimensions, binary-size and finite-value checks; the
sensitivity maps were not completely zero, and one ESPIRiT set was used. The
reported `pics` invocation used `--fista --wavelet dau2 -R W:7:0:0.01 -i 100
-s 0.95 -n -w 1`, the preserved mask and generated maps, and returned `0`.
The reconstruction passed the reported structural check for shape, singleton
later axes, complex64 representation and finite values.

Ricardo additionally reported the local automated run using the same
64 × 64 × 64 k-space, eight synthetic channels, mask and one ESPIRiT set. The
complete Python invocation returned `0`. `ecalib.log` records BART code `0`
and `-r 64:16:16 -k 6:6:6 -t 0.001 -c 0.8 -m 1`. `reconstruction.log` records
`pics` using the generated sensitivities in the automated run directory, the
same mask and k-space, and `--fista --wavelet dau2 -R W:7:0:0.01 -i 100
-s 0.95 -n -w 1.0`; its code was `0`. The reported `stage-records.json`
contains eight stages, all `success` with code `0`: `input-inspection`,
`sampling-check`, `ecalib-input-check`, `ecalib`, `ecalib-output-check`,
`sampling-and-sensitivity-checks`, `reconstruction`, and
`reconstruction-output-check`. Calibration and reconstruction `log_error`
values are `null`; resolved settings and generated-map paths are recorded.
Ricardo reported `cmp` exit code `0` for the manual/automated
`sensitivities.cfl`, `eigenvalues.cfl`, and `reconstruction.cfl` pairs. These
reports are owner-supplied and were not independently reproduced.

**Review and related revision:** Static review by reading the changed code and
documentation found the path organized as input/mask checks, requested
calibration, generated-map/eigenvalue checks, `pics`, and output checks. This
static review is distinct from Ricardo's reported local execution. The earlier
reported in-memory compilation and CLI `--help` checks predate this integration
and do not verify it. The `cmp` results establish byte-for-byte identity only
for the three reported manual/automated file pairs; they are not automated
comparisons to a synthetic reference. Task 7.6 remains partial, and the current
task-state checkboxes remain unchanged.

**Limitations:** Evidence applies only to Ricardo's reported synthetic
preparation and paired manual/automated local executions. It does not establish
general compatibility, ARC execution, convergence, complete FR-32 coverage, or
scientific quality acceptance. The comparisons are not automated comparisons
to a reference image or volume.

## 2026-11-22 — First Python automation block and owner-reported checks

**Date:** Consolidated on 2026-11-22 from Ricardo's report of the first
automation implementation checks and executions.

**Tool/model and access mode:** Copilot implemented and corrected
`src/bart_workflow.py`; ChatGPT performed static review and guided the checks.
Ricardo executed all commands and supplied the results. Exact model identifiers
were not recorded.

**Inputs:** The reviewed manual Cartesian 2D, 3D and 3D CS procedures; the
first-block implementation and source README; and Ricardo's supplied terminal
results and execution-record summaries for synthetic preparations under
`$HOME/bart-learning/bart-workflow-preparations/` and reconstructions under
`$HOME/bart-learning/bart-workflow-reconstructions/`.

**Assistance and affected files:** Copilot implemented and corrected the first
automation block in `src/bart_workflow.py` and applied the documentary
consolidation to this record, the relevant progress/evidence notes in
`tasks/tasks-bart-reconstruction-workflow.md`, and the owner-reported check
summary in `src/README.md`. ChatGPT statically reviewed the implementation,
guided Ricardo's checks, and prepared the consolidation instructions. During
this documentary consolidation, no tutorial, PRD, reconstruction parameter,
or local execution record was modified.

**Corrections and decisions:** The 2D run used `generation-01/kspace` and wrote
`automated-2d-01/reconstruction`, compared with
`manual-2d-01/reconstruction.cfl`. The 3D run used `generation-3d-01/kspace`
and wrote `automated-3d-01/reconstruction`, compared with
`manual-3d-01/reconstruction.cfl`. The CS run used
`generation-3d-cs-01/kspace_undersampled` with that generation's `mask3d` and
`sensitivities`, and wrote `automated-3d-cs-01/reconstruction`, compared with
`manual-3d-cs-01/reconstruction.cfl`. The commands correspond to `fft -i -u
3`, `fft -i -u 7`, and `pics` with the explicit `manual-cartesian-3d-cs`
profile. The reported destination-protection check used `output-guard-VxO0l5`
and confirmed that an existing directory is rejected without modifying its
pre-existing `stage-records.json`.

**Execution and evidence:** Ricardo reported that in-memory syntax compilation
and terminal `--help` both returned exit code `0`. For each of the three
reconstruction runs, the supplied stage record reports BART exit code `0`,
successful structural checks and `log_error: null`; each automated directory
contains the reconstruction pair, `reconstruction.log` and
`stage-records.json`. Ricardo ran `cmp` against the corresponding manual
reconstruction `.cfl` in the terminal; all three returned exit code `0`,
establishing byte-for-byte equality of those pairs for these runs. No separate
comparison artifact was created and no automated comparison function was
implemented. For the output-guard check, Ricardo reported workflow exit code
`1`, unchanged dummy stage-record contents (`cmp` exit code `0`), and a
post-check listing containing only that original record. The earlier Pylance
syntax-check request timed out and is inconclusive, not a passing check.

**Review and related revision:** ChatGPT performed static review and guided the
checks; Ricardo executed the commands and provided the reported outputs.
Evidence and attribution are recorded under Tasks 7.6–7.10 without changing
their statuses or the status of Block 7.0. The manual `.cfl` comparisons are
not the automated reconstruction-to-reference comparison work in Task 7.10.

**Limitations:** The results are limited to the reported local synthetic
preparations and these executions. They do not establish all FR-32 conditions,
execution on ARC, general compatibility, scientific validation or a quality
acceptance criterion. The byte comparisons establish equality only for the
reported manual/automated output pairs; they are not comparisons to the
synthetic reference and do not implement a reusable comparison operation.

## 2026-11-16 — Manual Cartesian 3D compressed-sensing execution and consolidation

**Date:** Consolidated on 2026-11-16, covering the reviewed manual Cartesian 3D
compressed-sensing execution evidence and its local-record consolidation.

**Tool/model and access mode:** GitHub Copilot Chat in VS Code and ChatGPT
through owner-provided repository documents, local synthetic-case logs and
headers, execution records, figures and Ricardo's supplied results. Exact model
identifiers were not recorded.

**Inputs:** The reviewed PRD and task list, the accepted project decisions,
`docs/tutorials/manual-cartesian-3d-cs.md`, the existing 3D tutorial format,
`scripts/check_preparation_pair_3d.py`, `scripts/check_fourier_numpy.py`, the
two local CS preparations, the local reconstruction directory and Ricardo's
execution observations.

**Assistance and affected files:** Copilot drafted and edited the CS tutorial,
updated `scripts/check_preparation_pair_3d.py` to admit `kspace_full`, prepared
the related documentation and task tracking, and created the two preparation
records and the reconstruction `run-record.md`. ChatGPT reviewed the shared
fragments and results, explained the procedure, and guided the manual execution
and recovery after paste errors.

**Corrections and decisions:** The documented case uses a BART Shepp–Logan
phantom of `64 x 64 x 64`, one channel, a Poisson mask repeated with
`repmat 0 64`, constant sensitivities `1 + 0j`, and the reviewed `pics`
parameters. The optional Appendix A viewer uses the existing configured
`PYTHON`, reads existing CS files, resolves the interactive backend and GUI
framework without forcing a backend, and does not create saved figures,
metrics or records. The future automation is documented to expose clearly
named sampling and reconstruction parameters, accept explicit values, and
document defaults where appropriate; the values in this manual example are
not universal defaults.

**Execution and evidence:** Ricardo confirmed the decisions and approved the
procedure before execution, executed the commands, inspected the static figure
and optional viewer, and supplied the results. Copilot and ChatGPT did not
perform the BART or Python execution. The local records preserve the observed
mask counts and acceleration, regeneration comparison, reconstruction,
structural check, static figure, quantitative comparison and the human visual
observation. The viewer confirmation was `macosx` backend/framework with final
exit code `0`. The evidence includes owner-reported statuses where the
corresponding generation log is empty and preserves the ambiguous second
mask-application record.

**Review and related revision:** Copilot performed static review of the
procedure, cross-references, local records and evidence consolidation. The
review confirmed separation of operational results, human observations and
quality interpretation, and recorded the corresponding Task 6.0 conclusions.
Ricardo remains responsible for confirming the consolidated records and any
later release or automation decisions.

**Limitations:** Exact execution timestamps, the repository revision, and the
state of local changes during execution remain unconfirmed. The evidence does
not establish `pics` convergence, exactly 100
iterations, inspection of every slice, a quality acceptance criterion, general
validation or clean-checkout reproducibility. The local preparation data,
logs, figure and records remain outside the repository.

## 2026-11-05 — Manual Cartesian 3D tutorial and evidence consolidation

**Date:** Consolidated on 2026-11-05, covering the drafting, review, execution
and evidence consolidation of the manual Cartesian 3D synthetic procedure.

**Tool/model and access mode:** GitHub Copilot Chat in VS Code and ChatGPT
through owner-provided repository documents, code excerpts, execution outputs
and a supplied figure. Exact model identifiers were not recorded.

**Inputs:** The reviewed PRD and task list, the accepted project decisions,
existing 2D tutorial and support scripts, the local environment record, and
Ricardo's reported 3D execution evidence and observations.

**Assistance and affected files:** Copilot drafted and edited
`docs/tutorials/manual-cartesian-3d.md`,
`docs/tutorials/manual-cartesian-2d.md`,
`scripts/check_preparation_pair_3d.py`,
`tasks/tasks-bart-reconstruction-workflow.md`, `README.md` and this record.
The work covered the synthetic-case proposal, preparation and regeneration
instructions, BART reconstruction, structural checks, static and optional
interactive visual comparison, full-volume quantitative comparison and the
execution-record format. The 2D tutorial also received the shared
regeneration-comparison corrections; its historical execution evidence was
preserved.

**Corrections and decisions:** The 3D case was fixed as a BART-generated
64 × 64 × 64 Shepp–Logan phantom, fully sampled Cartesian, single-channel and
without simulated coil sensitivities. The reference, k-space and reconstruction
remain separate. Regeneration review preserves the original header `DIFFERENT`
results while allowing a documented review when both binary files match and
header differences are limited to generation-directory paths; dimensions,
BART version, options, base names and input/output roles must otherwise match.
The interactive viewer backend resolution was corrected to unpack
`backend_registry.resolve_backend()` directly into the backend and GUI
framework before execution. The viewer remains optional and does not become a
condition for future non-interactive automation.

**Execution and evidence:** ChatGPT reviewed proposals, code excerpts,
documentation, execution outputs and the supplied static figure, and guided
the manual execution. Ricardo reviewed the work, personally executed the
commands, supplied the visual observations and confirmed the optional viewer
behavior. The two 3D preparations passed their structural checks; both binary
comparisons returned `MATCH` with exit code `0`, while both header comparisons
returned `DIFFERENT` with exit code `1` and were explained by the expected paths.
BART reconstruction from `generation-3d-01` to `manual-3d-01` returned exit code
`0`; the reconstruction structural check returned `VALID` with exit code `0`.
Static figure generation returned exit code `0`. Ricardo reported no visually
appreciable differences in the displayed index-32 orthogonal slices; the log
reported reconstruction slice magnitudes above the fixed display maximum, and
the cause was not inferred. The complete-volume complex relative L2 error was
`1.729089800e-07` with exit code `0`, using complex64 stored data and complex128
calculation arrays, without preprocessing or a tolerance. The optional viewer
resolved the `macosx` backend and GUI framework, closed normally with exit code
`0`, and Ricardo confirmed its operation and his observations without claiming
that every slice was inspected. Reported versions were BART v1.0.00, Python
3.13.17, NumPy 2.5.4 and Matplotlib 3.11.2.

**Review and related revision:** Copilot consolidated the owner-supplied evidence
and recorded its static review under Task 5.10. ChatGPT reviewed the proposals,
code excerpts, documentation, execution results and consolidation diff, and
guided Ricardo's manual execution. The task list
records Tasks 5.1–5.10 as complete where supported by the proposal, review,
owner execution and supplied evidence. The optional cumulative `run-record.md`
was not made mandatory. The tutorial does not contain execution transcripts or
historical result tables.

**Limitations:** The evidence is for this synthetic case and does not establish
general validation, a numerical acceptance criterion, clean-checkout
reproduction, experimental 3D validation, or equivalence of a future automated
route. The supplied execution records remain outside the repository. No
compressed-sensing procedure was started, and no experimental data, DICOM,
extraction code, credentials, private storage or HPC access was used.

## 2026-11-03 — Simplified tutorial replacement for Task 2.3 review

**Date:** 2026-11-03, covering incorporation and static review of the simplified replacement for the manual Cartesian 2D tutorial.

**Tool/model and access mode:** ChatGPT prepared the replacement document supplied by Ricardo; GitHub Copilot Chat in VS Code integrated the file and updated the task tracking. Exact model identifiers were not recorded.

**Inputs:** Ricardo's corrected `manual-cartesian-2d.md` attachment, the existing tutorial, the active task list, and the consolidated assistance record.

**Assistance and affected files:** ChatGPT prepared the simplified tutorial replacement, performed static review of its nine sections, reviewed the shared visual PNG, and helped interpret Ricardo's reported results. Follow-ups added executable, non-interactive visual-comparison and quantitative-comparison blocks to Sections 7–8. Copilot integrated the replacement at `docs/tutorials/manual-cartesian-2d.md` and updated the Task 2.3–2.5 and later execution/comparison tracking.

**Corrections and decisions:** The replacement keeps one configuration block, explicitly reuses checked preparations, organizes new preparation by stages, uses consistent command-error handling, and keeps a brief run-record format confirmed by Ricardo. Section 7 generated one headless two-panel PNG using `read_bart_2d`, transposed magnitudes, shared reference-based limits, and a new figure directory without overwriting existing files. Ricardo approved that visual method and accepted the clipping warning as a presentation limitation. Section 8 applied Ricardo's approved complex relative L2 method through `read_bart_2d` and `relative_error` on the original complex arrays without preprocessing, normalization beyond the metric denominator, tolerance, or pass/fail criterion. The historical two-generation evidence remains separate.

**Execution and evidence:** Ricardo executed the BART reconstruction and shared the reported logs and results. The reconstruction returned exit code `0`; the structural check returned `VALID` with exit code `0`; figure generation returned exit code `0`; and the quantitative comparison returned `1.442448308e-07` with exit code `0`. The visual log reports reconstruction values above the display maximum and clipping. The printed maxima do not determine the exact excess or its cause. The previously reported evidence of two historical generations remains unchanged.

**Review and related revision:** Ricardo executed the commands, shared the results, confirmed the manual execution record, and approved both comparison methods. ChatGPT reviewed the PNG and helped interpret the reported outputs without attributing personal visual observations to Ricardo. Copilot updated the tutorial and task tracking. The existing `run-record.md` was found in the execution directory and was not modified.

**Limitations:** The execution is case-specific and does not establish general validation or clean-checkout reproduction. The visual log reports clipping above the reference display maximum; the exact excess and cause are not determined by the printed maxima. The cumulative record format remains optional and was not used as a prerequisite; stage-specific records remain the execution evidence. Ricardo's confirmations close the manual execution-record and comparison-method review tasks without changing those limitations.

## 2026-11-02 — Task planning and synthetic 2D tutorial checkpoint

**Date:** Consolidated on 2026-11-02, covering development-task planning, synthetic 2D preparation and regeneration, and manual-tutorial drafting.

**Tool/model and access mode:** GitHub Copilot Chat in VS Code and ChatGPT through owner-provided documents, text excerpts, execution reports, and public documentation. Exact model identifiers for the complete round were not recorded.

**Inputs:** Reviewed repository documentation, the PRD, the development task list, existing synthetic 2D support code, successive procedure and tutorial drafts, and execution evidence supplied by Ricardo.

**Assistance and affected files:** Assistance covered task-list review, preparation-checker drafting, shell-procedure review, interpretation of reported execution results, tutorial drafting, and static integration review. This checkpoint saves the integrated nine-section tutorial draft, separates the Section 9 execution and method-review fields, marks Task 2.2 complete, and updates the task list and this assistance record.

**Corrections and decisions:** The work preserved the distinction between synthetic preparation and reconstruction, retained separate generation directories, corrected shell invocation and result reporting, clarified why the case was generated twice, and separated reusable tutorial instructions from historical execution evidence. Personal installation paths were distinguished from reader-configurable paths. The proposed visual comparison uses shared magnitude display without independent normalization, while its method remains pending review; the proposed display transpose is visual only. The preliminary quantitative comparison identifies its open method, representation, preprocessing, and reporting decisions without adopting the exploratory metric or values. Section 9 now separates method-review status, operational execution status, figure generation, human inspection, and quantitative results, while preserving `MATCH`, `DIFFERENT`, and `ERROR` for generation comparisons. No run record was created and no execution was claimed. Existing visualization support was inspected but not invoked because it expects an additional NumPy reconstruction and produces a broader figure set.

**Execution and evidence:** Ricardo executed both preparation generations. Each reported five successful stages. Comparisons of the four corresponding reference and k-space header and binary files returned MATCH with exit code 0. These results establish exact equality of those files between the two reported executions. AI assistance did not execute BART, Python project scripts, reconstructions, or project tests.

**Review and related revision:** Copilot proposed procedures and tutorial text; ChatGPT provided static review; Ricardo reviewed and executed the preparation and comparison commands. The latest owner-supplied publication checkpoint is 657e1fa on planning/ai-dev-tasks. No publication evidence for this documentation checkpoint has been supplied.

**Limitations:** The saved tutorial is an integrated Task 2.2 working draft and has not been executed as written. The visual method is not approved, the quantitative method and implementation remain pending Tasks 4.2–4.3, and the Section 9 record format remains pending Task 2.4 review. Reconstruction of the new exercise, reconstruction-output checks, visual comparison, quantitative comparison, and clean-checkout reproduction have not been demonstrated. Task 2.3 is the next review step.

## 2026-11-02 — Reviewed PRD and planning documentation

**Date:** Consolidated on 2026-11-02 (UTC), covering the requirements discussions
after the supplied `ad532fc` publication checkpoint, Copilot's reported PRD save,
and preparation of this documentation update. This date does not assign all
activities to a single day.

**Tool/model and access mode:** ChatGPT through the web interface, with public
web retrieval and document inspection/editing tools. Delegated document editors
and reviewers worked on the prepared copies. Ricardo identified GitHub Copilot
Chat in VS Code as the client used for this requirements stage. Exact model
identifiers for the complete round were not independently recorded.

**Inputs:** Cumulative reviewed repository documentation, Ricardo's decisions and
supplied Git publication output, successive PRD drafts, the supplied
`prd-bart-reconstruction-workflow.md` attachment, and Copilot's completion report.
Public references included ai-dev-tasks, BART and VS Code documentation. Two
owner-supplied Python reference scripts were read statically after Ricardo
confirmed their use for that purpose. The scripts contained local paths and
acquisition-specific labels; those values are not reproduced in this entry or
the prepared repository prose.

**Assistance and affected files:** Assistance covered interactive requirements
clarification, review of Copilot's PRD drafts, interpretation of the two reference
scripts, and preparation of English documentation copies and an incremental
patch for Ricardo to review and apply. The affected files are
`tasks/prd-bart-reconstruction-workflow.md`, `README.md`,
`.github/copilot-instructions.md`, `docs/copilot-handoff.md`,
`docs/project-context.md`, `docs/open-questions.md` and this `AI_USE.md` entry.
The PRD edits in this documentation pass correct links and align summary wording
with its existing requirements; they do not select the pending scientific or
implementation details.

**Corrections and decisions:**

- The agreed sequence begins with manual synthetic tutorials, starting with 2D,
  followed by equivalent Python automation for Cartesian 2D, Cartesian 3D and
  Cartesian 3D with compressed sensing. Synthetic preparation is separate from
  the reconstruction operation that accepts compatible BART inputs.
- The software interface means a terminal entry point backed by reusable Python
  functions. Runs require no GUI, windows, dialogs or interactive questions;
  optional figures are saved for later inspection.
- Manual–automated comparisons use the same prepared synthetic inputs and
  equivalent effective settings and requested outputs. Regeneration of a case,
  difference from the reference, route equivalence and operator intervention
  remain separate evaluation questions.
- A reviewed metric and calculation procedure precede the preliminary numerical
  comparison. A tolerance or pass/fail rule is not required for that descriptive
  comparison; any later formal test requires its criteria in advance. Questions
  concerning later evaluations do not automatically block the first comparison.
- Earlier PRD edits were corrected to preserve FR-1 through FR-40 and the original
  FR-33 through FR-37 meanings. FR-32 remains proposed behavior pending review.
  The additional phantom-definition discussion proposed before saving the PRD
  was deferred to the relevant task-planning work, with those choices left open.
- Static script review identified assumptions about input layout and possible
  reuse of existing outputs after settings change. These are review findings,
  not observed reconstruction failures or verified recipes for the new workflow.
- Three PRD contract links were changed from local filesystem targets to relative
  repository links. Navigation and current planning descriptions now reference
  the reviewed draft. The accepted contract retains its separate access/action
  authority, and historical AI-use records remain unchanged.

**Execution and evidence:** Copilot's supplied transcript reports saving the PRD
and checking it by text searches and reads. Its read operations name `tasks/`,
while its final message names `task/`. The supplied attachment establishes the
document content available for review, not its location on Ricardo's computer
or its Git publication state. The prepared documentation consistently uses
`tasks/prd-bart-reconstruction-workflow.md`.

ChatGPT read and edited review copies, checked requirement identifiers and
relative references, compared text and prepared a patch. Text review confirmed
one definition of each FR-1 through FR-40 and preserved the 31 PRD questions,
18 project-question identifiers and earlier AI-use entries. Public source reads
provided workflow context; retrieval of the project branch did not return its
contents. File-content review therefore used the known reviewed copies and the
supplied PRD, rather than an independently synchronized checkout.

No project scripts, tests, reconstructions, builds or installations were run.
The two reference scripts were not executed, edited or incorporated into the
repository. No development task list or implementation was generated in this
documentation pass. The assistant did not apply changes on Ricardo's Mac or
perform Git operations or remote publication.

**Review and related revision:** Ricardo reviewed the requirements discussions
and requested that this documentation update be prepared with ChatGPT. His
latest supplied publication output places `planning/ai-dev-tasks` and its
remote-tracking reference at `ad532fc`, with the message
`docs: clarify Git workflow and historical records`, following `2435329`.
The supplied status showed no file-change entries or ahead/behind indication at
that checkpoint. These records do not establish a subsequent merge into `main`.
The PRD remains `Reviewed draft for task planning`; this update is prepared for
Ricardo's review and application. No supplied output establishes a commit or
publication of this round.

**Limitations:** This work establishes documentation consistency, not scientific
validation, numerical acceptance, clean-checkout reproduction or tool isolation.
The first phantom, dimensions, sampling, channel count, metrics, tolerances and
implementation details remain open where identified in the PRD. Experimental
arrays, DICOM, credentials, private storage and HPC access were not part of this
work. The accepted contract, its decision register and the completed
contract-creation prompt were not edited. Task planning is the next supervised
stage after review of this documentation update.

## 2026-10-29 — Git workflow and historical record clarification

**Date:** Consolidated on 2026-10-29, covering the final documentation cleanup
after Ricardo supplied the `2435329` publication checkpoint, and preparation of
this entry.

**Tool/model and access mode:** ChatGPT through the web interface, with tools for
document inspection and editing and read-only reviewer agents. Model identifiers
for the complete round were not independently recorded.

**Inputs:** The repository export at
`5bcf772a09ced4339cc70b87eba85488713c2c41`, cumulative reviewed documentation,
selected supplied synthetic text records, and Ricardo's commit, push, status and
log output for `2435329`.

**Assistance and affected files:** English review copies and incremental patches
were prepared for `docs/git-workflow.md`, `docs/sources.md`,
`docs/milestones/01-familiarization.md` and this `AI_USE.md` entry. Assistance also
included explanations of the proposed wording and commands for Ricardo to review,
apply, commit and publish the documentation changes.

**Corrections and decisions:**

- The Git guide now presents continued work on an existing branch first, with
  separate routes for creating a new branch and consulting the historical initial
  setup. Branch names and commit messages are examples, and historical command
  instructions are distinguished from evidence that commands were executed.
- The source catalogue identifies the 39-file staged listing with the
  2026-10-23 assembly checkpoint. It is not presented as a current repository
  file count.
- The milestone's pending-work column and completion-review wording explicitly
  refer to the assembly checkpoint. Historical pending statuses were preserved
  rather than replaced by later publication outcomes.
- The milestone now describes the timestamp recorded in the supplied start file,
  replacing the stronger phrase "Exact initial execution timestamp". Supplied
  timestamps, reported measurements and their evidence limits were preserved.
- Ricardo requested a plain-language explanation of these small wording changes,
  then authorized the limited edits, consolidation of this entry and direct
  commit instructions. The edits did not expand into a broader historical rewrite.

**Execution and evidence:** Document-handling tools read archive text and prepared
copies, compared text, inspected headings and references, and created review
files and patches. Read-only reviewer agents checked factual preservation,
historical context and readability. Selected supplied text records were read to
check timestamp wording; no values were recalculated.

No project scripts, tests, reconstructions, builds or installations were run.
The assistant did not execute the Git procedures, commit, push or modify the
remote repository. Publication evidence came from Ricardo's terminal output;
current GitHub contents were not independently inspected.

**Review and related revision:** Ricardo authorized the successive blocks and
requested the consolidated record and commit instructions. His supplied output
records commit `2435329` with the message
`docs: clarify project records and update publication evidence`, and its successful
push to `planning/ai-dev-tasks`. The supplied status and log showed the local branch
and its remote-tracking reference at that commit,
with no file-change entries at that checkpoint. This evidence follows the
previous entry's preparation; the earlier entry remains a record of what was
known then. No subsequent Git output establishes a commit or publication of this
final documentation round. This entry is prepared for Ricardo's review.

**Limitations:** This was an internal documentation and evidence-consistency
review. The original course PDFs were not available for direct comparison, and
public reference links were not rechecked online. No scientific validation,
clean-checkout reproduction or technical isolation was established. Experimental
data, DICOM, extractor code, credentials, private storage and HPC remained outside
the work. The accepted contract, its decision register and the completed
contract-creation prompt were not edited. Interactive preparation of ai-dev-tasks
with Copilot remains pending.

## 2026-10-29 — Follow-up documentation cleanup

**Date:** Consolidated on 2026-10-29, covering the follow-up documentation blocks
after Ricardo supplied publication evidence for `d59ff7d`, and preparation of
this entry.

**Tool/model and access mode:** ChatGPT through the web interface, with tools for
inspecting and editing documents and read-only reviewer agents. A model identifier
covering the complete round was not independently recorded.

**Inputs:** The previously reviewed repository export at
`5bcf772a09ced4339cc70b87eba85488713c2c41`, cumulative documentation copies and
patches, Ricardo's project decisions, and his supplied Git push, status and log
output for `d59ff7d`.

**Assistance and affected files:** English review copies and incremental patches
were prepared for `docs/project-context.md`, `docs/input-inventory.md`,
`docs/open-questions.md`, `docs/copilot-handoff.md` and this `AI_USE.md` entry.
The work clarified document purpose, reported input history, pending questions
and the distinction between earlier and later Git checkpoints.

**Corrections and decisions:**

- Project context was rewritten as technical direction and evaluation planning.
  Proposal and instructor-feedback quantities remained attributed planning,
  without becoming AI-access rules, software limits or a newly approved protocol.
- Current brain MRI 3D `.cfl`/`.hdr` reports were separated from historical `.h5`,
  extraction and acquisition descriptions. Configuration rows were not treated as
  dataset counts; correspondence between earlier descriptions and current inputs
  remained unresolved.
- The open-questions record retained all 18 identifiers. A draft of DATA-03 was
  corrected to preserve the unresolved conventions of current experimental inputs
  alongside future software support. These questions remained separate from the
  accepted AI access/action contract.
- GIT-02 wording was changed from "review commit" to "published commit" to reflect
  the supplied evidence. The Git questions and handoff incorporated the
  supplied `d59ff7d` publication evidence while retaining the starting checkpoint.
- Planned milestone dates, supplied synthetic timestamps and Git publication
  records remained distinct. The existing synthetic exercise remained exploratory
  evidence without a numerical acceptance threshold or general validation claim.

**Execution and evidence:** Document-handling commands read archive text and
prepared copies, created review files and patches, compared text and checked
relative references and heading anchors. Read-only reviewer agents checked
factual preservation, policy hierarchy and readability. No project scripts,
tests, reconstructions, builds or installations were run in this documentation
pass. The assistant did not commit, push or modify the remote repository.

File-content review used the supplied export and prepared copies. The assistant
did not independently inspect the current GitHub tree; the publication evidence
came from Ricardo's terminal output.

**Review and related revision:** Ricardo authorized the successive blocks and
requested this consolidated entry. His supplied terminal output records the
earlier publication of `planning/ai-dev-tasks` at `d59ff7d`, with the message
`docs: align documentation and standardize AI use records`; the
[publication checkpoint](docs/open-questions.md#supplied-publication-checkpoint)
records the evidence and its limits. The earlier documentation-alignment entry
remains a record of what was known before that output. No later command output
establishes the applied diff, commit or publication for this follow-up round.
This entry is prepared for Ricardo's review.

**Limitations:** Static documentation review did not reproduce the synthetic
exercise, verify experimental inputs or results, or establish tool isolation.
No experimental data, DICOM, extractor, credentials, private storage or HPC access
formed part of this work. The accepted contract, its decision register and the
completed contract-creation prompt were not edited. Detailed software and
evaluation design, and preparation of ai-dev-tasks with Copilot, remained pending.

## 2026-10-29 — Documentation alignment and record standardization

**Date:** Consolidated on 2026-10-29. This entry covers the repository review and
successive documentation blocks in this conversation; it does not assign all of
that work to the consolidation date.

**Tool/model and access mode:** ChatGPT through the web interface, with tools for
document inspection and editing and read-only reviewer agents. Exact model
identifiers for the complete review were not independently recorded.

**Inputs:** The repository export at
`5bcf772a09ced4339cc70b87eba85488713c2c41`, Ricardo's reported Git state and project
decisions, and the cumulative documentation copies prepared during the review.
The source export was the reference for repository contents; later edits were
prepared separately from that snapshot.

**Assistance and affected files:** Assistance covered document organization,
reading routes, current usage descriptions and the distinction between recorded
evidence and pending work. English file copies and incremental patches were
prepared for Ricardo's review. Affected files were `README.md`,
`docs/data-and-ai-boundaries.md`, `.github/copilot-instructions.md`,
`docs/copilot-handoff.md`, `docs/open-questions.md` and this `AI_USE.md` record.

**Corrections and decisions:**

- The README was organized as the reader's entry point, with environment, input,
  manual execution, automation status, verification and repository layout sections.
- Reading routes were updated to include the accepted contract and decision
  register. Supporting boundary notes explicitly defer to the contract for AI
  access and actions; software requirements and evaluation remain separate.
- The handoff and Git questions were aligned with recorded Copilot use and
  Ricardo's later Git report. Historical checkpoints were distinguished from
  current reported context and unverified operations.
- The 64 × 64 synthetic exercise remained exploratory evidence. The revised text
  did not claim a numerical acceptance threshold, clean-checkout reproduction,
  implemented automated workflow or experimental 3D validation.
- Ricardo confirmed that the contract-creation prompt had completed its purpose;
  a proposed further review of that prompt was removed from the work.
- Ricardo requested a consistent, reader-facing AI-use record. Historical
  instructions were rewritten as dated observations or unresolved record gaps,
  and a common entry format was introduced.

**Execution and evidence:** Initial orientation in the assistant's environment
printed the working-directory path and searched under `/workspace` for file paths
named `AGENTS.md`; no matching path appeared in the returned output. Subsequent
substantive review used the supplied ZIP and prepared documentation copies. Document-handling tools
listed and read archive contents, created review copies and patches, compared
text and checked relative references. Read-only reviewer agents provided bounded
editorial, evidence and policy reviews.

Attempts to retrieve the supplied GitHub pages did not establish live repository
contents. The review therefore did not use the remote as a verified replacement
for the supplied snapshot. No project scripts, tests, reconstructions, builds or
installations were run, and the assistant did not commit, push or modify the
remote repository.

**Review and related revision:** Ricardo authorized successive blocks and supplied
corrections during the conversation. This rewritten record is prepared for his
review. The source commit and owner-reported branch context are documented in the
[supplied Git checkpoint](docs/copilot-handoff.md#repository-checkpoint-supplied-by-ricardo).
Application of the prepared patches, later commits and publication were not
established through supplied command output.

**Limitations:** Static document and source-code review did not reproduce the
synthetic exercise or validate scientific results. No experimental data,
extractor, credentials, private storage or HPC access formed part of this work.
The accepted contract, its decision register and the existing contract-creation
prompt were not edited in this documentation pass.

## 2026-10-27 — Access/action boundary acceptance

**Date:** 2026-10-27, as recorded for the acceptance activity.

**Tool/model and access mode:** Copilot SDK in VS Code. The underlying model was
not recorded. The activity concerned reviewed project documentation.

**Inputs:** Reviewed project context and Ricardo's explicit acceptance of
ENSF620-BART-DC v0.3.0.

**Assistance and affected files:** Assistance covered the contract's purpose and
the record of owner acceptance. The recorded policy materials are
`docs/DATA_CONTRACT.md` and `docs/DATA_CONTRACT_DECISIONS.md`, with this log
documenting the assistance. The original entry did not provide a complete
file-level change list for that session.

**Corrections and decisions:** The contract was narrowed from an overly broad
software specification and evaluation document to an AI data-access and
action-boundary policy. Ricardo accepted the reviewed v0.3.0 as `OWNER_ACCEPTED`.

**Execution and evidence:** The session recorded documentary acceptance. No
commands or tests were run for that update. Technical implementation and
verification states remained unchanged.

**Review and related revision:** Owner acceptance was explicit and is preserved
in the contract and decision register. Ricardo subsequently identified `5bcf772`
as the acceptance commit; that association is owner-reported, not an independent
Git-history check performed for this log.

**Limitations:** Acceptance did not establish technical enforcement, restricted
data access, an approved software specification or evaluation protocol, or blanket
tool-execution permission. Operation-specific unresolved items remained in the
decision register.

## 2026-10-26 — Contextual documentation revision

**Date:** 2026-10-26, as recorded for the documentation revision.

**Tool/model and access mode:** Copilot SDK in VS Code, using reviewed workspace
documents and an authorized file list. The underlying model was not recorded.

**Inputs:** Reviewed project documents and Ricardo's updated, non-sensitive
description of scope, inputs, development approach and Git status.

**Assistance and affected files:** Documentation was revised in `README.md`,
`docs/project-context.md`, `docs/input-inventory.md`, `docs/open-questions.md`,
`docs/data-and-ai-boundaries.md`, `docs/copilot-handoff.md`,
`.github/copilot-instructions.md`, `AI_USE.md` and
`.github/prompts/rvb-create-data-contract.prompt.md`.

**Corrections and decisions:** The update reflected Python as the primary workflow
language; Cartesian 2D/3D scope including CS; author-reported brain MRI BART
`.cfl`/`.hdr` inputs; BART-generated synthetic phantoms for development and testing;
DICOM as a proposed complementary reference; and the owner-reported initial
`main` push at `aad0525`. Historical extraction and Poisson/R=8/10-volumes/"200"
details were retained with scope and correspondence limits. Reported availability,
verified recipes, implemented functionality and executed evidence were kept distinct.

**Execution and evidence:** The session record reports no terminal, network,
browser, MCP or subagent use and no private-data or remote-system access. No
commands, tests, commits or pushes were performed in that documentation update.
The then-draft contract files were not edited, and no contract acceptance occurred
in that session.

**Review and related revision:** Final author review of those edits was pending
at that checkpoint. A commit for the revision was not recorded in the entry.

**Limitations:** The update documented reviewed context and owner reports; it did
not verify experimental inputs, recipes, reconstruction results or tool isolation.
The contract's later acceptance is recorded separately under 2026-10-27.

## 2026-10-23 — Repository assembly and SSH preparation

**Date:** 2026-10-23, as recorded for the repository-preparation checkpoint.

**Tool/model and access mode:** ChatGPT, web interface. The model identifier was
not recorded. Ricardo supplied selected local outputs for review.

**Inputs:** A staged listing of 39 files, a text diff, SSH authentication output
and the chosen repository address.

**Assistance and affected files:** A documentation-only patch was prepared to
align repository contents, setup guidance and provenance notes with the supplied
listing and SSH route. The original entry did not enumerate every affected file.
Numerical code, metrics, figures, dependency versions and data boundaries were
not changed by that patch.

**Corrections and decisions:** Stale wording describing imported scripts and
reports as absent was corrected. GitHub CLI/HTTPS guidance was replaced with
Ricardo's selected SSH route; GitHub CLI was not required for that route.

**Execution and evidence:** Ricardo's supplied SSH output showed authentication
as `rictr161`. The intended remote was
`git@github.com:rictr161/ensf620-bart-workflow.git`, which Ricardo reported as
empty at that checkpoint. No private key or passphrase was supplied. The assistant
did not configure the remote, commit, push or rerun MRI calculations.

**Review and related revision:** Patch application, author review and subsequent
Git operations were not established by that entry. It did not identify a completed
commit or push.

**Limitations:** The staged listing established the listed files, and SSH output
established the reported authentication event. Neither demonstrated patch
application, publication, reviewer access or clean-checkout reproduction. The
empty-remote description belongs to this historical checkpoint.

## Consolidated 2026-10-23 — Familiarization, environment and repository preparation

**Date:** Consolidated on 2026-10-23 from preceding sessions. This date does not
mean that all work occurred that day or that the planned October 9 milestone was
met.

**Tool/model and access mode:** ChatGPT, web interface. Model identifiers were not
independently recorded for the preceding sessions. Copilot was planned for later
supervised work; no Copilot execution was established by this entry.

**Inputs:** Ricardo supplied the proposal, instructor feedback, proposal package,
final project guide, selected terminal outputs, five synthetic figures, hardware
details and a non-sensitive dataset summary.

**Assistance and affected files:** Assistance covered BART/Git concepts, a macOS
build recipe, synthetic image and k-space generation, Python setup, an independent
NumPy inverse, visualization, interpretation, inventory and English repository
notes and Copilot guidance. A complete per-session file list was not recorded.
Recorded outputs included `scripts/check_fourier_numpy.py`,
`scripts/visualize_synthetic.py`, selected reports and figures, environment records
and project documentation.

**Corrections and decisions:**

- Windows/WSL guidance was replaced after Ricardo clarified the macOS platform.
- BART's detached HEAD was identified as belonging to its separate upstream
  release checkout, not the ENSF 620 repository.
- A BART-only round trip was not treated as an independent correctness check;
  Ricardo subsequently executed a separate NumPy inverse.
- No numerical threshold or formal pass status was assigned after observing the
  residuals.
- An accidental `view` invocation opened Vim; exit guidance restored the terminal.
  This learning interruption was not an evaluated experimental failure.
- Ricardo corrected a temporary "No" for 3D CS to "Yes". This corrected the receipt
  report rather than documenting a new delivery. Format, actual volume count and
  the meaning of "200" remained unresolved at that checkpoint.
- The instruction file and `.gitignore` were recognized as guidance and
  version-control mechanisms, without evidence of restricted-data isolation.

**Execution and evidence:** Ricardo executed commands on his Mac and supplied
their outputs. The assistant did not access his Mac, TALC, laboratory storage or
GitHub repository. The checker read the synthetic files, checked dimensions,
binary sizes and finite values, and computed an inverse Fourier transform with
NumPy without invoking BART. No numerical acceptance threshold was applied. Five
figures and three reported relative errors were preserved as supplied evidence.

The supplied staged listing included the two imported scripts, selected text
reports and dependency snapshots. Script contents and environment snapshots also
appeared in the supplied diff. These records did not establish a new execution or
byte-for-byte equality with every original file on the Mac.

**Review and related revision:** The initial documentation was AI-drafted; author
review was pending at the pre-publication checkpoint. The entry did not establish
a completed commit or its date. Ricardo retained responsibility for scope,
criteria, code review, local execution, data handling and TALC submission.

**Limitations:** Clean-checkout reproduction, formal regression tests and the
experimental baseline remained pending. No laboratory measurements, derived
laboratory images, extraction code, credentials or private sharing links were
provided. Learning and one-time development were distinguished from later
operational comparisons.

## Incomplete historical disclosure

Earlier AI assistance with proposal scoping, drafting and LaTeX was acknowledged
in the proposal. A separate session-level record, exact dates, model identifiers,
affected revisions and verification details were not recorded in the supplied
AI-use log. That disclosure remains incomplete.

## Blank entry template

```markdown
## YYYY-MM-DD — Activity title

**Date:** [Activity date/range or consolidation date and period covered.]

**Tool/model and access mode:** [Tool, recorded model identifier and access mode.]

**Inputs:** [Reviewed information supplied or accessed for the activity.]

**Assistance and affected files:** [Material assistance and affected code or text.]

**Corrections and decisions:** [Accepted, corrected or rejected suggestions.]

**Execution and evidence:** [Actions actually performed, actor and supporting evidence.]

**Review and related revision:** [Human review status and known commit or revision.]

**Limitations:** [Unverified outcomes, missing records or unresolved discrepancies.]
```
