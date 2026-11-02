# Copilot Handoff

Use this note to resume supervised AI-assisted work on the ENSF 620 project. The
[project README](../README.md) is the starting point for project scope, current
usage, evidence and documentation. This handoff provides session context and a
suggested request for supervised task planning.

## Accepted policy and project context

The [AI data-access and action contract](DATA_CONTRACT.md),
**ENSF620-BART-DC v0.3.0**, is `OWNER_ACCEPTED`. The
[decision register](DATA_CONTRACT_DECISIONS.md) records its acceptance on
2026-10-27, boundary decisions and unresolved access/action questions. The contract
takes precedence over this handoff and other supporting guidance for AI access and
actions. It does not define the software specification or evaluation protocol,
and acceptance does not establish technical enforcement.

Python is the chosen primary implementation language for the Cartesian 2D/3D
workflow, including compressed sensing. The existing evidence is Ricardo's
fully sampled, single-channel, 64 × 64 synthetic 2D exercise, with an independent
NumPy inverse of the BART-generated k-space. No numerical acceptance threshold was
applied. The automated workflow, verified experimental 3D baseline, approved
evaluation criteria and clean-checkout reproduction remain pending; see
[Current status](../README.md#current-status). DICOM comparison remains a proposed
complementary reference without an approved protocol.

## Current requirements and planning

The [software PRD](../tasks/prd-bart-reconstruction-workflow.md) has the status
**Reviewed draft for task planning**. It describes the planned software behavior
and retains proposed behavior and unresolved decisions. It does not establish
implemented functionality or completed evaluation.

The [project context](project-context.md) preserves the broader evaluation
planning. HPC deployment is outside the current PRD. The next planning step is a
review of top-level development tasks before expansion into subtasks.

## Recorded Copilot use

[AI_USE.md](../AI_USE.md) records supervised documentation work using
"Copilot SDK in VS Code" on 2026-10-26 and access/action-boundary acceptance on
2026-10-27. These entries document past use; they do not establish the current
editor configuration, enabled tools, permissions or technical isolation.

The earlier entry describing Copilot as planned belongs to the familiarization
checkpoint. Preserve it as a dated record rather than treating it as the current
state of all project assistance.

For the current PRD stage, Ricardo reports using **Copilot Chat in VS Code**.
That identifies the reported interface for this activity; enabled tools,
permissions and technical isolation still depend on the actual client and session.

## Repository checkpoint supplied by Ricardo

The starting repository export corresponds to commit
`5bcf772a09ced4339cc70b87eba85488713c2c41`. Ricardo reported the following Git state
for that checkpoint:

| Item | Reported state |
| --- | --- |
| Repository | `rictr161/ensf620-bart-workflow` |
| Policy acceptance commit | `5bcf772` |
| Integrated branch | `docs/data-contract-workflow` was merged and published on `main` |
| Working branch | `planning/ai-dev-tasks` was created from `main` |

Ricardo subsequently supplied successful push, status and log output for
documentation commit `d59ff7d` on `planning/ai-dev-tasks`. The
later supplied documentation publication checkpoints were `2435329` and
`ad532fc`; `ad532fc` is the latest checkpoint supplied for this requirements
process. The
[publication checkpoint](open-questions.md#supplied-publication-checkpoint)
records the supplied publication evidence and its limits.

These are supplied checkpoints, not independent checks of current local or
remote Git state. Publication at `ad532fc` does not establish publication of the
PRD or this documentation update, or a merge of the working branch into `main`.
Reviewer access and clean-checkout reproduction remain unverified, as recorded
under GIT-02 and VERIFY-02 in the same questions record.

Earlier setup and assistance checkpoints remain in the
[Git workflow](git-workflow.md) and [AI use record](../AI_USE.md). Their dated
statements do not make initial repository setup or the first push a pending task.

## Workspace and review responsibilities

Open only the reviewed project folder, not the home directory, laboratory storage,
upstream BART tree or a multi-root workspace containing restricted material. Give
specific context documents to the assistant. Check whether the chosen client is
using the [repository instructions](../.github/copilot-instructions.md); do not
assume every repository file is automatically read in a particular response.

Available workspaces and tools depend on the client and mode. Do not assume a
hosted session has Ricardo's Mac installation, BART dependencies or local
synthetic files. Instructions and `.gitignore` do not establish isolation. Review
execution approvals and available controls; keep automatic approval off. The
[workspace and data handling notes](data-and-ai-boundaries.md) provide supporting
guidance under the accepted policy.

For each requested block, identify the affected files and prepare a reviewable
diff. Ricardo reviews and applies changes and executes commands. Preserve
historical evidence and record material assistance, corrections and actual checks
in `AI_USE.md`; distinguish proposed checks from completed ones. Ricardo handles
Git operations and approves evaluation criteria and data decisions.

Experimental data, DICOM, extractor code, credentials, private storage and HPC
remain outside AI access. The assistant must not initiate or observe private
execution. Repository visibility does not change these boundaries.

## Suggested task-planning request

```text
Read these reviewed project documents:
- README.md
- docs/DATA_CONTRACT.md and docs/DATA_CONTRACT_DECISIONS.md
- tasks/prd-bart-reconstruction-workflow.md
- .github/copilot-instructions.md
- docs/project-context.md, docs/input-inventory.md and docs/open-questions.md
- docs/data-and-ai-boundaries.md, docs/copilot-handoff.md and AI_USE.md

Consult environment/local-macos.md and tests/synthetic_2d/README.md for the
recorded environment and synthetic exercise. Reading these procedures does
not authorize execution.

Treat ENSF620-BART-DC v0.3.0 as the accepted AI access/action policy. It is
not the software specification or evaluation protocol.

Use the PRD as the reviewed draft for task planning. Preserve its requirement
identifiers, proposed behavior and unresolved choices; do not fill in
undecided reconstruction settings, interfaces or evaluation criteria.

For this initial task-planning response, do not edit files or run commands.
Briefly summarize the requirements and pending decisions, distinguishing
executed evidence from planned work. Then propose only top-level development
tasks grounded in the PRD, preserving its three reconstruction cases and
manual-before-automation sequence. Wait for my review before expanding
them into subtasks. Do not write code or start implementation.

Keep repository content in English and explanations in Spanish. Use only
the reviewed files listed above. Do not access laboratory data, images,
extraction code, credentials, private storage or HPC. Do not initiate or
observe private execution.
```

## Next work

Use the [generate-tasks.md workflow](https://github.com/snarktank/ai-dev-tasks/blob/main/generate-tasks.md)
with Copilot to prepare top-level development tasks from the reviewed PRD.
Ricardo reviews those tasks before expansion into subtasks. Adapt the generic
workflow to this repository's Python scope and existing `planning/ai-dev-tasks`
branch; a new branch is not required for this planning step. Implementation is
not part of the current planning block.

BART-generated synthetic phantoms remain the development and testing route.
The PRD's unresolved reconstruction settings, interface choices and evaluation
decisions still need review; do not infer them from the access contract or guess
experimental metadata.
