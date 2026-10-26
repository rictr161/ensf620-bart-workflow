# AI Use Record

## Familiarization, environment and repository preparation

Consolidation date: 2026-10-23. This is not a claim that all work occurred that day
or by the planned October 9 milestone.

Tool: ChatGPT, web interface.  
Model identifier: not independently recorded for the preceding sessions.  
Copilot: planned for subsequent supervised work; no Copilot execution is established
by this entry.

### Inputs and assistance

Ricardo supplied the proposal, instructor feedback, proposal package and final
project guide, selected terminal outputs, five synthetic figures, hardware details
and a non-sensitive dataset summary.

Assistance covered BART/Git concepts, a macOS build recipe, synthetic image and
k-space generation, Python setup, a separate NumPy inverse, visualization,
interpretation, inventory and the English repository notes/Copilot guidance.

### Execution and verification

Ricardo executed commands on his Mac and returned their outputs. The assistant did
not access his Mac, TALC, laboratory storage or GitHub repository. The independent
checker reads the synthetic files, validates dimensions/size/finite values and
computes an inverse Fourier transform with NumPy without invoking BART. No
numerical threshold was applied. The five figures and three reported relative
errors are preserved as supplied evidence, not assistant-run results.

The supplied staged listing now includes the two imported scripts, selected text
reports and dependency snapshots. The script contents and environment snapshots
were also included in the supplied diff. This does not establish a new execution
or byte-for-byte equality against every original file. Clean-checkout reproduction,
formal regression tests and the experimental baseline remain pending.
The documentation was AI-drafted and still requires author review.

### Important corrections and limitations

- Initial Windows/WSL guidance was replaced after Ricardo clarified the macOS platform.
- BART's detached HEAD belongs to its separate upstream release checkout, not the
  ENSF 620 repository.
- A BART-only round trip was not treated as an independent correctness check;
  a separate NumPy inverse was subsequently executed.
- No numerical threshold or formal pass status was invented after seeing residuals.
- An accidental `view` invocation opened Vim; exit guidance restored the terminal.
  This learning interruption was not an evaluated experimental failure.
- Ricardo corrected a temporary "No" for 3D CS to "Yes". This was a reporting error,
  not a new receipt. Format, actual volume count and "200" remain unresolved.
- The instruction file and `.gitignore` are guidance/version-control mechanisms,
  not guarantees of restricted-data isolation.

### Boundaries and responsibility

No laboratory measurements, derived laboratory images, extraction code, credentials
or private sharing links were provided. Ricardo retains responsibility for scope,
criteria, code review, local execution, data handling and TALC submission. Learning
and one-time development are separate from later operational comparisons.

Earlier AI help with proposal scoping, drafting and LaTeX, acknowledged in the
proposal, requires its own concise entry; do not invent dates/model identifiers.
Raw private transcripts are not necessary for this disclosure.

Human review of this initial documentation: pending at the pre-publication checkpoint.
Actual commit identity and date must come from Git history, not retrospective claims.

## Contextual documentation revision — 2026-10-26

Tool/access: Copilot SDK in VS Code, using only reviewed workspace documents and
the authorized file list. No terminal, network, browser, MCP, subagent, private
data, or remote system was used.

The documentation was updated to reflect Ricardo's current author-confirmed
context: Python as the primary workflow language; Cartesian 2D/3D scope including
CS; author-reported brain MRI BART `.cfl`/`.hdr` inputs; BART-generated synthetic
phantoms as the development/testing basis; DICOM as a proposed complementary
reference; the initial `main` push at `aad0525`; and the continuing separation
between reported availability, validated recipes, implemented functionality and
experimental evidence. Historical extraction and Poisson/R=8/10-volumes/"200"
details were retained only with scope and correspondence limits.

Affected files: `README.md`, `docs/project-context.md`, `docs/input-inventory.md`,
`docs/open-questions.md`, `docs/data-and-ai-boundaries.md`,
`docs/copilot-handoff.md`, `.github/copilot-instructions.md`, this file, and
`.github/prompts/rvb-create-data-contract.prompt.md`. The data-contract drafts
were not edited. No tests, commands, commits, pushes or contract approval were
performed. Final author review of these documentation edits remains pending.

## Repository assembly and SSH preparation — 2026-10-23

Tool/access: ChatGPT, web interface. Ricardo supplied the staged file listing and
text diff, the SSH authentication output, and the chosen repository address.

The staged listing contains 39 files. Assistance identified stale starter wording
that still described imported scripts/reports as absent and a GitHub CLI/HTTPS
route that did not reflect Ricardo's chosen SSH setup. A documentation-only patch
updates these records and the setup instructions without changing numerical code,
metrics, figures, dependency versions or data boundaries.

SSH authentication succeeded as `rictr161`. The intended remote is
`git@github.com:rictr161/ensf620-bart-workflow.git`; Ricardo reports it is empty.
No private key or passphrase was supplied. GitHub CLI is not required for the
selected route. The assistant did not configure the remote, commit, push or rerun
MRI calculations on Ricardo's behalf. Patch application, author review and Git
operations must be verified from Ricardo's actual command output.

## Future entry template

Date(s):  
Tool/model and access mode:  
Task and affected files:  
Permitted input material:  
Accepted/corrected/rejected suggestions:  
Commands/tests actually executed and evidence:  
Limitations and unresolved discrepancies:  
Human review and related commit:
