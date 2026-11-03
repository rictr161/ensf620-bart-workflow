# BART Reconstruction Workflow Development Tasks

Source: [Product Requirements Document](./prd-bart-reconstruction-workflow.md)

This task list is based on the reviewed PRD. It preserves the manual-before-automation
sequence, keeps unresolved scientific and interface decisions at the stage where they
are needed, and treats FR-32 as proposed behavior pending review. Tasks remain
unchecked until the corresponding work is completed and reviewed.

## Tasks

- [x] **1.0 Define and Review the Synthetic 2D Preparation Case**
  - [x] **1.1 [Copilot] Compile the open decisions required for the first synthetic 2D case**  
    Identify the unresolved choices for phantom definition, image dimensions, sampling configuration, Cartesian full-sampling status, channel count, channel handling, authoritative files, mandatory checks, and preparation records without assigning values.
  - [x] **1.2 [Copilot] Prepare and explain the proposed synthetic 2D preparation and regeneration procedure**  
    Develop a future technical proposal covering the candidate synthetic case, preparation and regeneration commands, required inputs, expected outputs, mandatory checks, and minimum execution record, without selecting the scientific values in this task-planning response.
    **Dependency:** 1.1
  - [x] **1.3 [Copilot] Review the proposed preparation procedure against the PRD and repository boundaries**  
    Check that the proposal separates synthetic preparation from reconstruction, uses BART-generated synthetic material, preserves the reference, includes regeneration verification, and does not rely on experimental data, extraction code, `.h5` conversion, or unapproved generalizations.
    **Dependency:** 1.2  
    **Review record:** The executed procedure used synthetic BART data, kept preparation separate from reconstruction, preserved inputs in separate generation directories, regenerated the reference and k-space, and stayed within the documented scope. Copilot prepared the proposal; ChatGPT performed static review; Ricardo reviewed and executed the procedure. The case-specific execution evidence and limitations are summarized in this task list and in the preserved stage-specific records.
  - [x] **1.4 [Ricardo] Review, adjust, and approve the proposed synthetic 2D preparation and regeneration procedure**  
    Review Copilot’s technical proposal, decide the required adjustments, and approve the commands, inputs, outputs, checks, regeneration procedure, and minimum record that will later be executed.
    **Dependency:** 1.3
  - [x] **1.5 [Ricardo] Prepare, regenerate, and verify the approved synthetic 2D case**  
    After the preparation and regeneration procedure, commands, inputs, outputs, checks, and minimum record have been documented and reviewed in 1.2–1.4, execute that procedure and verify that the regenerated reference, corresponding k-space, and required metadata match the intended case.
    **Dependency:** 1.4  
    **Evidence:** Ricardo reported five successful preparation stages for each generation and exact `MATCH` results with exit code `0` for all four corresponding reference and k-space files. The evidence remains separate from the reusable tutorial.

- [x] **2.0 Establish and Review the Manual Cartesian 2D Tutorial**
  - [x] **2.1 [Copilot] Draft the complete manual 2D tutorial structure**  
    Organize the tutorial from synthetic preparation and regeneration through k-space generation, BART reconstruction, output checks, visual comparison, preliminary quantitative comparison, and evidence recording.
    **Dependency:** 1.4
  - [x] **2.2 [Copilot] Document the reviewed manual procedure and its expected evidence**  
    Describe each future command, input, output, relevant parameter, expected check, figure, and observation without inventing undecided values or claiming execution.
    **Dependency:** 2.1  
    **Status:** Complete. The integrated simplified tutorial was reviewed for the manual reconstruction and reconstruction-output-check sequence. Visual and quantitative comparisons remain pending their respective review.
  - [x] **2.3 [Ricardo] Review the manual commands and BART procedure**  
    Confirm that the proposed manual sequence represents the intended BART procedure and identify changes required before execution.
    **Dependency:** 2.2  
    **Status:** Complete. Ricardo confirmed the simplified manual procedure for this synthetic 2D case, including use of the existing `generation-01` preparation and a new reconstruction output directory.
  - [x] **2.4 [Ricardo] Confirm the tutorial’s execution and evidence-recording format**  
    Approve how commands, configurations, checks, outputs, figures, observations, regeneration verification, and limitations will be recorded for the first case.
    **Dependency:** 2.3  
    **Status:** Complete. Ricardo confirmed the brief record format in the integrated tutorial.
  - [x] **2.5 [Copilot] Produce the reviewed 2D tutorial draft for execution**  
    Deliver a complete human-readable procedure that integrates the reviewed preparation and regeneration block, can be executed without undocumented interactive steps, and clearly marks any remaining decision or review gate.
    **Dependency:** 2.4 and 1.5  
    **Status:** Complete. The simplified tutorial is integrated and reviewed for the reconstruction and reconstruction-output-check execution; visual and quantitative comparisons remain explicitly pending.

