# Copilot Handoff

Use this note to resume supervised AI-assisted work on the ENSF 620 project. The
[project README](../README.md) is the starting point for project scope, current
usage, evidence and documentation. This handoff provides session context and a
suggested initial review request.

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

## Recorded Copilot use

[AI_USE.md](../AI_USE.md) records supervised documentation work using
"Copilot SDK in VS Code" on 2026-10-26 and access/action-boundary acceptance on
2026-10-27. These entries document past use; they do not establish the current
editor configuration, enabled tools, permissions or technical isolation.

The earlier entry describing Copilot as planned belongs to the familiarization
checkpoint. Preserve it as a dated record rather than treating it as the current
state of all project assistance.

## Repository checkpoint supplied by Ricardo

The starting repository export corresponds to commit
`5bcf772a09ced4339cc70b87eba85488713c2c41`. Ricardo reported the following Git state:

| Item | Reported state |
| --- | --- |
| Repository | `rictr161/ensf620-bart-workflow` |
| Policy acceptance commit | `5bcf772` |
| Integrated branch | `docs/data-contract-workflow` was merged and published on `main` |
| Working branch | `planning/ai-dev-tasks` was created from `main` |

This is a supplied checkpoint, not an independent check of live local or remote
Git state. Publication of the working branch and commits for the documentation
edits prepared after that export have not been verified here.

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

## Suggested initial request

```text
Read these reviewed project documents:
- README.md
- docs/DATA_CONTRACT.md and docs/DATA_CONTRACT_DECISIONS.md
- .github/copilot-instructions.md
- docs/project-context.md, docs/input-inventory.md and docs/open-questions.md
- docs/data-and-ai-boundaries.md, docs/copilot-handoff.md and AI_USE.md

Consult environment/local-macos.md and tests/synthetic_2d/README.md for the
recorded environment and synthetic exercise. Reading these procedures does
not authorize execution.

Treat ENSF620-BART-DC v0.3.0 as the accepted AI access/action policy. It is
not the software specification or evaluation protocol.

During this initial review, do not edit files or run commands. Summarize the
documented state, distinguishing executed evidence, owner-reported context
and pending work. Identify concrete documentation inconsistencies and
propose one small next correction, its affected files and how I should
review it. Wait for my review before preparing changes. Do not draft
software specifications, development task lists or implementation yet.

Keep repository content in English and explanations in Spanish. Use only
the reviewed files listed above. Do not access laboratory data, images,
extraction code, credentials, private storage or HPC. Do not initiate or
observe private execution.
```

## Next work

Continue the documentation alignment in small blocks reviewed by Ricardo. Then
prepare interactive use of [ai-dev-tasks](https://github.com/snarktank/ai-dev-tasks)
with Copilot. That preparation remains pending; this handoff does not establish
that ai-dev-tasks has been installed, configured or used.

BART-generated synthetic phantoms remain the development and testing route.
Future software requirements, reconstruction settings and evaluation decisions
need their own review; do not infer them from the access contract or guess
experimental metadata.
