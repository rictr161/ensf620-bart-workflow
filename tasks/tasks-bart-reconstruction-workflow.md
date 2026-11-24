# BART Reconstruction Workflow Development Tasks

Source: [Product Requirements Document](./prd-bart-reconstruction-workflow.md)

This task list is based on the reviewed PRD. It preserves the manual-before-automation
sequence, keeps unresolved scientific and interface decisions at the stage where they
are needed, and records the approved FR-32 behavior while keeping implementation
details staged. Tasks remain
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

- [x] **5.0 Establish, Review, Execute, and Record the Manual Cartesian 3D Procedure**
  - [x] **5.1 [Copilot] Identify the decisions required for the manual Cartesian 3D case**\
    Organize the later-stage questions concerning the synthetic case, dimensions, input characteristics, reconstruction procedure, output representation, mandatory checks, and reference comparison without selecting their values.
    **Dependency:** 4.6
    **Status:** Complete. The accepted 3D case, dimensions, sampling, channel configuration, input roles, reconstruction procedure, output representation, checks, and comparison decisions were established before drafting the procedure.
  - [x] **5.2 [Copilot] Prepare and explain the proposed manual Cartesian 3D procedure**\
    Develop a technical proposal covering the confirmed candidate synthetic case, preparation and regeneration commands, reconstruction commands, required inputs, expected outputs, reference-comparison methods, mandatory checks, and evidence record.
    **Dependency:** 5.1
    **Status:** Complete. The complete manual Cartesian 3D procedure is drafted and reviewed statically; the later execution tasks record the owner-reported execution evidence.
  - [x] **5.3 [Copilot] Review the proposed Cartesian 3D procedure against the PRD**\
    Check that the proposal separates synthetic preparation, regeneration verification, manual reconstruction, reference comparison, and evidence recording while preserving the manual-first sequence and avoiding experimental input requirements.
    **Dependency:** 5.2
    **Review:** The procedure covers the confirmed BART-generated 64 × 64 × 64, fully sampled, single-channel synthetic case; preserves reference and k-space inputs; separates preparation, regeneration verification, reconstruction, structural checks, visual comparison, quantitative comparison, and execution records; uses non-interactive figure generation; and keeps comparison results case-specific without tolerances or pass/fail criteria. No material inconsistency with the reviewed PRD or accepted decisions was found. Ricardo's review and approval are recorded in Task 5.4. The only correction identified during review was the regeneration-record path wording in Section 9, which now explicitly refers to the second preparation directory.
  - [x] **5.4 [Ricardo] Review, adjust, and approve the Cartesian 3D manual procedure**\
    Review Copilot’s technical proposal, decide the required adjustments, and approve the preparation, regeneration, reconstruction, comparison, checking, and recording procedures before execution.
    **Dependency:** 5.3
    **Status:** Complete. Ricardo reviewed and approved the procedure before the reported preparation and reconstruction execution; no separate approval date is asserted.
  - [x] **5.5 [Ricardo] Prepare, regenerate, and verify the synthetic Cartesian 3D case**\
    Execute the approved preparation procedure, regenerate the intended synthetic case, and verify the reference, corresponding reconstruction input, and required metadata before performing the manual reconstruction.
    **Dependency:** 5.4
    **Evidence:** `generation-3d-01` and `generation-3d-02` passed reference and k-space structural checks. The two `.cfl` comparisons returned `MATCH` with exit code `0`; the two `.hdr` comparisons returned `DIFFERENT` with exit code `1`, and Ricardo's supplied diffs showed only expected generation-directory paths in `# Command` and `# Files`.
  - [x] **5.6 [Ricardo] Execute the reviewed manual Cartesian 3D reconstruction**\
    Run the approved manual reconstruction procedure using the verified prepared synthetic inputs and perform the required stage and output checks.
    **Dependency:** 5.5
    **Evidence:** BART reconstructed from `generation-3d-01` to `manual-3d-01` with exit code `0`; the structural output check returned `VALID` with exit code `0`.
  - [x] **5.7 [Copilot] Prepare and explain the Cartesian 3D reference-comparison application**\
    Propose how the reviewed visual and quantitative reference-comparison method should be applied to the Cartesian 3D case, identifying any case-specific preprocessing, reporting, or limitation decisions without imposing a new metric or tolerance.
    **Dependency:** 4.3 and 5.4
    **Status:** Complete. The tutorial applies the reviewed visual method to three zero-based orthogonal index-32 slices and the reviewed complex relative L2 method to the complete volume without preprocessing, while keeping the comparison case-specific.
  - [x] **5.8 [Ricardo] Review, approve, and execute the Cartesian 3D reference comparison**\
    Review the proposed application, decide whether the earlier method is suitable or requires an approved adjustment, approve the visual and quantitative comparison procedure, and execute both comparisons for the verified manual Cartesian 3D reconstruction.
    **Dependency:** 5.7 and 5.6
    **Evidence:** Static figure generation returned exit code `0`; Ricardo reported no visually appreciable differences in the displayed slices. The log reported reconstruction slice magnitudes above the fixed display maximum; no cause was inferred. The complete-volume complex relative L2 error was `1.729089800e-07` with exit code `0`. No tolerance or numerical pass/fail criterion was applied.
  - [x] **5.9 [Ricardo] Record the Cartesian 3D manual execution and reference-comparison results**\
    Preserve the executed commands, effective settings, reference, inputs, outputs, figures, checks, observations, failures, corrections, and the observed visual and quantitative comparisons with the corresponding synthetic reference.
    **Dependency:** 5.8
    **Evidence:** The supplied execution evidence identifies the preparations, reconstruction output, structural check, static figure and quantitative comparison. The optional cumulative `run-record.md` remains optional and is not required for this task.
  - [x] **5.10 [Copilot] Review the Cartesian 3D manual evidence as an automation prerequisite**\
    Confirm that the Cartesian 3D procedure has been established, reviewed, executed, regenerated and verified, compared with its synthetic reference, and sufficiently evidenced before equivalent automation is developed.
    **Dependency:** 5.9
    **Review:** Complete static evidence review found the procedure and supplied evidence sufficient for the manual 3D prerequisite. The evidence remains case-specific; clean-checkout reproduction, general validation, experimental inputs, formal tolerances, and manual–automated equivalence remain unconfirmed. The optional interactive viewer closed normally with the resolved `macosx` backend; Ricardo confirmed its operation and visual observations, but complete slice inspection is not claimed.