- [x] **3.0 Execute and Document the Manual Synthetic 2D Reconstruction**
  - [x] **3.1 [Ricardo] Execute the reviewed manual 2D reconstruction procedure**  
    Run the approved tutorial using the verified prepared synthetic inputs and preserve the source inputs and generated outputs in a distinct case or run location.
    **Dependency:** 2.5  
    **Evidence:** Ricardo executed BART in `manual-2d-01` using the existing `generation-01` preparation; `reconstruction.log` records exit code `0`.
  - [x] **3.2 [Ricardo] Perform the required manual-stage checks**  
    Verify that each stage produced the expected files and data needed by the next stage, including the reference, k-space, reconstruction input, and BART reconstruction output.
    **Dependency:** 3.1  
    **Evidence:** `reconstruction-check.txt` reports `VALID` for 64 × 64 dimensions, singleton trailing axes, correct size, and finite values, with exit code `0`.
  - [x] **3.3 [Ricardo] Capture manual 2D execution evidence**  
    Record the executed commands, effective settings, checks, produced outputs, figures, observed failures, and corrections.
    **Dependency:** 3.2  
    **Evidence:** The `manual-2d-01` directory contains the reconstruction, output-check, visual-generation, and quantitative-comparison records; its existing `run-record.md` was not modified.
  - [x] **3.4 [Copilot] Review the recorded evidence for completeness and traceability**  
    Check that the record distinguishes preparation from reconstruction, includes the regeneration verification from 1.5, and does not present exploratory evidence as general validation.
    **Dependency:** 3.3  
    **Status:** Static review completed. The records distinguish the reused preparation from reconstruction and preserve the historical regeneration evidence separately.
  - [x] **3.5 [Ricardo] Confirm the manual 2D execution record**  
    Review the evidence and identify whether the manual tutorial execution is complete, needs correction, or must be repeated.
    **Dependency:** 3.4  
    **Status:** Complete. Ricardo confirmed that the available records sufficiently document the reconstruction, structural check, figure generation, and quantitative result for this case. This does not establish clean-checkout reproduction or general validation.

