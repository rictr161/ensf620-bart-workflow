# Product Requirements Document: BART Reconstruction Workflow

**Status:** Reviewed draft for task planning  
**Project:** ENSF 620 BART Workflow  
**Reference checkpoint:** `ad532fc`, the latest publication checkpoint supplied for this requirements process  
**Working branch:** `planning/ai-dev-tasks`, as reported by Ricardo  
**Primary audience:** Developers and reviewers who need to understand what will be built, why it is needed, and how it will be evaluated

## 1. Introduction and Overview

This project will make BART-based image reconstruction easier to understand, reproduce, execute, and compare.

The initial development will organize existing BART procedures for:

1. Cartesian 2D reconstruction.
2. Cartesian 3D reconstruction.
3. Cartesian 3D reconstruction with compressed sensing.

The development sequence is intentional:

1. Establish and review human-readable manual tutorials.
2. Execute the procedures manually using reproducible synthetic cases.
3. Develop Python automation that performs the same reviewed procedures.
4. Compare the manual and automated routes using the same prepared synthetic inputs, equivalent effective configurations, and equivalent requested outputs.

The first practical deliverable will be a manual tutorial for Cartesian 2D reconstruction. It will cover the complete synthetic workflow, from creation of a known phantom through k-space generation, BART reconstruction, visual comparison, and preliminary quantitative comparison against the original reference.

The future Python workflow will receive compatible BART `.cfl/.hdr` inputs. Phantom generation belongs to preparation of development and evaluation examples; it is not part of the reconstruction function's required input workflow.

The software will be usable from a terminal through a command-line entry point backed by reusable Python functions. It will not provide a graphical user interface. A complete run must be executable without windows, dialogs, or interactive questions. All required configuration must be supplied before execution begins.

Access and authority for AI-assisted operations are governed by the accepted [Data Contract v0.3.0](../docs/DATA_CONTRACT.md). This PRD references that contract as an authority boundary and does not redefine or extend it.

## 2. Goals

### 2.1 Initial development goals

- Document reviewed BART procedures in a form that a developer or operator can follow step by step.
- Provide a reproducible synthetic 2D example before developing reconstruction automation.
- Preserve a known reference image or volume for each synthetic reconstruction case.
- Generate corresponding k-space from the known synthetic reference.
- Explain the purpose, parameters, inputs, outputs, and checks for each manual step.
- Record the commands, configurations, outputs, and observed results of manual execution.
- Develop Python automation that performs the reviewed manual procedures under equivalent conditions.
- Support automation for all three agreed reconstruction cases:
  - Cartesian 2D.
  - Cartesian 3D.
  - Cartesian 3D with compressed sensing.
- Keep reconstruction inputs unchanged and organize outputs in separate run directories.
- Associate each result with the settings used to produce it.
- Compare manual and automated reconstruction results using the same prepared synthetic inputs, equivalent effective configurations, and equivalent requested outputs.
- Keep reconstruction quality, route equivalence, and operator intervention as separate evaluation questions.

### 2.2 Broader workflow goals

- Extend the documented workflow from Cartesian 2D to Cartesian 3D.
- Document a Cartesian 3D compressed-sensing procedure that includes controlled undersampling.
- Reduce repetitive manual parameter entry only where information can genuinely be read or checked from supported inputs.
- Keep decisions that require domain knowledge or explicit configuration distinct from information available in input files.
- Support optional non-interactive figure generation that saves files for later inspection.
- Establish evidence that allows later review of what was executed and under which settings.
- Organize the implementation within the repository's general areas:
  - `src/` for Python source code.
  - `configs/` for configuration-related material.
  - `tests/` for tests.
  - `scripts/` for supporting scripts.
  - `environment/` for environment and dependency documentation.

## 3. User Stories

### 3.1 Manual procedure user

- As a developer, I want to follow a complete 2D tutorial from phantom creation to reconstruction so that I can understand every stage of the BART workflow.
- As an operator, I want each command and parameter explained so that I can execute the procedure without relying on undocumented assumptions.
- As a reviewer, I want input and output files identified at every stage so that I can inspect the generated evidence.
- As a developer, I want to regenerate the same synthetic case so that its preparation is reproducible, while using the same prepared inputs for each manual–automated comparison.

### 3.2 Reconstruction workflow user

- As a user, I want the reconstruction workflow to accept compatible BART `.cfl/.hdr` inputs so that reconstruction can be separated from scanner-specific extraction.
- As a user, I want the workflow to support Cartesian 2D, Cartesian 3D, and Cartesian 3D compressed-sensing procedures.
- As a user, I want to run the workflow from a terminal without a graphical interface.
- As a user, I want to provide all required configuration before execution so that the run does not require interactive questions.
- As a user, I want source inputs preserved so that a reconstruction run does not alter the original case.
- As a user, I want outputs separated by run so that results from different settings can be compared without ambiguity.
- As a user, I want each result linked to the settings used for its run so that I can understand and reproduce the output.
- As a user, I want optional figures saved as files so that they can be inspected later without interactive visualization.

### 3.3 Evaluation user

- As a reviewer, I want to compare a reconstruction with its known synthetic reference so that the observed reconstruction difference can be documented.
- As a reviewer, I want to compare manual and automated results produced from equivalent conditions so that automation can be assessed independently of reference-image accuracy.
- As a reviewer, I want operator intervention recorded for both routes so that operational effort can be compared separately from image quality.
- As a reviewer, I want the initial evidence clearly identified as exploratory or case-specific so that it is not presented as general validation.

## 4. Functional Requirements

### 4.1 Manual tutorials

**FR-1.** The project must provide a human-readable manual tutorial for Cartesian 2D reconstruction as the first practical deliverable.

**FR-2.** The 2D tutorial must distinguish synthetic-case preparation from reconstruction.

**FR-3.** The synthetic-case preparation section must include reproducible creation of a known phantom.

**FR-4.** The tutorial must preserve the original reference image used for the synthetic case.

**FR-5.** The synthetic-case preparation section must generate k-space corresponding to the reference image.

**FR-6.** The reconstruction section must reconstruct the synthetic case using BART.

**FR-7.** The tutorial must identify the input and output files for each stage.

**FR-8.** The tutorial must explain the purpose of each command and the relevant parameters used by that command.

**FR-9.** The tutorial must include checks that allow the operator to determine whether each stage produced the expected files and data needed by the next stage.

**FR-10.** The tutorial must include a visual comparison between the reconstructed result and the original reference.

**FR-11.** The tutorial must include a preliminary quantitative comparison between the reconstructed result and the original reference.

**FR-12.** The tutorial must provide a way to record commands, configuration values, observed outputs, checks, figures, and comparison results.

**FR-13.** The metric and its calculation procedure must be selected and reviewed before the quantitative comparison is performed. The preliminary comparison may record observed differences without an acceptance tolerance or pass/fail classification. If a formal acceptance test is defined later, its metric, calculation procedure, tolerances, and decision criteria must be agreed before that test is executed.

**FR-14.** The project must later provide corresponding tutorials for Cartesian 3D and Cartesian 3D with compressed sensing.

**FR-15.** The compressed-sensing tutorial must include controlled undersampling and must not assume that reconstruction error is negligible.

### 4.2 Synthetic development and evaluation cases

**FR-16.** Development and evaluation cases must retain a known reference image or volume.

**FR-17.** Each case must document how its corresponding k-space was generated.

**FR-18.** Each case must document the dimensions, sampling configuration, and other characteristics needed to reproduce the example once those characteristics have been agreed.

**FR-19.** Each manual–automated comparison must use the same prepared synthetic inputs, equivalent effective configurations, and equivalent requested outputs. This comparison requirement is distinct from checking whether the synthetic case can be regenerated from its documented preparation procedure.

**FR-20.** The project must distinguish facts available from supported input files from reconstruction decisions that require explicit configuration.

**FR-21.** Array dimensions alone must not be treated as proof of acquisition semantics, sampling history, or suitable reconstruction parameters.

### 4.3 Python automation

**FR-22.** After the manual procedures for the agreed reconstruction cases are established, reviewed, and executed, the project must provide Python automation for those same procedures.

**FR-23.** The automation must provide a terminal-based entry point for running a reconstruction procedure.

**FR-24.** The automation must provide configurable reconstruction settings without assuming that optimal settings can be inferred automatically.

**FR-25.** The automation must accept compatible BART `.cfl/.hdr` reconstruction inputs.

