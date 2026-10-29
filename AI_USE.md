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