- [x] **4.0 Define and Perform Reconstruction-to-Reference Comparison**
  - [x] **4.1 [Copilot] Identify the pending decisions for the preliminary 2D comparison**  
    List the metric, calculation procedure, preprocessing, normalization, cropping, masking, alignment, and reporting choices required before the comparison is performed.
    **Dependency:** 3.5  
    **Status:** Complete. The tutorial identifies representation, preprocessing, normalization, alignment, reporting, tolerance, and pass/fail decisions before execution.
  - [x] **4.2 [Copilot] Propose and explain the preliminary 2D reference-comparison method**  
    Prepare a technical proposal for the visual and preliminary quantitative comparison, including the candidate metric, calculation procedure, preprocessing, normalization, cropping, masking, alignment, reporting fields, and limitations, without selecting final values or establishing tolerances.
    **Dependency:** 4.1  
    **Status:** Complete. The tutorial documents the visual proposal and the complex relative L2 candidate without importing exploratory values or acceptance criteria.
  - [x] **4.3 [Ricardo] Review, adjust, and approve the preliminary 2D reference-comparison method**  
    Review Copilot’s proposed visual and quantitative comparison method, decide the necessary adjustments, and approve the method for execution without treating it as general validation.
    **Dependency:** 4.2  
    **Status:** Complete. Ricardo approved the visual method: two magnitude panels, shared grayscale limits from zero to the reference maximum, and visual-only `abs(array).T` transposition. Ricardo accepted the clipping warning as a presentation limitation. Ricardo also approved the complex relative L2 method on original complex arrays without preprocessing, tolerance, or pass/fail criterion.
  - [x] **4.4 [Ricardo] Perform the 2D visual comparison**  
    Inspect and compare the manual reconstruction with the known synthetic reference using the reviewed visual procedure and preserve the resulting figures or observations.
    **Dependency:** 4.3  
    **Evidence:** Ricardo generated the two-panel PNG with exit code `0` and shared it; ChatGPT reviewed the PNG. The visual log reports reconstruction values above the display maximum and clipping. No personal visual observations are attributed to Ricardo.
  - [x] **4.5 [Ricardo] Perform the preliminary quantitative 2D comparison**  
    Calculate and record the observed difference using the reviewed metric and calculation procedure, without presenting the result as general validation.
    **Dependency:** 4.3  
    **Evidence:** `quantitative-comparison.txt` records complex relative L2 error `1.442448308e-07`, exit code `0`, original complex arrays, no preprocessing, and no tolerance or pass/fail criterion.
  - [x] **4.6 [Copilot] Review the combined 2D tutorial evidence**  
    Confirm that Tasks 1.0–4.0 collectively cover preparation, regeneration verification, tutorial documentation, manual execution, visual comparison, preliminary quantitative comparison, and the distinction between case-specific evidence and general validation.
    **Dependency:** 4.4 and 4.5  
    **Status:** Complete. Static review confirmed that preparation/regeneration, reconstruction, structural checking, visual figure generation, and quantitative comparison remain distinct from general validation.

- [ ] **5.0 Establish, Review, Execute, and Record the Manual Cartesian 3D Procedure**
  - [ ] **5.1 [Copilot] Identify the decisions required for the manual Cartesian 3D case**  
    Organize the later-stage questions concerning the synthetic case, dimensions, input characteristics, reconstruction procedure, output representation, mandatory checks, and reference comparison without selecting their values.
    **Dependency:** 4.6
  - [ ] **5.2 [Copilot] Prepare and explain the proposed manual Cartesian 3D procedure**  
    Develop a future technical proposal covering the candidate synthetic case, preparation and regeneration commands, reconstruction commands, required inputs, expected outputs, reference-comparison methods, mandatory checks, and evidence record, without selecting the scientific values in this task-planning response.
    **Dependency:** 5.1
  - [ ] **5.3 [Copilot] Review the proposed Cartesian 3D procedure against the PRD**  
    Check that the proposal separates synthetic preparation, regeneration verification, manual reconstruction, reference comparison, and evidence recording while preserving the manual-first sequence and avoiding experimental input requirements.
    **Dependency:** 5.2
  - [ ] **5.4 [Ricardo] Review, adjust, and approve the Cartesian 3D manual procedure**  
    Review Copilot’s technical proposal, decide the required adjustments, and approve the preparation, regeneration, reconstruction, comparison, checking, and recording procedures before execution.
    **Dependency:** 5.3
  - [ ] **5.5 [Ricardo] Prepare, regenerate, and verify the synthetic Cartesian 3D case**  
    Execute the approved preparation procedure, regenerate the intended synthetic case, and verify the reference, corresponding reconstruction input, and required metadata before performing the manual reconstruction.
    **Dependency:** 5.4
  - [ ] **5.6 [Ricardo] Execute the reviewed manual Cartesian 3D reconstruction**  
    Run the approved manual reconstruction procedure using the verified prepared synthetic inputs and perform the required stage and output checks.
    **Dependency:** 5.5
  - [ ] **5.7 [Copilot] Prepare and explain the Cartesian 3D reference-comparison application**  
    Propose how the reviewed visual and quantitative reference-comparison method should be applied to the Cartesian 3D case, identifying any case-specific preprocessing, reporting, or limitation decisions without imposing a new metric or tolerance.
    **Dependency:** 4.3 and 5.4
  - [ ] **5.8 [Ricardo] Review, approve, and execute the Cartesian 3D reference comparison**  
    Review the proposed application, decide whether the earlier method is suitable or requires an approved adjustment, approve the visual and quantitative comparison procedure, and execute both comparisons for the verified manual Cartesian 3D reconstruction.
    **Dependency:** 5.7 and 5.6
  - [ ] **5.9 [Ricardo] Record the Cartesian 3D manual execution and reference-comparison results**  
    Preserve the executed commands, effective settings, reference, inputs, outputs, figures, checks, observations, failures, corrections, and the observed visual and quantitative comparisons with the corresponding synthetic reference.
    **Dependency:** 5.8
  - [ ] **5.10 [Copilot] Review the Cartesian 3D manual evidence as an automation prerequisite**  
    Confirm that the Cartesian 3D procedure has been established, reviewed, executed, regenerated and verified, compared with its synthetic reference, and sufficiently evidenced before equivalent automation is developed.
    **Dependency:** 5.9