**FR-26.** Phantom generation may be used to prepare synthetic development and evaluation cases, but the reconstruction operation must be able to operate on compatible prepared BART inputs.

**FR-27.** The automation must use readable internal Python functions and clearly distinguish input inspection, configuration, reconstruction, output handling, and optional figure generation.

**FR-28.** The automation must preserve source inputs.

**FR-29.** The automation must organize outputs in separate run directories.

**FR-30.** The automation must retain or generate sufficient run information to associate each output with the settings used for that run.

**FR-31.** The automation must support optional non-interactive figure generation that saves files for later inspection and does not require a display window.

**FR-32.** **Proposed behavior pending review:** The automation should surface invalid inputs, unsupported conditions, and execution failures explicitly rather than silently selecting fallback behavior.

**FR-38.** The automation must support the three agreed reconstruction cases in the planned scope:

- Cartesian 2D.
- Cartesian 3D.
- Cartesian 3D with compressed sensing.

**FR-39.** The automation must execute without windows, dialogs, or interactive questions. All required configuration must be available before execution begins.

**FR-40.** The terminal-facing interface must communicate through command-line arguments, configuration options, produced results, and error reporting. The concrete function names, argument names, and configuration format remain open.

### 4.4 Manual and automated comparison

**FR-33.** Each manual–automated comparison must use the same prepared synthetic inputs. This requirement concerns comparison of the two execution routes and does not replace separate reproducibility checks for regenerating the synthetic case.

**FR-34.** Each manual–automated comparison must use equivalent effective reconstruction configurations and equivalent requested outputs.

**FR-35.** The project must separately document:

- Difference between each reconstruction and its known synthetic reference.
- Difference between the manual and automated results.
- Operator intervention required by each route.
- Whether the synthetic preparation procedure regenerated the intended reference and corresponding input data.

**FR-36.** The comparison record must identify the prepared inputs, effective settings, commands or entry-point invocation, requested outputs, produced outputs, figures, metrics, and observed differences.

**FR-37.** The project must not present a single exploratory 64 × 64 exercise as general validation or as proof of reproduction from a clean checkout.

## 5. Non-Goals and Scope Boundaries

### 5.1 Software scope

The initial software scope includes:

- Manual procedures for Cartesian 2D, Cartesian 3D, and Cartesian 3D compressed-sensing reconstruction.
- Python automation equivalent to those reviewed manual procedures.
- Terminal execution through a non-graphical command-line entry point.
- Reusable Python functions supporting the terminal workflow.
- Configurable reconstruction settings.
- Optional non-interactive figure generation saved as files.
- Preservation of source inputs.
- Separate run directories and association of outputs with their effective settings.
- Comparison of manual and automated routes using the same prepared synthetic inputs, equivalent effective configurations, and equivalent requested outputs.
- Synthetic phantom generation for preparation of development and evaluation examples.

The initial software scope does not include:

- Scanner extraction.
- Conversion from `.h5`.
- Automatic selection of optimal reconstruction parameters.
- Automatic parameter search or optimization.
- Batch reconstruction implementation for ARC.
- ARC deployment or a commitment to implement ARC reuse at this stage.
- HPC deployment.
- A complete implementation architecture before the reviewed manual procedures are established.
- A graphical user interface.

Batch reconstruction and reuse in ARC remain possible future directions. Their scope, interface, deployment details, and implementation are not committed by this PRD.

### 5.2 AI access and authority boundary

AI-assisted access and actions are governed by the accepted [Data Contract v0.3.0](../docs/DATA_CONTRACT.md). The Data Contract remains the authority for those boundaries.

This PRD does not reproduce the Data Contract, redefine its permissions, or convert the interaction rules of the requirements process into software capabilities or software exclusions.

### 5.3 Evidence and scientific-interpretation boundaries

The following limits apply to evaluation conclusions:

- Experimental DICOM images are not an approved ground-truth reference for this project.
- Private metadata, extractor code, private storage, and HPC access are not required inputs to this development.
- The existing 64 × 64 BART/NumPy exercise is exploratory evidence only.
- A preliminary quantitative difference must not be presented as general validation.
- No conclusion may assume that compressed-sensing reconstruction error is negligible.
- No numerical acceptance threshold is established until the metric, calculation procedure, and criteria are explicitly reviewed.

## 6. Design Considerations

