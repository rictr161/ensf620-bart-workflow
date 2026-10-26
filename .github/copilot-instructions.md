# Repository instructions

Read `README.md`, `docs/project-context.md`, `docs/input-inventory.md`,
`docs/open-questions.md`,
`docs/data-and-ai-boundaries.md`, and `docs/copilot-handoff.md` before proposing
changes. Consult `environment/local-macos.md` and `tests/synthetic_2d/README.md`
for execution and verification.

## Scope and status

This is Ricardo's individual ENSF 620 BART workflow project. Python is the primary
implementation language for a simpler Cartesian 2D/3D workflow interface, including
compressed sensing. Prioritize one verified 3D Cartesian manual–automated pair. Do
not expand implementation to radial or 4D, or modify BART algorithms. Operator
intervention is primary; runtime/memory are secondary. Extraction and `.h5`
conversion are outside the current workflow implementation boundary.

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
success or adjust tolerances merely to pass. Human-approved tolerances and action
counting rules must be fixed before evaluation.

Keep the NumPy inverse independent of BART execution. The current reader and
centering recipe support only the documented 64 × 64, single-channel fixture;
do not silently generalize them. Match paired inputs, settings and resources.
Keep learning/development outside operational action measurements. Record failures.

## Files and disclosure

Keep both original scripts together in `scripts/`: visualization imports
`read_bart_2d` from `check_fourier_numpy.py`. They use the current working directory
for data. Preserve that behavior until a reviewed refactor.
Identify missing original files before reproduction. Never fabricate replacement
logs. Keep experimental BART files, DICOM images, extractor code, credentials,
private storage and HPC access outside AI context. Record material AI assistance,
corrections and actual checks in `AI_USE.md`.