- [ ] **6.0 Establish, Review, Execute, and Record the Manual Cartesian 3D Compressed-Sensing Procedure**
  - [ ] **6.1 [Copilot] Identify the decisions required for the manual 3D compressed-sensing case**  
    Organize the open questions concerning controlled undersampling, sampling representation, synthetic preparation, reconstruction settings, outputs, checks, and reference comparison without selecting values.
    **Dependency:** 5.10
  - [ ] **6.2 [Copilot] Prepare and explain the proposed manual Cartesian 3D compressed-sensing procedure**  
    Develop a future technical proposal covering the candidate synthetic case, preparation and regeneration commands, controlled undersampling, reconstruction commands, required inputs, expected outputs, reference-comparison methods, mandatory checks, and evidence record, without selecting the scientific values in this task-planning response.
    **Dependency:** 6.1
  - [ ] **6.3 [Copilot] Review the proposed compressed-sensing procedure against the PRD**  
    Check that the proposal separates synthetic preparation, regeneration verification, manual reconstruction, reference comparison, and evidence recording, and does not assume negligible compressed-sensing error or general validity.
    **Dependency:** 6.2
  - [ ] **6.4 [Ricardo] Review, adjust, and approve the Cartesian 3D compressed-sensing procedure**  
    Review Copilot’s technical proposal, decide the required adjustments, and approve the preparation, controlled-undersampling, regeneration, reconstruction, comparison, checking, and recording procedures before execution.
    **Dependency:** 6.3
  - [ ] **6.5 [Ricardo] Prepare, regenerate, and verify the synthetic compressed-sensing case**  
    Execute the approved preparation and controlled-undersampling procedure, regenerate the intended synthetic case, and verify the reference, undersampled input, sampling information, and required metadata before performing the manual reconstruction.
    **Dependency:** 6.4
  - [ ] **6.6 [Ricardo] Execute the reviewed manual Cartesian 3D compressed-sensing reconstruction**  
    Run the approved manual reconstruction procedure using the verified prepared inputs and perform the required checks for the undersampled input and reconstructed output.
    **Dependency:** 6.5
  - [ ] **6.7 [Copilot] Prepare and explain the compressed-sensing reference-comparison application**  
    Propose how the reviewed visual and quantitative reference-comparison method should be applied to the compressed-sensing case, identifying case-specific preprocessing, reporting, and limitations without assuming negligible error or introducing an unreviewed metric or tolerance.
    **Dependency:** 4.3 and 6.4
  - [ ] **6.8 [Ricardo] Review, approve, and execute the compressed-sensing reference comparison**  
    Review the proposed application, decide whether the earlier method is suitable or requires an approved adjustment, approve the visual and quantitative comparison procedure, and execute both comparisons for the verified manual compressed-sensing reconstruction.
    **Dependency:** 6.7 and 6.6
  - [ ] **6.9 [Ricardo] Record the compressed-sensing manual execution and reference-comparison results**  
    Preserve commands, effective settings, sampling information, reference, inputs, outputs, figures, checks, observations, failures, corrections, and the observed visual and quantitative comparisons with the corresponding synthetic reference.
    **Dependency:** 6.8
  - [ ] **6.10 [Copilot] Review the compressed-sensing manual evidence as an automation prerequisite**  
    Confirm that the compressed-sensing procedure has been established, reviewed, executed, regenerated and verified, compared with its synthetic reference, and sufficiently evidenced before equivalent automation is developed.
    **Dependency:** 6.9

