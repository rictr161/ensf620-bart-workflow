# Repository instructions

## Reading order and document authority

Read the following documents before proposing changes:

1. [README.md](../README.md) for the project overview, current status and evidence.
2. [docs/DATA_CONTRACT.md](../docs/DATA_CONTRACT.md) and
   [docs/DATA_CONTRACT_DECISIONS.md](../docs/DATA_CONTRACT_DECISIONS.md) for the
   accepted AI access/action policy, acceptance record and boundary decisions.
3. [tasks/prd-bart-reconstruction-workflow.md](../tasks/prd-bart-reconstruction-workflow.md)
   for software requirements, proposed behavior and stage-specific open questions.
   Its status is **Reviewed draft for task planning**.
4. [docs/project-context.md](../docs/project-context.md),
   [docs/input-inventory.md](../docs/input-inventory.md) and
   [docs/open-questions.md](../docs/open-questions.md) for project planning,
   reported input availability and unresolved questions.
5. [docs/data-and-ai-boundaries.md](../docs/data-and-ai-boundaries.md) for
   supporting workspace separation and data handling notes.
6. [docs/copilot-handoff.md](../docs/copilot-handoff.md) for collaboration context.

The accepted **ENSF620-BART-DC v0.3.0** is the primary policy for AI access and
actions and takes precedence over these instructions and supporting guidance on
those subjects. The contract and its decision register do not define the software
specification or evaluation protocol. The PRD records planned software behavior;
its presence does not authorize implementation or resolve its open decisions.

Consult [environment/local-macos.md](../environment/local-macos.md) and
[tests/synthetic_2d/README.md](../tests/synthetic_2d/README.md) for the recorded
environment and existing synthetic procedure. These references do not authorize
command execution.

## Scope and status

This is Ricardo's individual ENSF 620 BART workflow project. Python is the primary
implementation language for Cartesian 2D, Cartesian 3D and Cartesian 3D with
compressed sensing. The first practical deliverable is the manual synthetic 2D
tutorial. Establish, review and execute the manual procedures before developing
their equivalent Python automation, following the PRD's staged questions.

The planned automation uses a terminal entry point and reusable Python functions,
without a GUI, windows, dialogs or interactive questions during execution.
Optional figures are saved for later inspection. Concrete arguments,
configuration formats and internal architecture remain open.

Do not expand implementation to radial or 4D, or modify BART algorithms.
Extraction and `.h5` conversion remain outside the implementation boundary.
The project context preserves the earlier course evaluation planning, including
the priority given to one verified 3D manual–automated pair and operator
intervention as the primary outcome. HPC deployment is outside the initial PRD
scope; broader evaluation planning does not make it a current implementation task.

Only a fully sampled 64 × 64 synthetic Fourier comparison has been observed.
It is exploratory, not the automated workflow, an experimental 3D baseline or a
formal pass under a predefined tolerance. Do not describe planned work as executed.
BART-generated synthetic phantoms are the confirmed development/testing basis for
matched manual and automated procedures; fixtures, settings, tests and acceptance
criteria remain undefined and unverified.

## Language and review

Write committed notes, code comments, test reports and commit messages in English.
Conversational explanations for Ricardo may be in Spanish.

Propose small, explainable changes. State assumptions, affected files and verification
steps. Ricardo reviews code and runs commands. Do not install software, access
networks, submit jobs, commit/push, change history or run destructive commands
without explicit authorization. Do not enable automatic command approval.

## Access and data

Use project-owned code and explicitly authorized synthetic/public examples. Do not
seek access to laboratory measurements, images, extraction code, storage, TALC,
credentials or private links. Do not scan the home folder or adjacent workspaces.
If material is unavailable, record the limitation rather than searching for it.
These instructions and `.gitignore` are not enforced access controls.

## Scientific checks

Never infer missing masks, trajectories, dimension meanings, parameters or permission.
Earlier Poisson/R=8/10-volumes/"200" details are historical and must not be assigned
to current brain datasets without established correspondence. Current experimental
inputs are author-reported `.cfl`/`.hdr` files; availability is not validation.
Preserve historical evidence. Do not fabricate results, treat missing outputs as
success or adjust tolerances merely to pass. Select and review the metric and
calculation procedure before a preliminary quantitative comparison; that
comparison may report observed differences without a tolerance or pass/fail
classification. Agree any formal acceptance criteria before their test and
operator-action counting rules before measuring operator intervention.

Keep the NumPy inverse independent of BART execution. The current reader and
centering recipe support only the documented 64 × 64, single-channel fixture;
do not silently generalize them. Use the same prepared synthetic inputs and
equivalent effective configurations and requested outputs for a manual–automated
comparison. Keep resource conditions comparable when measuring operational effects.
Keep learning/development outside operational action measurements. Record failures.

## Files and disclosure

Keep both original scripts together in `scripts/`: visualization imports
`read_bart_2d` from `check_fourier_numpy.py`. They use the current working directory
for data. Preserve that behavior until a reviewed refactor.
Identify missing original files before reproduction. Never fabricate replacement
logs. Keep experimental BART files, DICOM images, extractor code, credentials,
private storage and HPC access outside AI context. Record material AI assistance,
corrections and actual checks in `AI_USE.md`.