The following behaviors are requirements of the planned workflow. The mechanisms for implementing them remain open:

- Source inputs must be preserved.
- Outputs must be organized in separate run directories.
- Each result must remain associated with the effective settings used to produce it.
- Figure generation must be optional.
- Optional figures must be saved as files without requiring interactive visualization.
- The workflow must run without windows, dialogs, or interactive questions.
- All required configuration must be supplied before execution begins.
- The terminal-facing interface must expose arguments, configuration options, results, and error communication.
- The implementation should align with the repository's general organization in `src/`, `configs/`, `tests/`, `scripts/`, and `environment/`.

The following implementation details are intentionally not decided:

- Internal Python module and function organization.
- Concrete function names.
- Concrete command-line argument names.
- Configuration file format and schema.
- Run-directory naming convention.
- Exact mechanism for storing effective settings with outputs.
- Exact error-reporting format.
- Exact mechanism for generating and saving figures.
- Whether the terminal entry point will be implemented as a script, Python module invocation, or another command-line arrangement.

The manual tutorial should serve as the behavioral reference for the first automation implementation. The interface should remain simple for the initial workflow while leaving room for later reuse of internal functions.

## 7. Technical Considerations and Constraints

- BART is the reconstruction tool whose reviewed procedures will be organized.
- The reconstruction workflow must work with compatible BART `.cfl/.hdr` inputs.
- Synthetic phantom generation is part of preparing reproducible examples, not a substitute for validating arbitrary input semantics.
- Input dimensions and file availability must not be overinterpreted as evidence of acquisition meaning or sampling history.
- The manual and automated paths must be compared using the same prepared synthetic inputs, equivalent effective configurations, and equivalent requested outputs.
- Existing source inputs and previously generated runs must remain distinguishable.
- The terminal workflow must not depend on a graphical display or interactive prompts.
- Figure generation must be possible in a non-interactive mode.
- The repository is generally organized around:
  - `src/`
  - `configs/`
  - `tests/`
  - `scripts/`
  - `environment/`
- The internal organization of those areas remains open.
- Documentation, source comments, and commit messages must be written in English.
- Access and authority boundaries are defined by the accepted [Data Contract v0.3.0](../docs/DATA_CONTRACT.md).

## 8. Success Metrics and Evaluation

Success will be evaluated using evidence from the reviewed synthetic workflows, not by assuming a result in advance.

### 8.1 First tutorial completion

The following criteria apply specifically to the first practical deliverable: the manual Cartesian 2D tutorial.

The first tutorial is successful when an operator can:

- Recreate the agreed 2D phantom.
- Preserve and identify the reference image.
- Generate the corresponding k-space.
- Run the documented BART reconstruction.
- Identify the inputs and outputs of each stage.
- Inspect the reconstruction visually.
- Perform and record the approved preliminary quantitative comparison.
- Record the commands, parameters, checks, and observed results.
- Complete the procedure without undocumented interactive steps.

These criteria do not establish numerical acceptance thresholds for the reconstruction.

### 8.2 Reconstruction-to-reference comparison

The project will measure the observed difference between the reconstruction and the known synthetic reference.

The metric and its calculation procedure must be selected and reviewed before this comparison is carried out. The preliminary comparison may document an observed difference without applying a tolerance or pass/fail classification.

If a formal acceptance test is defined later, its metric, calculation procedure, tolerances, preprocessing rules, and decision criteria must be agreed before that test is executed.

The result must be reported as observed evidence for the agreed case and configuration. It must not automatically be interpreted as general validation.

### 8.3 Manual-to-automated comparison

The project will compare the manual and automated results using:

- The same prepared synthetic inputs.
- Equivalent effective reconstruction configurations.
- Equivalent requested outputs.

This comparison is separate from checking whether the synthetic preparation procedure can regenerate the intended case.

The comparison must document the observed difference and the conditions under which it was obtained. It must not be conflated with similarity to the synthetic reference.

No tolerance or pass/fail classification is established by this draft.

### 8.4 Operator intervention

The project will document the intervention required by each route, such as:

- Commands entered.
- Parameters supplied.
- Configuration decisions made.
- Checks performed.
- Manual decisions or corrections required.

Operational measurement rules remain to be defined. This draft does not assume that one route will require less intervention.

### 8.5 Scope and reproducibility evidence