- [ ] **7.0 Design and Implement the Python Automation Equivalent**
  - [ ] **7.1 [Copilot] Confirm the manual-procedure readiness gate required by FR-22**  
    Verify that the 2D, 3D, and 3D compressed-sensing manual procedures have each been established, reviewed, executed, and documented before their equivalent automation is developed.
    **Dependency:** 4.6, 5.10, and 6.10
  - [ ] **7.2 [Copilot] Derive automation behavior from the reviewed manual procedures**  
    Identify the required input inspection, explicit configuration, reconstruction invocation, output handling, run association, optional figure generation, and error-reporting behaviors without fixing module names, function names, or configuration formats prematurely.
    **Dependency:** 7.1
  - [ ] **7.3 [Ricardo] Review the proposed automation decisions**  
    Review which information may be read or checked from supported inputs, which decisions must remain explicit configuration, and how the terminal workflow should be invoked non-interactively.
    **Dependency:** 7.2
  - [ ] **7.4 [Copilot] Prepare and explain the proposed FR-32 behavior**  
    Describe how invalid inputs, unsupported conditions, and execution failures could be surfaced explicitly, including expected reporting points and limitations, while preserving FR-32 as proposed behavior pending Ricardo’s review.
    **Dependency:** 7.3
  - [ ] **7.5 [Ricardo] Review and decide the proposed FR-32 behavior**  
    Review Copilot’s proposal, decide the required adjustments, and determine whether and how the behavior may be incorporated; this task does not mark FR-32 as accepted in advance.
    **Dependency:** 7.4
  - [ ] **7.6 [Copilot] Implement the reviewed Python automation in the existing repository areas**  
    Add only the reviewed automation under the repository’s existing `src/`, `configs/`, `tests/`, `scripts/`, and `environment/` organization as appropriate, without fixing module names, function names, or architecture solely to satisfy the task template.
    **Dependency:** 7.5
  - [ ] **7.7 [Copilot] Prepare static checks for the automated workflow**  
    Prepare code, configuration, interface, and non-interactive execution checks, including source-input preservation, separate run outputs, effective-setting association, and optional figure generation without a display window. Static review must not be presented as proof of execution.
    **Dependency:** 7.6
  - [ ] **7.8 [Ricardo] Execute the automated reconstruction commands and review the resulting evidence**  
    Execute the approved Python workflow for the 2D, 3D, and 3D compressed-sensing cases, then review the actual invocations, outputs, figures if generated, settings, checks, and failures. Optional automated figures remain optional and must not be treated as mandatory outputs.
    **Dependency:** 7.7
  - [ ] **7.9 [Copilot] Review the automated implementation and execution evidence**  
    Compare the recorded execution evidence with the established manual references, confirm coverage of all three cases, and distinguish actual execution evidence from static code or configuration review.
    **Dependency:** 7.8
  - [ ] **7.10 [Copilot] Prepare the automated reconstruction-to-reference comparisons**  
    Propose the application of the reviewed reference-comparison method to each automated 2D, 3D, and 3D compressed-sensing reconstruction, including case-specific reporting or limitation notes, without imposing a new metric or tolerance.
    **Dependency:** 4.3, 5.8, 6.8, and 7.9
  - [ ] **7.11 [Ricardo] Review and execute the automated reconstruction-to-reference comparisons**  
    Review the proposed application, decide required adjustments, and execute the approved visual and quantitative comparisons between each automated reconstruction and its corresponding synthetic reference.
    **Dependency:** 7.10
  - [ ] **7.12 [Copilot] Review the automated reference-comparison evidence**  
    Confirm that automated reference comparisons are recorded separately from manual–automated comparisons and identify missing evidence, failures, or unresolved interpretation limits.
    **Dependency:** 7.11

