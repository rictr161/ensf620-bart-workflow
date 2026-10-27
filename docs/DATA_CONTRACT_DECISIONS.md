# Data Contract Decisions and Closure Evidence

Contract: ENSF620-BART-DC v0.3.0  
Prepared: 2026-10-27  
State: OWNER_ACCEPTED; no invented approval or private values.

This register records decisions about the AI data-access and action boundary.
It does not define the reconstruction software, dataset inventory, or
evaluation protocol.

## Established decisions

| ID | Decision | Status | Effect |
|---|---|---|---|
| D01 | AI supports supervised development; it is not a runtime reconstruction agent or autonomous parameter optimizer | CONFIRMED_CONTEXT | Separates assistant actions from reviewed Python/BART execution |
| D02 | AI has no access to laboratory data, derivatives, DICOM, extractor, credentials, private storage, or TALC | CONFIRMED_CONTEXT | Restricted classes remain inaccessible |
| D03 | Ricardo reviews context and code, handles authorized private inputs, and separately initiates reviewed software | CONFIRMED_CONTEXT | Human authorization and private execution remain distinct from AI access |
| D04 | The assistant may use explicitly supplied reviewed project documents, reviewed code, and cleared synthetic/public material | CONFIRMED_CONTEXT | Defines the permitted development context |
| D05 | File discovery, command execution, network, remote systems, HPC, publication, and destructive actions are not implied by a documentation task | ACCEPTED_POLICY | Requires explicit task-specific authorization |
| D06 | Unknown classification, authorization, audience, or effective isolation is treated as restricted until resolved | ACCEPTED_POLICY | Blocks only the affected action; safe unaffected synthetic work may continue |
| D07 | Written instructions, `.gitignore`, editor guidance, private repository status, and UI labels are not enforced access controls | CONFIRMED_CONTEXT | Prevents claims of technical isolation from documentation alone |
| D08 | Repository documentation is English and working explanations are Spanish | CONFIRMED_CONTEXT | Applies to this contract and register |
| D09 | The instructor's evaluation recommendation remains project-planning context, not a normative access or software rule in this contract | CONFIRMED_CONTEXT | Prevents this boundary document from hard-coding evaluation scope |
| D10 | Experimental DICOM is restricted; any future comparison remains outside this boundary contract | CONFIRMED_CONTEXT | No DICOM access or comparison protocol is authorized here |
| D11 | The drafting session used Read and edit operations on authorized documents | CURRENT_DRAFT_RECORD | Records tool use without claiming isolation or control verification |

## Existing requirement disposition

| Baseline ID | Disposition in v0.3.0 | Reason |
|---|---|---|
| `DC-001`–`DC-009` | Retained as normative boundary requirements | They govern assistant access, authority, classification, lifecycle, retention, and environment boundaries |
| `DC-010`–`DC-012` | Excluded from normative scope | They specify input interfaces and file-handler validation |
| `DC-013`–`DC-016` | Retained as normative boundary requirements | They govern safe actions, runtime separation, human initiation, and network behavior |
| `DC-017`–`DC-018` | Excluded from normative scope | They specify runtime output, provenance, and verification behavior |
| `DC-019`–`DC-020` | Split by subject, not reused | Private-record non-disclosure is retained in the boundary; runtime log/export field design is excluded |
| `DC-021`–`DC-025` | Excluded from normative scope | They specify paired execution, metrics, correctness, evaluation, and action-counting |
| `DC-026`–`DC-031` | Retained where they govern AI/repository/release/incident/change boundaries | Software and evaluation details are not retained as contract obligations |

No excluded requirement is claimed to have been relocated, implemented, or
approved elsewhere. No `DC-REQ-*` catalogue is used; those labels were
intermediate chat-only proposal labels and are retired as non-canonical.

## Open decisions and evidence

These are retained only when they affect the access/action boundary. Dataset
counts, array metadata, recipe details, numerical values, and evaluation
decisions are not reopened by this register.

| ID | Missing decision/evidence | Operation affected | Non-sensitive closure evidence |
|---|---|---|---|
| Q01 | Effective Copilot client/mode/tool boundaries if a technical isolation claim is needed | Claiming isolation or authorizing tool-based work beyond reviewed text | Client/mode/tool description and harmless-boundary check; no private data |
| Q02 | Intended use and permitted destination for a specific laboratory source | Sharing or private processing destination for that source | Operator-held permission reference and reviewed status summary |
| Q08 | Which fields/results may leave private execution and for which audience | AI diagnostic sharing, course review, or public release | Audience-specific allowlist and approval record |
| Q09 | Retention owner, destination, and deletion conditions | Archival, temporary-copy deletion, or destructive cleanup | Private retention decision and transfer/deletion evidence |
| Q11 | Task-specific file location and release policy when a future operation needs them | Editing, publication, staging, or release claim | Explicit task authorization and reviewed allowlist |

The former `Q03`–`Q07` and `Q10` questions remain historical project questions
in the prior working register, but they are outside this contract's purpose and
are not required to complete this access-boundary draft. They must not be
silently treated as resolved or redefined here.

## Verification and implementation status

| Boundary area | Requirement status | Technical status |
|---|---|---|
| Reviewed-context allowlist | ACCEPTED_POLICY | NOT_IMPLEMENTED / NOT_VERIFIED |
| Restricted data and system separation | ACCEPTED_POLICY | NOT_IMPLEMENTED / NOT_VERIFIED |
| Task-specific authorization for edits, commands, network, HPC, and release | ACCEPTED_POLICY | NOT_IMPLEMENTED / NOT_VERIFIED |
| Unknown classification and incident response | ACCEPTED_POLICY | NOT_IMPLEMENTED / NOT_VERIFIED |
| Runtime/assistant separation | ACCEPTED_POLICY | NOT_IMPLEMENTED / NOT_VERIFIED |
| Repository/publication boundary | ACCEPTED_POLICY | NOT_IMPLEMENTED / NOT_VERIFIED |

The existing verification identifiers remain traceable as follows:

| Verification ID | Treatment |
|---|---|
| `V01` | Relevant future evidence for AI/tool boundary; not verified |
| `V02` | Relevant future evidence for authority/classification; not verified |
| `V03` | Relevant future evidence for source/output boundary controls; not implemented |
| `V04` | Excluded input validation evidence; not an acceptance test for v0.3.0 |
| `V05` | Relevant only for safe command/configuration boundary; not implemented |
| `V06` | Excluded runtime failure/provenance evidence; not an acceptance test for v0.3.0 |
| `V07` | Relevant future evidence for private/shareable record separation; not implemented |
| `V08` | Excluded scientific/evaluation evidence; not an acceptance test for v0.3.0 |
| `V09` | Excluded evaluation/action-counting evidence; not an acceptance test for v0.3.0 |
| `V10` | Relevant future repository/release evidence; not implemented |
| `V11` | Relevant future environment/incident/change evidence; not verified |

## Acceptance record

| Field | Current value |
|---|---|
| Contract version accepted by owner | ENSF620-BART-DC v0.3.0 |
| Acceptance date | 2026-10-27 |
| Scope accepted | AI data-access and action boundaries for supervised development |
| Document state | OWNER_ACCEPTED |
| Accepted by | Ricardo |
| Previous working version | 0.3.0-draft |
| Evidence | Owner's explicit acceptance in this conversation |
| Institutional permission | Not recorded here |
| Technical controls implemented | None established; technical status remains NOT_IMPLEMENTED / NOT_VERIFIED |
| Remaining access/action decisions | Q01, Q02, Q08, Q09, and Q11 as applicable |
