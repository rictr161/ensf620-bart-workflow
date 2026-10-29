# Open Questions and Evidence Status

This record tracks unresolved project questions and the evidence available to
answer them. A status of "not established" refers to the shared documentation;
it does not establish whether Ricardo holds additional information privately.

The technical scope is Cartesian 2D/3D reconstruction, including CS. Ricardo's
current experimental input report concerns brain MRI 3D BART `.cfl`/`.hdr` files;
the [input inventory](input-inventory.md) records that report and its historical
context. BART-generated synthetic phantoms remain the development and testing
route described in the [project context](project-context.md).

The accepted [AI access/action contract](DATA_CONTRACT.md),
**ENSF620-BART-DC v0.3.0**, governs assistant access and authority. The software
input conventions and evaluation questions below are separate from that policy.

## Input conventions and metadata

| ID | Question | Recorded status |
| --- | --- | --- |
| DATA-01 | How many files, acquisitions and datasets belong to each reported configuration? | Detailed counts are not established in the shared record |
| DATA-02 | What complex representation and axis meanings apply to the current experimental inputs? | Input-specific metadata and dimension meanings remain unverified in the shared record |
| DATA-03 | What scaling, centering and channel conventions apply to the current experimental `.cfl`/`.hdr` inputs? | Input-specific conventions remain unverified in the shared record; software support remains to be specified and reviewed. The synthetic example documents only its own conventions |
| DATA-04 | What sampling geometry, mask and reconstruction settings apply to the current 3D CS inputs? | Not established in the shared record |
| DATA-05 | Do the earlier acceleration and volume details describe the current inputs? | Correspondence remains unknown |
| DATA-06 | What does the earlier "200" value mean, and does it describe the current inputs? | Meaning, units and correspondence remain unresolved |

## Historical extraction context

These questions concern upstream provenance. Extraction and `.h5` conversion are
outside the current implementation scope; these questions are not current
workflow implementation blockers.

| ID | Question | Recorded status |
| --- | --- | --- |
| EXTRACT-01 | What are the historical extractor's identity, version and invocation? | Not established by the historical description |
| EXTRACT-02 | What are the historical extractor's dependencies and platform requirements? | Not established; compatibility with the recorded synthetic environment is also unverified |
| EXTRACT-03 | What outputs and configurations does the historical extractor support? | Not established by the historical description |

## Permissions and data handling

These operation-specific questions correspond to Q02, Q08 and Q09 in the
[contract decision register](DATA_CONTRACT_DECISIONS.md#open-decisions-and-evidence).
They do not change the contract's accepted status.

| ID | Question | Recorded status |
| --- | --- | --- |
| AUTH-01 | Which uses and processing/storage destinations are permitted for a specific laboratory source? | Source-specific confirmation is not recorded here; tracked under Q02 |
| AUTH-02 | What are the TrueNAS retention and student-copy deletion terms? | Confirmation by the laboratory supervisor/steward is not recorded here; tracked under Q09 |
| AUTH-03 | Which summaries or outputs may be shared, and with which audience? | Approved fields/results and intended audiences are not established here; tracked under Q08 |

## Environment and verification

The [local environment record](../environment/local-macos.md) describes the
observed Mac setup. The [project context](project-context.md#evaluation-planning-and-comparison-principles)
describes the evaluation planning behind the verification questions.

| ID | Question | Recorded status |
| --- | --- | --- |
| ENV-01 | What are the full BART commit and actual `Makefile.local` contents? | Only v1.0.00, short commit `37f3c5f` and selected flags are recorded; the full commit and configuration remain unrecorded |
| ENV-02 | What environment and resource configuration will TALC use, with ARC as a possible alternative? | A separate deployment record remains pending |
| VERIFY-01 | What pilot-justified numerical tolerances and operator-action counting rule will be used? | Definition and human approval remain pending before the main evaluation |
| VERIFY-02 | Have negative tests and reproduction from a clean checkout been completed? | Both remain pending in the shared record |

## Repository publication and review

| ID | Question | Recorded status |
| --- | --- | --- |
| GIT-01 | Has the working branch been published? | Publication of `planning/ai-dev-tasks` at `d59ff7d` is supported by Ricardo's supplied push output |
| GIT-02 | Which published commit is recorded, and can intended reviewers access it? | The supplied checkpoint identifies `d59ff7d`; intended reviewer access remains unverified |

### Supplied publication checkpoint

The earlier [repository checkpoint](copilot-handoff.md#repository-checkpoint-supplied-by-ricardo)
identifies policy acceptance commit `5bcf772` and the working branch's creation
from `main`. Subsequent terminal output supplied by Ricardo records:

- A successful `git push -u origin planning/ai-dev-tasks`, advancing the remote
  branch from `5bcf772` to `d59ff7d` and configuring upstream tracking.
- `git status --short --branch` showing the local branch and its upstream without
  file-change entries or an ahead/behind indication at that checkpoint.
- `git --no-pager log -1 --oneline` placing `HEAD`, `planning/ai-dev-tasks` and
  `origin/planning/ai-dev-tasks` at `d59ff7d`, with the commit message
  `docs: align documentation and standardize AI use records`.

This evidence applies to the supplied checkpoint; it is not an independent check
of current GitHub content. Publication of later documentation edits and a merge
of this working branch into `main` are not established by that output.
Clean-checkout reproduction remains tracked under VERIFY-02.

## Work affected by unresolved questions

The unresolved questions affect different parts of the project:

- Unclear authority blocks the affected experimental operation. Reviewed
  synthetic work may continue within the accepted access/action boundaries.
- Missing acquisition information blocks reconstruction procedures that depend
  on it, rather than all learning or synthetic development.
- Unresolved numerical discrepancies block promotion of the affected procedure
  to the main evaluation.

The existing planning note associates exclusions and their reasons with the
November 6, 2026 gate. No outcome from that gate is recorded here.