- [ ] **8.0 Compare Manual and Automated Reconstruction Routes**
  - [ ] **8.1 [Copilot] Define the comparison conditions for each reconstruction case**  
    Identify the prepared inputs, effective configurations, requested outputs, commands or invocations, and records required to compare the routes without selecting new scientific values implicitly.
    **Dependency:** 7.12
  - [ ] **8.2 [Ricardo] Review and approve the equivalence conditions for manual and automated runs**  
    Review Copilot’s proposed equivalence conditions and decide what constitutes equivalent effective configuration and equivalent requested output for the 2D, 3D, and compressed-sensing cases.
    **Dependency:** 8.1
  - [ ] **8.3 [Copilot] Propose and explain the numerical method for manual–automated comparison**  
    Prepare a method for comparing matched manual and automated reconstructions. The method may reuse an earlier reference-comparison method, but its application to route comparison must be reviewed separately; no new metric, tolerance, or pass/fail criterion is imposed here.
    **Dependency:** 8.2
  - [ ] **8.4 [Ricardo] Review and approve the numerical route-comparison method**  
    Review the proposed method, decide whether an earlier method can be reused or adjusted, and approve the calculation and reporting procedure before matched comparison runs are evaluated.
    **Dependency:** 8.3
  - [ ] **8.5 [Ricardo] Execute matched manual–automated comparison runs**  
    Use the same prepared synthetic inputs for each pair and preserve the conditions needed to distinguish route differences from synthetic-case preparation differences.
    **Dependency:** 8.4, 7.8, and the corresponding manual evidence from Tasks 3.0, 5.0, and 6.0
  - [ ] **8.6 [Ricardo] Compare the manual and automated outputs**  
    Record visual and approved numerical differences between each matched pair using the reviewed route-comparison method, without conflating route equivalence with similarity to the synthetic reference.
    **Dependency:** 8.5
  - [ ] **8.7 [Copilot] Review the route-comparison records**  
    Verify that each record identifies the case, shared prepared inputs, effective settings, requested outputs, produced outputs, comparison method, observed differences, and limitations, and that these records remain separate from reference comparisons and operator-intervention measurements.
    **Dependency:** 8.6

- [ ] **9.0 Measure Operator Intervention and Operational Outcomes**
  - [ ] **9.1 [Copilot] Draft operator-intervention definitions and counting rules**  
    Propose rules for commands, parameters, configuration decisions, checks, manual corrections, failures, and recovery, while excluding learning, development, one-time setup, individual keystrokes, and software-only operations where appropriate.
    **Dependency:** 8.7
  - [ ] **9.2 [Ricardo] Review and approve the intervention measurement protocol**  
    Establish the action granularity, inclusion and exclusion rules, treatment of failures and recovery, and comparable resource conditions before measurement runs begin.
    **Dependency:** 9.1
  - [ ] **9.3 [Copilot] Prepare the intervention recording checklist**  
    Prepare a reviewable checklist that can be applied consistently to manual and automated executions without requiring interactive behavior from the workflow.
    **Dependency:** 9.2
  - [ ] **9.4 [Ricardo] Execute the planned operational measurement runs**  
    Apply the approved counting rules to matched manual and automated runs under comparable conditions, recording failures and recovery separately.
    **Dependency:** 9.3
  - [ ] **9.5 [Ricardo] Calculate and review operator-intervention outcomes**  
    Produce the approved absolute and percentage comparisons, if applicable, and review whether the evidence supports an operational observation without overstating causality or generality.
    **Dependency:** 9.4
  - [ ] **9.6 [Copilot] Confirm that intervention measurement did not block the initial 2D tutorial**  
    Verify that the first tutorial and its preliminary reference comparison were completed independently of the later operational measurement protocol.
    **Dependency:** 4.6 and 9.5