- [x] **6.0 Establish, Review, Execute, and Record the Manual Cartesian 3D Compressed-Sensing Procedure**
  - [x] **6.1 [Copilot] Identify the decisions required for the manual 3D compressed-sensing case**\
    Organize the open questions concerning controlled undersampling, sampling representation, synthetic preparation, reconstruction settings, outputs, checks, and reference comparison without selecting values.
    **Dependency:** 5.10
    **Progress:** Complete. The candidate case and mask decisions were identified and reviewed. Ricardo confirmed the synthetic dimensions, axis convention, sensitivity representation, Poisson/repetition settings, nominal acceleration distinction, and candidate `pics` settings. These confirmations do not approve the complete procedure or claim execution.
  - [x] **6.2 [Copilot] Prepare and explain the manual Cartesian 3D compressed-sensing procedure for the confirmed case**\
    Develop the procedure covering the confirmed synthetic case, preparation and regeneration commands, controlled undersampling, reconstruction commands, required inputs, expected outputs, reference-comparison methods, mandatory checks, and evidence record.
    **Dependency:** 6.1
    **Progress:** The manual Cartesian 3D compressed-sensing procedure is drafted through Section 12. Execution, result review, and effective evidence preservation belong to later tasks and are not claimed here.
  - [x] **6.3 [Copilot] Review the proposed compressed-sensing procedure against the PRD**\
    Check that the proposal separates synthetic preparation, regeneration verification, manual reconstruction, reference comparison, and evidence recording, and does not assume negligible compressed-sensing error or general validity.
    **Dependency:** 6.2
    **Review:** Complete static review of the CS tutorial against the reviewed PRD, confirmed case decisions, and the existing 3D support found no material pending issue. The review covered preparation, mask generation and validation, constant sensitivities, regeneration and header review, session recovery, reconstruction, structural checks, visual and quantitative comparisons, execution records, shared paths and filenames, and separation of operational results, human observations, and quality interpretation. No execution, tolerance, acceptance criterion, automation, or result was introduced or claimed.
  - [x] **6.4 [Ricardo] Review, adjust, and approve the Cartesian 3D compressed-sensing procedure**\
    Review Copilot’s technical proposal, decide the required adjustments, and approve the preparation, controlled-undersampling, regeneration, reconstruction, comparison, checking, and recording procedures before execution.
    **Dependency:** 6.3
    **Status:** Complete. Ricardo approved the procedure before guided execution; no approval date is asserted.
  - [x] **6.5 [Ricardo] Prepare, regenerate, and verify the synthetic compressed-sensing case**\
    Execute the approved preparation and controlled-undersampling procedure, regenerate the intended synthetic case, and verify the reference, undersampled input, sampling information, and required metadata before performing the manual reconstruction.
    **Dependency:** 6.4
    **Evidence:** The two local preparation records document the six preserved pairs, owner-reported generation statuses where logs are empty, structural checks, mask counts and effective acceleration, exact mask application checks, constant sensitivities, and the twelve regeneration comparisons. The original header differences remain `DIFFERENT`; their reviewed path-only diffs are preserved. The mask retained 583 of 4096 phase-plane positions and 37312 of 262144 positions in the repeated 3D mask, giving a sampling fraction of 0.142333984375 and an effective acceleration of 7.02572898799, distinct from the nominal per-axis product 2 × 2 = 4.
  - [x] **6.6 [Ricardo] Execute the reviewed manual Cartesian 3D compressed-sensing reconstruction**\
    Run the approved manual reconstruction procedure using the verified prepared inputs and perform the required checks for the undersampled input and reconstructed output.
    **Dependency:** 6.5
    **Evidence:** The reconstruction used `generation-3d-cs-01`, returned BART exit code `0`, and its structural check returned `VALID` with exit code `0`; the local run record preserves the settings and evidence links.
  - [x] **6.7 [Copilot] Prepare and explain the compressed-sensing reference-comparison application**\
    Propose how the reviewed visual and quantitative reference-comparison method should be applied to the compressed-sensing case, identifying case-specific preprocessing, reporting, and limitations without assuming negligible error or introducing an unreviewed metric or tolerance.
    **Dependency:** 4.3 and 6.4
    **Status:** Complete. The tutorial documents the approved case-specific visual and full-volume complex relative L2 comparison without preprocessing, tolerance, or pass/fail classification.
  - [x] **6.8 [Ricardo] Review, approve, and execute the compressed-sensing reference comparison**\
    Review the proposed application, decide whether the earlier method is suitable or requires an approved adjustment, approve the visual and quantitative comparison procedure, and execute both comparisons for the verified manual compressed-sensing reconstruction.
    **Dependency:** 6.7 and 6.6
    **Evidence:** Ricardo approved and executed the comparisons. Static figure generation, the optional viewer, and quantitative comparison returned exit code `0`; the observed complex relative L2 error was `2.473308708e-01`, with no quality acceptance criterion applied. In the inspected slices, Ricardo reported a noisy appearance in the CS reconstruction, while the main shapes remained distinguishable.
  - [x] **6.9 [Ricardo] Record the compressed-sensing manual execution and reference-comparison results**\
    Preserve commands, effective settings, sampling information, reference, inputs, outputs, figures, checks, observations, failures, corrections, and the observed visual and quantitative comparisons with the corresponding synthetic reference.
    **Dependency:** 6.8
    **Evidence:** `preparation-record.txt` exists in both preparation directories and `run-record.md` exists in the reconstruction directory. They link the local logs and figure, retain the original comparison outcomes and incidents, and record Ricardo’s visual observation separately from automated results.
  - [x] **6.10 [Copilot] Review the compressed-sensing manual evidence as an automation prerequisite**\
    Confirm that the compressed-sensing procedure has been established, reviewed, executed, regenerated and verified, compared with its synthetic reference, and sufficiently evidenced before equivalent automation is developed.
    **Dependency:** 6.9
    **Review:** Complete static review of the tutorial, local preparation records, reconstruction run record, headers and available logs found the manual CS prerequisite sufficiently established for the next planning gate. The evidence remains case-specific and does not establish convergence, a quality threshold, general validation or clean-checkout reproducibility.