The project will retain enough information to determine:

- Which synthetic case was used.
- How the case was generated.
- Whether the preparation procedure regenerated the intended reference and corresponding input data.
- Which effective settings were used.
- Which manual commands or automated invocation were executed.
- Which outputs and figures were produced.
- Which metric and calculation procedure were used for a quantitative comparison.
- What differences were observed.
- Whether the evidence concerns reference similarity, route equivalence, or operator intervention.

## 9. Open Questions

The questions are grouped by the point in the development sequence when they must be resolved. Decisions concerning later 3D, compressed-sensing, or future ARC use must not block work on the first 2D case unless they directly affect that case.

### 9.1 Questions required for the first tutorial 2D

1. Which phantom definition or phantom-generation procedure will be used?
2. What image dimensions will be used?
3. What k-space sampling configuration will be used?
4. Will the first case use fully sampled Cartesian data?
5. How many channels will be used?
6. If multiple channels are used, how will channel data and combination be defined?
7. Which BART commands and reconstruction parameters constitute the reviewed baseline procedure?
8. Which files will be treated as the authoritative reference, k-space input, and reconstruction output?
9. Which checks are mandatory for the first tutorial beyond file existence and visual inspection?
10. What format should record commands, parameters, checks, outputs, figures, and observed results?

### 9.2 Questions required for the quantitative comparison

11. Which metric or set of metrics will be selected for the preliminary reconstruction-to-reference comparison?
12. What calculation procedure will be used for that metric?
13. What preprocessing, normalization, cropping, masking, or alignment rules are required before computing the metric?
14. Should the same metric later be used for manual-to-automated comparison, or should that comparison use a separate measure?
15. Will formal tolerances or pass/fail criteria be defined later? If so, for which comparison questions and under what review process?
16. What operational rules will be used to record operator intervention?

Questions 11–13 must be resolved before performing the first preliminary comparison against the reference. Question 14 concerns the later manual–automated comparison, question 15 concerns a possible formal acceptance test, and question 16 concerns measurement of operator intervention. These questions must be resolved before carrying out their respective evaluations, but they must not automatically become prerequisites for the first preliminary comparison against the reference.

### 9.3 Questions required for automation

17. What command-line arguments and configuration options are required for the first automated 2D procedure?
18. Which input information should the automation read or check, and which reconstruction decisions must remain explicit configuration?
19. How should repeated runs with different settings be named and associated with their effective configurations?
20. What information must be stored in each run directory?
21. What error conditions and reporting behavior should be specified for invalid inputs, unsupported conditions, and failed BART commands? FR-32 is a proposed behavior pending review.
22. What file formats and command-line conventions should be used for non-interactive figure generation?
23. Which Python functions should be reusable independently of the terminal entry point?
24. Which automated comparison outputs should be generated or recorded?
25. What must count as equivalent effective configuration and equivalent requested output when comparing manual and automated routes?

These questions may be resolved incrementally after the manual 2D procedure has been reviewed. They must not be answered by prematurely fixing a complete architecture.

### 9.4 Questions for later cases and future directions

26. Which Cartesian 3D procedure should be documented after the 2D tutorial?
27. Which controlled undersampling method and reconstruction procedure should be used for the Cartesian 3D compressed-sensing tutorial?
28. What additional input characteristics, checks, or output representations are required for the 3D cases?
29. What future requirements, if any, would be needed before considering reuse for ARC?
30. What future requirements, if any, would be needed before implementing batch reconstruction?
31. How should future parameter-exploration workflows reuse the reviewed reconstruction functions without becoming part of the current implementation?

These later questions must not block the first 2D tutorial unless a direct dependency is identified and reviewed.

## 10. Review Boundary

This document is a reviewed draft for task planning. It describes the agreed intent and separates requirements, proposed behavior, and unresolved decisions.

It does not:

- Authorize implementation before review.
- Define a complete Python architecture.
- Select the first phantom, sampling scheme, channel count, BART parameters, metric, tolerance, or acceptance criteria.
- Establish numerical acceptance thresholds.
- Commit batch reconstruction or ARC implementation.
- Redefine the accepted Data Contract v0.3.0.
- Treat future capabilities as already implemented.

The next step is task planning based on this draft, subject to resolution of the questions required for the first 2D tutorial and its quantitative comparison.