- [ ] **10.0 Consolidate Verification Evidence and Reproducibility Records**
  - [ ] **10.1 [Copilot] Define the evidence index across all workflow stages**  
    Organize records for synthetic preparation, regeneration verification, manual procedures, automated procedures, reference comparisons, manual–automated comparisons, and operator-intervention measurements as separate evidence categories.
    **Dependency:** 7.12, 8.7, and 9.5
  - [ ] **10.2 [Copilot] Map each record to the relevant PRD requirements**  
    Trace planned and completed evidence to applicable requirements, including FR-22, FR-32, FR-33 through FR-40, and the separate comparison obligations.
    **Dependency:** 10.1
  - [ ] **10.3 [Ricardo] Review reproducibility and regeneration evidence**  
    Confirm that each synthetic case has evidence of both preparation and regeneration verification, and that logs or collected records have not been treated as substitutes for checking the regenerated case.
    **Dependency:** 10.1
  - [ ] **10.4 [Copilot] Identify unresolved decisions and limitations in the final records**  
    Preserve open questions about metrics, tolerances, input semantics, interface details, architecture, and future ARC or HPC use rather than presenting them as resolved.
    **Dependency:** 10.2 and 10.3
  - [ ] **10.5 [Ricardo] Review the consolidated evidence package**  
    Confirm that the records distinguish reference similarity, manual–automated equivalence, and operator intervention, and that the 64 × 64 exploratory exercise is not presented as general validation or clean-checkout reproduction.
    **Dependency:** 10.4
  - [ ] **10.6 [Copilot] Prepare the verification summary for subsequent review**  
    Summarize completed checks, observed results, failed or incomplete checks, and remaining decisions without modifying the PRD or claiming implementation that has not been executed and reviewed.
    **Dependency:** 10.5

## Relevant Files

### Existing files

- [`tasks/prd-bart-reconstruction-workflow.md`](./prd-bart-reconstruction-workflow.md) — Reviewed software requirements, proposed FR-32 behavior, FR-22 sequencing constraint, comparison requirements, and staged open questions.
- [`README.md`](../README.md) — Project scope, current evidence, exploratory 64 × 64 limitation, and repository organization.
- [`tests/synthetic_2d/README.md`](../tests/synthetic_2d/README.md) — Existing documented synthetic 2D procedure and current limitations.
- [`scripts/check_fourier_numpy.py`](../scripts/check_fourier_numpy.py) — Existing independent NumPy comparison script; its current 64 × 64 behavior must not be generalized without review.
- [`scripts/visualize_synthetic.py`](../scripts/visualize_synthetic.py) — Existing synthetic visualization support.
- [`src/README.md`](../src/README.md) — Current source-area documentation.
- [`configs/README.md`](../configs/README.md) — Current configuration-area documentation.
- [`tests/README.md`](../tests/README.md) — Current test-area documentation.
- [`results/familiarization-2d-20261023/README.md`](../results/familiarization-2d-20261023/README.md) — Existing exploratory 2D evidence and limitations.
- [`docs/open-questions.md`](../docs/open-questions.md) — Related unresolved project, input, environment, verification, and publication questions.

### Planned locations, subject to review

- `src/` — Future Python automation, with modules and function names left undefined.
- `configs/` — Future reviewed configuration material, with format and schema left undefined.
- `tests/` — Future synthetic fixtures, regression checks, and comparison tests, with case structure left undefined.
- `scripts/` — Future supporting preparation, evidence, or reporting scripts, if approved.
- `results/` — Future reviewed run records, figures, and comparison evidence, subject to the repository’s evidence organization.
- `environment/` — Future dependency or execution documentation, if needed.

### Intentionally undefined until decisions are reviewed

- The concrete Python module and function names.
- The terminal entry point and command-line argument names.
- The configuration file format and schema.
- The run-directory naming convention.
- The exact metric and calculation procedure.
- Numerical tolerances and pass/fail criteria.
- The operator-action counting granularity.
- The exact 2D, 3D, and compressed-sensing phantom, dimensions, sampling, channels, and BART parameters.