- [x] **7.0 Design and Implement the Python Automation Equivalent**
  **Completion:** Complete. Tasks 7.1–7.12 are complete, with implementation, static review, owner-run executions, comparison proposal, reported automated reference evaluations, and evidence review recorded below. This closes Block 7 only; Tasks 8.0 onward remain open. The final operator guide `docs/automated-workflow.md` remains a later documentation deliverable and is not claimed as created here.
  - [x] **7.1 [Copilot] Confirm the manual-procedure readiness gate required by FR-22**\
    Verify that the fully sampled Cartesian 2D, fully sampled Cartesian 3D, and Cartesian 3D compressed-sensing manual procedures have each been established, reviewed, executed, and documented before their equivalent automation is developed.
    **Dependency:** 4.6, 5.10, and 6.10
    **Review:** Complete. Static review of [the manual Cartesian 2D tutorial](../docs/tutorials/manual-cartesian-2d.md), [the manual Cartesian 3D tutorial](../docs/tutorials/manual-cartesian-3d.md), [the manual Cartesian 3D compressed-sensing tutorial](../docs/tutorials/manual-cartesian-3d-cs.md), [the PRD FR-22 requirement](./prd-bart-reconstruction-workflow.md#python-automation), [the task evidence for 4.6, 5.10, and 6.10](./tasks-bart-reconstruction-workflow.md), [the README evidence summary](../README.md#available-evidence), and [the AI-use record](../AI_USE.md) confirmed the readiness gate for fully sampled Cartesian 2D, fully sampled Cartesian 3D, and Cartesian 3D CS. Each case has a documented and reviewed procedure; preparation/regeneration and structural checks; a reported manual reconstruction and output check; visual and quantitative reference-comparison records; and preserved case-specific evidence. Operational results, Ricardo's observations, and quality interpretation remain distinct. This review did not execute or reproduce any procedure, add a tolerance, establish quality acceptance, or close 7.0; it confirms only the FR-22 prerequisite for deriving equivalent automation.
  - [x] **7.2 [Copilot] Derive automation behavior from the reviewed manual procedures**\
    Identify the required input inspection, explicit configuration, reconstruction invocation, output handling, run association, optional figure generation, and error-reporting behaviors without fixing module names, function names, or configuration formats prematurely.
    **Dependency:** 7.1
    **Proposal:** Complete. [Proposed Python automation behavior](../docs/python-automation-behavior.md) derives the seven required behavior areas from the reviewed manual procedures and applicable PRD requirements. It covers prepared BART-compatible k-space inputs, explicit sampling information and known acquisition acceleration, case-specific reconstruction inputs and checks, source preservation, separate run outputs, effective-setting traceability, optional non-interactive figures, and detectable problem-reporting points. The proposal does not implement code, select new defaults, fix interfaces or configuration formats, or approve FR-32; these decisions remain subject to Ricardo's review in 7.3 and later tasks.
  - [x] **7.3 [Ricardo] Review the proposed automation decisions**\
    Review which information may be read or checked from supported inputs, which decisions must remain explicit configuration, and how the terminal workflow should be invoked non-interactively.
    **Dependency:** 7.2
    **Review:** Complete. Ricardo reviewed and accepted the behavior decisions documented in [the proposed automation behavior](../docs/python-automation-behavior.md): one readable non-interactive entry; prepared BART-compatible k-space; explicit Cartesian dimensionality and CS selection; configurable parameters with documented modifiable defaults where appropriate; automatic file inspection and compatibility checks; conditional supplied-map or explicitly requested `ecalib` sensitivity routes; supplied or explicitly requested and checked sampling information; stage results, separate run directories, effective-parameter records, and optional saved figures. At that review checkpoint, sampling estimation, CS 2D, `ecalib`, and multiple ESPIRiT map sets were noted for bounded manual checks. Ricardo later reported the manual 3D multichannel `ecalib` case under 7.6. On 2026-11-23 Ricardo removed Cartesian 2D CS from the December 1 delivery scope; that supersedes its earlier inclusion as a delivery capability, not the historical review record. Ricardo subsequently reported the manual `bart pattern` check and the automated `bart-pattern` execution under 7.8; Task 7.8 is complete. Multiple map sets remain a separate unsupported capability. The accepted local/ARC-usable entry is a non-interactive interface objective; ARC deployment or execution is not required for the December 1 delivery under the PRD and has not been verified. This completion records behavior review only and does not claim implementation, execution, or scientific validation.
  - [x] **7.4 [Copilot] Prepare and explain the proposed FR-32 behavior**\
    Describe how invalid inputs, unsupported conditions, and execution failures could be surfaced explicitly, including expected reporting points and limitations, while preserving FR-32 as proposed behavior pending Ricardo’s review.
    **Dependency:** 7.3
    **Proposal:** Complete. [The automation behavior](../docs/python-automation-behavior.md#10-proposed-fr-32-behavior) defines the bounded FR-32 policy covering absent or invalid files, incompatible configuration, unsupported inputs, unavailable BART, failed commands, failed checks, existing outputs, and optional figure failures. It preserves inputs and existing results, avoids silent parameter changes and output reuse, and distinguishes figure failures from reconstruction results. It does not add automatic retries, fallback, complex recovery, or cleanup. Ricardo approved the response and exit-code policy in 7.5.
  - [x] **7.5 [Ricardo] Review and decide the proposed FR-32 behavior**\
    Review Copilot’s proposal, decide the required adjustments, and determine whether and how the behavior may be incorporated; this task does not mark FR-32 as accepted in advance.
    **Dependency:** 7.4
    **Review:** Complete. Ricardo approved the FR-32 policy: mandatory operation or check failures stop dependent stages; actual operation and subsequent check results are recorded separately; inputs, records, and produced files are preserved; destination collisions fail explicitly without interaction, overwrite, or automatic reuse; no automatic retries, parameter changes, alternate routes, or deletion occur; mandatory success returns `0`, mandatory failure returns non-zero, and optional figure-only failures are reported separately without invalidating a valid reconstruction.
  - [x] **7.6 [Copilot] Implement the reviewed Python automation in the existing repository areas**
    Add only the reviewed automation under the repository’s existing `src/`, `configs/`, `tests/`, `scripts/`, and `environment/` organization as appropriate, without fixing module names, function names, or architecture solely to satisfy the task template.
    **Dependency:** 7.5
    **Progress:** Implementation complete; static review found no remaining functional implementation gap within Task 7.6. [`src/bart_workflow.py`](../src/bart_workflow.py) provides reusable `run_reconstruction` and a terminal entry point for prepared BART k-space: fully sampled single-channel Cartesian 2D/3D inverse-FFT routes and Cartesian 3D CS with supplied sensitivity maps or explicitly requested `ecalib`. It supports one ESPIRiT map set, the reviewed `manual-cartesian-3d-cs` profile, and explicit `provided` or `bart-pattern` sampling sources. Optional reconstruction figures are saved non-interactively. Defaults, effective settings, source semantics, and limitations are documented in [`src/README.md`](../src/README.md) and [`docs/python-automation-behavior.md`](../docs/python-automation-behavior.md). After k-space validation, the `runtime-environment` stage records the Python executable/version, imported NumPy version, OS details and architecture, configured BART executable, and the `version -V` command, exit code, and response; `bart-version.log` is mandatory, and a query or log-write failure stops dependent processing and is recorded. Matplotlib is imported and versioned only in the requested optional figure path. This implementation-status assessment is distinct from execution evidence: Ricardo's latest 7.8 report exercises the version query and automated `bart-pattern` route in one synthetic case, while the earlier local runs recorded below predate the runtime-environment stage. The static-check matrix is recorded under 7.7. The delivery scope remains fully sampled Cartesian 2D and 3D plus Cartesian 3D CS; Cartesian 2D CS and radial are out of scope, and multiple map sets remain unsupported. Automated reference evaluations using the existing tutorial blocks are recorded under Tasks 7.10–7.12; no general comparison CLI was added to this implementation. The final operator guide `docs/automated-workflow.md` remains planned after the interface is settled and is not a functional implementation gap for this task.
    **Manual evidence:** Ricardo reported a BART v1.0.00 run using `$HOME/bart-learning/bart-workflow-preparations/generation-3d-ecalib-01/kspace_undersampled` and the preserved `$HOME/bart-learning/bart-workflow-preparations/generation-3d-cs-01/mask3d`, with output under `$HOME/bart-learning/bart-workflow-reconstructions/manual-3d-ecalib-01`. The input was 64 × 64 × 64 with eight channels and singleton later axes. The mask check reported 37,312 acquired and 224,832 omitted spatial positions, exact acquired-value equality across all channels, zeros at omitted positions, and a fully sampled 64 × 16 × 16 center. Ricardo reported `ecalib -r 64:16:16 -k 6:6:6 -t 0.001 -c 0.8 -m 1` returning `0`; generated sensitivity and eigenvalue pairs passed dimensions, binary-size, and finite-value checks, the sensitivity maps were not completely zero, and one ESPIRiT set was used for eight channels. The subsequent `pics --fista --wavelet dau2 -R W:7:0:0.01 -i 100 -s 0.95 -n -w 1` run used the preserved mask and generated maps and returned `0`. Ricardo reports that the reconstruction passed the existing structural check as 64 × 64 × 64, singleton on later axes, complex64 and finite. This is owner-reported manual evidence for that synthetic case only; the automated results are recorded separately below. ChatGPT guided the manual execution, and Ricardo executed and supplied the results.
    **Automated execution and comparison evidence:** Ricardo reported running the Python workflow locally with the same k-space and mask, writing to `$HOME/bart-learning/bart-workflow-reconstructions/automated-3d-ecalib-01`; the complete invocation returned `0`. The generated `ecalib.log` records BART code `0` and `-r 64:16:16 -k 6:6:6 -t 0.001 -c 0.8 -m 1`. The `pics` invocation used generated sensitivities from the automated directory, the supplied mask and k-space, and `--fista --wavelet dau2 -R W:7:0:0.01 -i 100 -s 0.95 -n -w 1.0`; its `reconstruction.log` records code `0`. Ricardo reports that `stage-records.json` contains eight successful stages, each with code `0`: `input-inspection`, `sampling-check`, `ecalib-input-check`, `ecalib`, `ecalib-output-check`, `sampling-and-sensitivity-checks`, `reconstruction`, and `reconstruction-output-check`. Calibration and reconstruction `log_error` values are `null`; effective settings and generated-map paths are recorded. Ricardo's `cmp` comparisons between the manual and automated run directories returned `0` for `sensitivities.cfl`, `eigenvalues.cfl`, and `reconstruction.cfl`, establishing byte-for-byte identity for those three files in this case. This is not an automated comparison to a synthetic reference, general validation, ARC execution, convergence evidence, or scientific quality acceptance. ChatGPT statically reviewed the implementation and guided execution and comparisons; Ricardo executed and provided results; Copilot implemented the route and is applying this documentary consolidation.
  - [x] **7.7 [Copilot] Prepare static checks for the automated workflow**
    Prepare code, configuration, interface, and non-interactive execution checks for the three delivery cases and supported 3D CS sensitivity and sampling sources, including invalid source combinations, source-input preservation, separate run outputs, effective-setting and software/environment-version association, and the required optional figure-generation capability without a display window. Figure generation may be omitted from an individual run; its implementation and checks remain in scope under FR-31. Static review must not be presented as proof of execution.
    **Dependency:** 7.6
    **Evidence:** Before the current `ecalib` integration, Ricardo reported that in-memory syntax compilation and terminal `--help` each returned exit code `0`. An earlier Pylance syntax-check request timed out and remains inconclusive. ChatGPT later performed a static review by reading the implementation and documentation and guided the reported execution checks. Existing automated runs cover the supplied-mask and `ecalib` route, and Ricardo's manual `bart pattern` check by itself does not exercise the new automated source selection. The source route, invalid-combination behavior, and runtime-environment/version records were also reviewed statically; the matrix below separates those findings from owner-reported execution evidence.
    **Check matrix:**

    | Check | Method | Evidence and limits |
    |---|---|---|
    | Case routes, CLI/configuration, and sampling-source combinations | Static review of configuration validation, CLI parsing, and command construction; Pylance diagnostics were reported with no errors | Confirmed `provided` requires a mask, `bart-pattern` rejects a simultaneous mask, FFT rejects `bart-pattern`, and an invalid provided mask does not fall back. The generated mask is checked before calibration and the same effective mask reaches `pics`. Negative source-combination cases were not separately executed. |
    | Source preservation, run isolation, and destination guard | Static review of input use and write targets; Ricardo's existing-output guard execution | Input k-space is passed as BART input and generated records/files target the new run directory. The reported collision returned `1` and `cmp` confirmed the pre-existing dummy stage record was unchanged. No source-input checksum comparison was reported. |
    | Non-interactive route and setting coverage | Ricardo's reported CLI executions and stage/log records across 2D FFT, 3D FFT, 3D CS with supplied maps/mask, 3D CS with `ecalib`, and 3D CS with `bart-pattern` plus `ecalib` | The current pattern/`ecalib` case records 11 successful stages; the associated BART commands each returned `0`. Its global CLI exit code was not supplied. Historical runs retain their own case-specific outcomes. |
    | Effective settings and environment association | Static review of stage-record generation and Ricardo's shared current-run records | The current run records the selected profile and resolved `pics` settings, BART `v1.0.00`, Python `3.13.17`, NumPy `2.5.4`, Darwin, and `arm64`; reported log-write error fields are `null`. |
    | Optional figures without a display | Static review of the `FigureCanvasAgg` path and lazy Matplotlib import; Ricardo's reported figure-enabled runs | Earlier 2D/3D figure runs recorded successful figure stages and were visually reviewed by Ricardo. The latest 3D figure stage records Matplotlib `3.11.2` and the PNG path as successful; no new human visual inspection was reported. |

    **Review result:** Complete. The matrix distinguishes static checks from owner-reported execution evidence. It does not claim that negative source combinations or every FR-32 failure path were run; those are not additional closure conditions in this task.
  - [x] **7.8 [Ricardo] Execute the automated reconstruction commands and review the resulting evidence**
    Execute and review the approved Python workflow for fully sampled Cartesian 2D, fully sampled Cartesian 3D, and Cartesian 3D CS. The 3D CS evidence must cover the supported supplied-sensitivity and `ecalib` paths and exercise the selected sampling-source behavior, including the newly implemented `bart-pattern` path. Review actual invocations, outputs, settings, version/environment records, checks, and failures; figures may be omitted for an individual run and are not mandatory outputs.
    **Dependency:** 7.7
    **Evidence:** Ricardo reported three earlier local runs: `generation-01/kspace` to `automated-2d-01/reconstruction`, compared with `manual-2d-01/reconstruction.cfl`; `generation-3d-01/kspace` to `automated-3d-01/reconstruction`, compared with `manual-3d-01/reconstruction.cfl`; and `generation-3d-cs-01/kspace_undersampled` with that generation's `mask3d` and `sensitivities` to `automated-3d-cs-01/reconstruction`, compared with `manual-3d-cs-01/reconstruction.cfl`. The recorded operations were `fft -i -u 3`, `fft -i -u 7`, and `pics` with the explicit `manual-cartesian-3d-cs` profile. All three stage records report BART exit code `0`, successful structural checks, and `log_error: null`; each automated run directory contains the reconstruction pair, log, and stage record. Ricardo ran `cmp` against each listed manual `.cfl`; all returned exit code `0`, establishing byte-for-byte equality for those run pairs. His `output-guard-VxO0l5` check returned `1` for an existing destination, preserved its original dummy stage record (`cmp` exit code `0`), and left only that record in the directory. Ricardo subsequently reported the local multichannel `ecalib` run and eight successful stages described under 7.6; `cmp` returned `0` for the manual/automated sensitivity, eigenvalue, and reconstruction `.cfl` pairs. The earlier three route runs predate this `ecalib` integration; the new run is additional case-specific evidence, not a comparison to a synthetic reference. These earlier runs also predate the runtime-environment/version stage and do not verify it; the latest pattern/`ecalib` evidence below does. The actual global CLI result for that latest run was not provided.
    **Manual sampling-pattern evidence:** Ricardo reported the command `bart pattern <kspace_undersampled> <sampling_mask>` using the `generation-3d-ecalib-01/kspace_undersampled` input and output under `sampling-check-CCWi6Z/sampling_mask`. The generated mask header declares dimensions `64 64 64`, with later axes singleton, and creator `BART v1.0.00`. `cmp` between the generated mask `.cfl` and the known `generation-3d-cs-01/mask3d` `.cfl` returned `0`. Ricardo did not report the `bart pattern` process exit code; the `cmp` result is not used to infer it. This manual check remains distinct from the automated `--sampling-source bart-pattern` execution documented below.
    **Figure evidence:** Ricardo reported local fully sampled Cartesian 2D and 3D FFT runs with `--save-figures`, writing to `automated-2d-figures-01` and `automated-3d-figures-01`; both global exit codes were `0`. Each `stage-records.json` records `reconstruction-figure` as `success` with exit code `0` and the run-relative path `figures/reconstruction.png`. The 2D figure represents the complete 64 × 64 image. The 3D figure represents three central planes of the 64 × 64 × 64 volume at indices `[32, 32, 32]`. The records include magnitude limits and presentation settings, and Ricardo confirmed both visualizations display correctly. ChatGPT statically reviewed the implementation and guided the checks; Ricardo executed the runs and reviewed the figures; Copilot implemented the option and updated the documentation. This owner-reported evidence covers normal figure generation in these cases only; it does not verify all figure failure paths.
    **Automated pattern/`ecalib` evidence:** Ricardo reported the run in `automated-3d-pattern-ecalib-01` using `generation-3d-ecalib-01/kspace_undersampled`, `sampling_source="bart-pattern"` without a supplied mask, and `sensitivity_source="ecalib"` without supplied sensitivities. The run used calibration region `64:16:16`, kernel `6:6:6`, threshold `0.001`, crop `0.8`, one map set, the `manual-cartesian-3d-cs` profile, and requested figures. BART `version -V`, `pattern`, `ecalib`, and `pics` each recorded code `0`; all 11 stages report `success` with code `0`. The generated mask passed checks and was used by `pics -p`; `pics` used the maps generated by `ecalib` in the same run directory. The effective profile settings recorded FISTA, `dau2`, regularization `0.01`, 100 iterations, step `0.95`, random shift disabled, and data scaling `1.0`. The structural output check succeeded. The environment record reports BART `v1.0.00`, Python `3.13.17`, NumPy `2.5.4`, Darwin, and `arm64`; the figure stage reports Matplotlib `3.11.2`, shape `64 × 64 × 64`, central indices `[32, 32, 32]`, and `figures/reconstruction.png`. Shared log-write error fields are `null`. Ricardo did not report the global CLI exit code or a new human visual inspection of this figure.

    **Automated-to-automated comparison:** Ricardo reported `cmp` exit code `0` for `reconstruction.cfl` from `automated-3d-ecalib-01` versus `automated-3d-pattern-ecalib-01`. This establishes byte-for-byte identity between the two automated outputs for this case only; it is not a direct manual comparison or comparison to a synthetic reference.

    **Review result:** Complete. The reported executions cover the three delivery cases, supplied-map and `ecalib` CS routes, and both supplied-mask and `bart-pattern` sampling behavior. The global CLI result for the latest run is unreported and is not inferred; the recorded operation and stage outcomes satisfy the stated review criteria. Figure generation is recorded as successful, without claiming a new human visual review. This evidence does not establish ARC compatibility, general scientific quality, convergence, or reference-comparison completion.
  - [x] **7.9 [Copilot] Review the automated implementation and execution evidence**
    Compare the recorded execution evidence with the established manual references, confirm coverage of the three delivery cases and the supported 3D CS sensitivity paths, and distinguish actual execution evidence from static code or configuration review.
    **Dependency:** 7.8
    **Review:** Complete. The recorded manual-to-automated `.cfl` comparisons cover fully sampled Cartesian 2D, fully sampled Cartesian 3D, and Cartesian 3D CS; the multichannel `ecalib` case also has direct manual-to-automated identity results for sensitivities, eigenvalues, and reconstruction. The evidence confirms the supplied-sensitivity and `ecalib` paths and distinguishes these execution results from static review. The new pattern-run `cmp` compares two automated reconstructions only; it is not presented as a manual or reference comparison. No scientific quality or ARC conclusion is drawn. At the time of this review, automated reconstruction-to-reference comparison was planned under Tasks 7.10–7.12.
  - [x] **7.10 [Copilot] Prepare the automated reconstruction-to-reference comparisons**
    Propose the application of the reviewed reference-comparison method to each automated delivery case: fully sampled Cartesian 2D, fully sampled Cartesian 3D, and Cartesian 3D CS. Include case-specific reporting or limitation notes without imposing a new metric or tolerance.
    **Dependency:** 4.3, 5.8, 6.8, and 7.9
    **Proposal:** Complete. The case-specific inputs, existing visual methods, full-complex relative L2 calculation, separate evaluation outputs, and evidence boundaries are documented in [the Task 7.10 proposal](../docs/python-automation-behavior.md#12-automated-reference-evaluation-method-and-reported-results). It excludes the multichannel `ecalib` result because a compatible scalar reference has not been established.
    **Evidence boundary:** This task completes preparation of the proposal only. The subsequent automated evaluations and their evidence review are recorded under Tasks 7.11 and 7.12; they remain distinct from the existing manual-to-automated byte comparisons and manual-to-reference results.
  - [x] **7.11 [Ricardo] Review and execute the automated reconstruction-to-reference comparisons**
    Review the proposed application, decide required adjustments, and execute the approved visual and quantitative comparisons between each automated delivery-case reconstruction and its corresponding synthetic reference.
    **Dependency:** 7.10
    **Execution evidence:** Ricardo reported applying the existing tutorial blocks (Sections 7–8 for Cartesian 2D and 3D; Sections 10–11 for Cartesian 3D CS) to the preserved automatic reconstructions and references. The evaluations are outside the repository under `$HOME/bart-learning/bart-workflow-reconstructions/automated-reference-evaluations`; each case directory contains `quantitative-comparison.txt`, `visual-comparison.log`, and one figure under `figures-visual/`. Records report Python `3.13.17`, NumPy `2.5.4`, and Matplotlib `3.11.2`.

    | Case and inputs | Evaluation directory and figure | Complex relative L2 error; calculation / figure codes | Human observation and display limits |
    |---|---|---|---|
    | Cartesian 2D: `generation-01/reference` and `automated-2d-01/reconstruction` | `cartesian-2d-TAT46E`; `figures-visual/reference-reconstruction.png` | `1.442448308e-07`; `0` / `0` | Ricardo reported no evident visual differences. The shared display limit was `1`. |
    | Cartesian 3D: `generation-3d-01/reference` and `automated-3d-01/reconstruction` | `cartesian-3d-EqHsLn`; `figures-visual/reference-reconstruction-orthogonal.png` | `1.729089800e-07`; `0` / `0` | Ricardo reported no visual differences in the reviewed figure. The shared display limit was `2`; small magnitude exceedances were recorded in each of the three displayed cuts. |
    | Cartesian 3D CS, original single-channel case: `generation-3d-cs-01/reference` and `automated-3d-cs-01/reconstruction` | `cartesian-3d-cs-hBicqH`; `figures-visual/reference-reconstruction-orthogonal.png` | `2.473308708e-01`; `0` / `0` | Ricardo reported a noisier appearance than the reference and an appearance similar to the manual result. The shared display limit was `2`; the reconstruction's global maximum magnitude was `2.851191679`, above that limit. |

    The quantitative blocks used the complete complex data and `relative_error`, without magnitude conversion, alignment, additional normalization, phase correction, cropping, or region selection. No new metric, tolerance, or acceptance criterion was introduced. The display-limit warnings did not change the figure-generation exit codes. These quantitative values match the previously reported manual-to-reference values at the displayed precision; that agreement does not merge the evaluations or replace the earlier manual-to-automated binary comparisons. This evidence is for the original single-channel CS case, not the multichannel `ecalib` run. Ricardo inspected the reported figures; the observations do not claim inspection of every slice or general scientific acceptance.
  - [x] **7.12 [Copilot] Review the automated reference-comparison evidence**
    Confirm that automated reference comparisons are recorded separately from manual–automated comparisons and identify missing evidence, failures, or unresolved interpretation limits.
    **Dependency:** 7.11
    **Review:** Complete. The reported input pairs, case-specific evaluation directories, quantitative and visual records, figures, results, and exit codes cover the three proposed automatic-reference comparisons. They are recorded separately from the prior manual-to-automated `.cfl` comparisons and the manual-to-reference results. No calculation or figure-generation failure was reported (each code was `0`), and no further evidence required by this task's criterion is identified as missing. Remaining interpretation limits are explicit: figures and human observations cover only the reviewed views, no tolerance or quality acceptance was applied, the CS result is the original single-channel case, and the multichannel `ecalib` case was not compared to a reference. This review does not claim general scientific validation or ARC execution.

- [x] **8.0 Compare Manual and Automated Reconstruction Routes**
  **Completion:** Complete. Tasks 8.1–8.7 define and approve the conditions and binary method, transparently reuse the three preserved manual–automated executions, record the historical binary results and Ricardo's direct visual observations, and complete the evidence review. No new reconstruction is claimed. The operator guide remains a later documentation deliverable.
  - [x] **8.1 [Copilot] Define the comparison conditions for each reconstruction case**
    Identify the prepared inputs, effective configurations, requested outputs, commands or invocations, and records required to compare the three delivery cases without selecting new scientific values implicitly.
    **Dependency:** 7.12
    **Proposal:** Complete. The comparison matrix, effective settings, output and provenance conditions, and evidence limits are documented in [the proposed manual–automated comparison conditions](../docs/python-automation-behavior.md#13-proposed-manualautomated-comparison-conditions). The historical `cmp` results are identified as pre-Block 8 evidence, not as results from a prospectively approved Block 8 protocol.
  - [x] **8.2 [Ricardo] Review and approve the equivalence conditions for manual and automated runs**
    Review Copilot’s proposed equivalence conditions and decide what constitutes equivalent effective configuration and equivalent requested output for fully sampled Cartesian 2D, fully sampled Cartesian 3D, and Cartesian 3D CS.
    **Dependency:** 8.1
    **Decision:** Complete. Ricardo explicitly approved the reuse of the three preserved pairs (Cartesian 2D, Cartesian 3D, and original single-channel Cartesian 3D CS), correspondence of prepared inputs and dimensional interpretation, effective reconstruction settings, and for CS its mask and sensitivities. He approved the BART reconstruction pair as the comparable output, retaining and explaining justified provenance differences, and transparent reuse of the historical evidence without representing it as produced under prospective Block 8 approval. This approves the comparison conditions only; it does not approve the method in Task 8.3 or 8.4.
  - [x] **8.3 [Copilot] Propose and explain the numerical method for manual–automated comparison**
    Prepare a method for comparing matched manual and automated reconstructions. The method may reuse an earlier reference-comparison method, but its application to route comparison must be reviewed separately; no new metric, tolerance, or pass/fail criterion is imposed here.
    **Dependency:** 8.2
    **Proposal:** Complete. [The binary comparison method](../docs/python-automation-behavior.md#14-approved-manualautomated-comparison-method-and-reviewed-results) defines the `.cfl` `cmp` procedure and outcome interpretation, prerequisites, per-case structural evidence, semantic header review, and separation of historical results from later evaluation. Task 8.4 records Ricardo's approval below.
  - [x] **8.4 [Ricardo] Review and approve the numerical route-comparison method**
    Review the proposed method, decide whether an earlier method can be reused or adjusted, and approve the calculation and reporting procedure before matched comparison runs are evaluated.
    **Dependency:** 8.3
    **Approval:** Complete. Ricardo explicitly approved binary `cmp` of each matched `reconstruction.cfl` pair, its exit-code interpretation, the structural and configuration prerequisites, and semantic review of headers without requiring full text identity. This approves the method; the historical `cmp` executions remain identified as predating Block 8 and are not represented as new or prospectively controlled runs.
  - [x] **8.5 [Ricardo] Execute matched manual–automated comparison runs**
    Use the same prepared synthetic inputs for each pair and preserve the conditions needed to distinguish route differences from synthetic-case preparation differences.
    **Dependency:** 8.4, 7.8, and the corresponding manual evidence from Tasks 3.0, 5.0, and 6.0
    **Execution evidence:** Complete through Ricardo's approved reuse of the preserved paired runs under `/Users/ricardoaguilar/bart-learning/bart-workflow-reconstructions/`. The cases use their shared prepared inputs and corresponding effective settings, with the original single-channel CS case using the same supplied `mask3d` and `sensitivities`. These are historical executions; no new reconstruction was requested or performed for Block 8.
  - [x] **8.6 [Ricardo] Compare the manual and automated outputs**
    Record visual and approved numerical differences between each matched pair using the reviewed route-comparison method, without conflating route equivalence with similarity to the synthetic reference.
    **Dependency:** 8.5
    **Comparison evidence:** The historical `cmp` results for `reconstruction.cfl` were code `0` for Cartesian 2D, Cartesian 3D, and original single-channel Cartesian 3D CS. Ricardo also directly compared the existing manual and automated reconstruction panels and reported that he identified no visible differences in the views shown for all three cases. For 3D and CS, the visual observation covers the displayed central planes, not every slice. No manual–automated L2 error or scientific acceptance result is claimed.
  - [x] **8.7 [Copilot] Review the route-comparison records**
    Verify that each record identifies the case, shared prepared inputs, effective settings, requested outputs, produced outputs, comparison method, observed differences, and limitations, and that these records remain separate from reference comparisons and operator-intervention measurements.
    **Dependency:** 8.6
    **Review:** Complete. The behavior record identifies, for each case, the shared inputs, effective operation/settings, requested manual and automated reconstruction pairs, existing structural checks, historical `.cfl` comparison and reported code, header findings, and direct visual result. It distinguishes prior binary comparisons from the current visual inspection, both from Task 7.11 reference evaluations and its observations, and both from future operator-intervention measurement. Header review confirms compatible dimensions, effective commands/settings, declared BART creator version, and expected output-path provenance. Limits remain explicit: the visual review covers only the displayed views; no L2 error, tolerance, scientific pass/fail, or complete retrospective runtime-environment record is claimed. The separate multichannel `ecalib` and automated-to-automated sampling-variant results are not substituted for these pairs.

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

- [`tasks/prd-bart-reconstruction-workflow.md`](./prd-bart-reconstruction-workflow.md) — Reviewed software requirements, approved FR-32 behavior, FR-22 sequencing constraint, comparison requirements, and staged open questions.
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
