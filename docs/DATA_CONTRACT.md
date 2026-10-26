# ENSF 620 BART Reconstruction Data Contract

| Document field | Value |
|---|---|
| Contract ID | ENSF620-BART-DC |
| Version | 0.1.0-draft |
| Prepared | 2026-10-23 |
| Document state | DRAFT_REVIEW_REQUIRED |
| Project owner/operator | Ricardo |
| Technical enforcement state | NOT_IMPLEMENTED_OR_VERIFIED_BY_THIS_DELIVERABLE |
| Owner acceptance | Not yet recorded |
| Laboratory permission evidence | Must be recorded privately for the intended use; this document grants no new permission |

## 1. Purpose, scope, and sources

The contract specifies the input/output interface and handling rules for a Python workflow that orchestrates reviewed BART reconstruction recipes. Its goals are consistent input interpretation, reproducible paired execution, preservation of source data, controlled sharing, and prevention of unauthorized AI access.

The scientific question is whether the automated workflow reduces manual intervention while maintaining numerical equivalence with verified manual reconstruction. Timing and memory are secondary. The software does not introduce new reconstruction algorithms or autonomously optimize parameters. The AI assistant supports development and explanation; it is not a reconstruction-time agent. [P: A, p.1; C, pp.2-3; E, p.5]

The contractual input boundary begins at exported k-space and required metadata. Scanner extraction is an upstream dependency and is excluded from the manual/automated comparison. This does not exempt the exported inputs from integrity, authority, or semantic validation. [P: C, pp.2-3]

### Evidence labels

- **P - Proposal commitment:** the attached ENSF 620 Project Proposal, sections A-F. This is evidence of planned requirements, not proof of completed processing or installed controls.
- **U - Owner-reported update:** subsequent project discussion, summarized in `PROJECT_CONTEXT_FOR_AI.md`. Reported environment and input details are not independent technical validation.
- **C - Proposed control:** an operational safeguard specified by this draft. It needs owner acceptance and implementation evidence where applicable.
- **UNKNOWN:** unresolved. The relevant operation remains blocked until the stated closure evidence exists.

The latest explicit owner correction supersedes an earlier project fact, with the change recorded. No instruction or project decision can manufacture third-party rights or institutional approval. Existing proposal restrictions on AI access apply while this document is a draft.

## 2. Roles and trust boundaries

| Actor/environment | Permitted role | Boundary |
|---|---|---|
| Ricardo, operator | Review code, inspect authorized private inputs, run development checks, initiate reviewed workflows, personally submit TALC jobs, review exports | Retains responsibility for permission and sharing decisions |
| AI assistant and its tools | Explain public documentation, draft original code/documents, propose synthetic examples and checks, reason about approved diagnostics | No laboratory data, extractor, credentials, private storage, or TALC access |
| Reviewed Python/BART runtime | Process admitted inputs in an authorized local or HPC execution environment after human initiation | No AI calls or implicit publication; laboratory roots remain private, while synthetic/public-licensed cases follow their reviewed sharing classification |
| Laboratory provider/supervisor | Clarify acquisition semantics and applicable conditions of use, retention, and release | Their involvement is not evidence of blanket redistribution approval |
| External reviewer/public CI | Reproduce the synthetic route using reviewed source/configuration and synthetic inputs | No laboratory dataset, extractor, credentials, or TALC dependency |

**DC-001 (P/C):** The assistant must not inspect, process, or transmit restricted materials, including through terminal tools, MCP, remote editors, symlinks, screenshots, notebook outputs, or an uploaded small sample. Ricardo may execute the reviewed program independently against authorized inputs. Permission for the program does not extend to the assistant.

**DC-002 (C):** The AI development environment must contain only material cleared for that environment and must have no effective route to restricted roots, mounts, credentials, or remote sessions. If isolation is not established, use a separate text-only drafting interface with explicitly reviewed context, no private workspace context, and no execution or discovery tools. A tool-free editor session may still supply its active file, selection, or other automatic context: keep restricted files closed and outside that environment, and verify the context before submission. Keep Copilot and other AI extensions disabled in the private processing/remote TALC environment. Do not represent an open-folder boundary, worktree, Python virtual environment, or `.gitignore` as operating-system isolation.

**DC-003 (P/C):** The operator reviews commands and executes development tests. The assistant may propose tests; it must not auto-run them. Any later permission for a particular synthetic test is limited to an environment verified to exclude restricted material. The assistant never submits laboratory or TALC jobs under this contract.

These are required behaviors and proposed deployment conditions. Their presence in Markdown does not enforce them. Client instructions and content exclusions are supplementary; their applicability depends on the actual product, plan, mode, and tools. [S2-S6]

## 3. Inventory, classification, and permission

Availability, permission, and technical admission are separate attributes.

| Configuration | Availability evidence | Current admission evidence |
|---|---|---|
| 2D Cartesian | Received, reported in proposal | Interface/recipe evidence not supplied to this draft |
| 3D Cartesian | Received; intended first experimental baseline | Interface/recipe evidence not supplied to this draft |
| 3D CS | Received, reported in proposal | Sampling/calibration/recipe evidence not supplied to this draft |
| 4D Cartesian | Pending in proposal | Not established |
| 4D CS | Pending in proposal | Not established |
| 2D radial | Pending in proposal | Not established |
| 3D radial | Pending in proposal | Not established |

The measurements are described as GRE acquisitions of a spherical phantom. Original 2D/3D Cartesian files have later been reported as `.h5`; exported format and internal layout remain unresolved. No received configuration is declared validated by this document. [P: B, pp.1-2; U]

| Classification | Examples | AI context | GitHub/public release |
|---|---|---|---|
| RESTRICTED_LAB | Raw data, exported k-space, lab-derived arrays/images, masks/calibration derived from lab data | Prohibited | Prohibited under the current contract; a separately authorized, reviewed derivative needs its own release decision |
| RESTRICTED_EXTRACTOR | Laboratory/GE extraction code, binaries, restricted documentation | Prohibited | Prohibited without separately established rights and a contract revision |
| RESTRICTED_ACCESS | Credentials, private URLs, hosts/paths, account details, access tokens | Prohibited | Prohibited |
| PRIVATE_RECORD | Real run manifests, checksums, full logs, command lines, acquisition metadata, operator records containing private details | Not automatically allowed | Not automatically allowed |
| PROJECT_CODE | Original workflow code, sanitized templates, documentation with no embedded private values | Allowed after review | Allowed after ownership/license and release review |
| SYNTHETIC | Independently generated phantom fixtures, generation code, resulting synthetic verification records | Allowed after review | Allowed after release review; must not embed laboratory samples or identifiers |
| PUBLIC_LICENSED | Public source/data with recorded terms | Only when those terms and the intended AI use allow it | Only as permitted by the license/terms, with attribution |
| RELEASE_CANDIDATE | A new summary constructed from approved fields | Only with explicit AI-sharing clearance | Only with separate public-release clearance |
| UNKNOWN | Origin, rights, or contents unresolved | Prohibited pending resolution | Prohibited pending resolution |

**DC-004 (P/C):** Possession, a phantom label, pseudonymization, a private GitHub repository, or availability online does not establish sharing authority. Approval for AI context and approval for public release are distinct decisions.

**DC-005 (P/C):** A private inventory records provenance, receipt date, source version, opaque dataset ID, laboratory contact, intended use, permitted environments, and permission evidence. A public inventory must omit private identities/paths/links and include only separately approved facts. An opaque public ID must not be a reversible encoding of a private filename.

**DC-006 (P):** Public inputs require source, version/commit where applicable, access date, license/terms, and attribution. Unclear authority pauses that source's affected use; synthetic development can continue.

## 4. Lifecycle, custody, and environment

**DC-007 (P/C):** Source measurements and exported input sets are immutable for reconstruction. Keep source, export, and run-output areas distinct. Use read-only source permissions where feasible; record private input integrity before use and detect changes. Never write output into the input tree or overwrite an existing run silently.

**DC-008 (P):** TALC is a working environment, not the sole archival copy. Verify current cluster conditions and the course allocation before use. The proposal's statements about TALC retention are planning context, not a schedule to automate without checking. TrueNAS is a proposed archival destination; the owner and supervisor must settle destination approval, retention, and removal of working copies. Verify transfers before deleting temporary copies. Do not delete shared source files without the provider's agreement. [P: B, p.2]

**DC-009 (P/U):** Record actual local and HPC environments separately. The current owner-reported local machine is a MacBook Pro, Apple M5, 24 GB RAM; this supersedes the proposal's Windows/WSL description. Record the actual OS/architecture, Python and BART versions/build, numerical libraries, threads/resources, and run-relevant settings without dumping the environment. BART version, build, and readiness are not established here.

## 5. Input interface specification

The following is a proposed field catalogue for an eventual machine-validated dataset manifest. It is not an implemented JSON/YAML schema and is not evidence that any private file conforms. A future schema must specify types, allowed fields, conditional requirements, version compatibility, and bounds, with tests linked to this contract.

Private path bindings are stored outside the AI-accessible repository and supplied only to the reviewed runtime. Repository examples use synthetic identifiers and symbolic roots. Do not place real private values in sample configuration.

| Field/group | Type and requirement | Validation/meaning |
|---|---|---|
| `schema_version` | Required supported version string | Reject unknown/incompatible versions; no silent migration |
| `dataset_id` | Required opaque string | Unique within inventory; no private filename/contact embedded |
| `source_class` | Required dataset-class enum | Only RESTRICTED_LAB, SYNTHETIC, or PUBLIC_LICENSED; other artifact classes in section 3 are not reconstruction datasets; permission and technical admission still required |
| `acquisition_type` | Required explicit enum | One of the seven planned configurations or an explicitly added versioned type |
| `availability` / `admission_state` | Required separate enums | Receipt alone never equals admission |
| `authority_ref` | Required private evidence reference for external sources | Intended use and environment verified by operator; do not publish evidence contents |
| `files[]` | Required nonempty list | Explicit file roles; no broad filesystem discovery |
| `files[].relative_path` | Required relative path under private input root | Reject absolute paths, traversal, URL schemes, and unsupported links |
| `files[].role` | Required supported role | K-space, trajectory, mask, calibration, reference, or other reviewed role |
| `files[].format` / `format_version` | Required format; version when relevant | Determined from verified export interface, not a guessed extension |
| `files[].size_bytes` / `checksum` | Required integrity values, private | Match actual local bytes; SHA-256 is the proposed checksum algorithm |
| `array.dtype` / `complex_encoding` | Required per numeric payload | Explicit precision, byte order where relevant, complex storage representation |
| `array.shape` | Required positive integer list | Rank/shape and payload size must agree; resource bounds checked |
| `array.axes[]` | Required one-to-one semantic mapping | Axis index, meaning, extent; map into the installed BART conventions explicitly |
| `array.units` / `scaling` | Required documented conventions | Include Fourier centering/normalization and any preprocessing scaling |
| `sampling` | Required explicit description | Fully sampled/undersampled; mask or index representation and interpretation verified |
| `trajectory` | Conditional for non-Cartesian recipes | Coordinates, dimensions, units, axis order/signs, centering, sample alignment verified |
| `density_compensation` | Conditional on recipe | Method/weights or an explicitly justified not-required decision |
| `calibration` | Conditional on recipe | Provenance of maps/calibration, coil processing and compatibility; no guessed files |
| `temporal_or_other_axes` | Conditional for 4D or additional dimensions | Explain what the extra dimension means; never infer time from the label "4D" |
| `preprocessing` | Required, possibly explicitly empty | Versioned transformations applied before input to paired recipes |
| `recipe_id` / `recipe_version` | Required | Reviewed recipe and installed BART compatibility; not executable free text |
| `validation_record_ref` | Required for admission | Operator-reviewed private evidence; public summary only after export review |

**DC-010 (P/C):** Missing metadata, mask, trajectory, axis meaning, or scaling blocks the affected recipe. Do not infer masks solely from zero-valued samples, invent radial angles, or reshape until a plausible image appears. A not-applicable field needs a recipe-specific justification; it is not a substitute for unknown information.

**DC-011 (C):** A future validator must reject unknown required-field values, unsupported extra fields, absent files, mismatched payload sizes, incompatible axes, non-finite values, and unverified conditional metadata before reconstruction. Headers and private metadata are inspected only by the operator/reviewed program in the private environment.

**DC-012 (C):** File handlers must not execute content. Disallow unsafe pickle/object deserialization and executable YAML/configuration. Reject external HDF5 links or virtual datasets unless support and permitted targets are explicitly reviewed. Reject unexpected archive extraction or network-backed file references. Apply bounded reads and resource checks appropriate to each supported format.

## 6. Configuration and runtime behavior

**DC-013 (P/C):** Configuration contains explicit, typed, allowlisted reconstruction parameters and stopping criteria. Reject unknown keys, unsupported options, invalid values, and a missing recipe. Keep paths/secrets out of versioned templates. There is no parameter search or AI decision in the runtime.

**DC-014 (C):** Resolve private inputs against an operator-configured input root and outputs against a separate run root. Enforce containment after path resolution, reject unsupported symlinks and traversal, and check that source and destination cannot alias. Default to rejecting links; documented exceptions require a new reviewed rule. Permissions must support these boundaries; path checks alone are insufficient in an adversarial shared filesystem.

**DC-015 (C):** Build BART invocations from a fixed executable and validated argument lists, without interpreting a shell command stored in configuration. A Python implementation should use argument arrays with `shell=False` or an equivalently constrained interface. Do not use `eval`, dynamically loaded arbitrary plugins, or file contents as instructions. Check exit status and explicit output expectations.

**DC-016 (P/C):** Human initiation is required. The program may then validate, reconstruct, compare, and organize outputs automatically. It must not access an external AI service or upload telemetry containing inputs/outputs. Any new network transfer feature requires a separate documented use and permission review. Operator-controlled staging and job submission remain outside the assistant's access.

## 7. Outputs, provenance, and failure states

Every run uses a unique ID and a separate output directory. Store the full run record privately when any component derives from laboratory material. [P: D, p.4]

Required run-record groups are:

- Contract and manifest versions; recipe/version; source classification and private dataset reference.
- Git revision and whether the code has uncommitted modifications; a final evaluated/released run needs a reproducibly identified source state.
- Private input/output checksums; resolved configuration; invoked commands; environment/build and relevant numerical settings.
- Resource configuration, execution mode, repeat number, timestamps/durations, exit status, and output inventory. Use consistent units; separate queue time from process time and define the memory measure.
- Dimensions/representation/scaling checks, finite-value checks, correctness/paired comparison results, tolerance/protocol version, and structured failure codes.
- Operator-action checklist and failure/recovery references where part of evaluation.

**DC-017 (P/C):** Distinguish `REJECTED_INPUT`, `EXECUTION_FAILED`, `VERIFICATION_FAILED`, and `VERIFIED`. Do not report a run as verified because a file exists or the process returned zero. Missing output, incompatible dimensions, NaN/Inf, unsuccessful execution, or exceeded acceptance thresholds is a failure. Preserve evidence without overwriting the failed run.

**DC-018 (P/C):** Preserve private provenance and record corrections as new versions/runs. Checksums support identity and change detection; they do not prove scientific correctness, anonymization, or permission to share.

## 8. Logs, diagnostics, and controlled export

**DC-019 (P/C):** Use two distinct records: a private execution record and a separately constructed export summary. Never treat a private record as shareable merely by removing a few strings. Do not dump all environment variables, credentials, raw arrays, headers, or unrestricted object representations into logs. BART stderr, scheduler logs, stack traces, notebooks, plots, filenames, and command arguments may contain restricted content.

**DC-020 (C):** Proposed export fields are an opaque release-case ID, source category, reviewed recipe/protocol version, reviewed code revision, execution mode/repeat index, agreed aggregate metrics with units, status/failure category, and a shareable evidence reference. These are candidates, not an approved public schema. Exact fields, granularity, identifiers, and results require owner review and any applicable laboratory permission before use.

Publication follows this sequence:

1. The operator selects the permitted purpose and audience: AI debugging, course review, or public release.
2. The private runtime constructs a candidate using an explicit field allowlist; unknown fields fail export.
3. Local checks look for private paths/links, identifiers, credentials, unsafe embedded outputs, and unexpected files. These checks reduce risk but cannot prove absence of all sensitive information.
4. The operator reviews the candidate and records the release decision privately.
5. Only the approved candidate reaches the chosen destination. Do not attach source records for extra context.

A wholly synthetic failure reproduction is the preferred AI debugging input. A laboratory diagnostic summary must be minimal and cleared for the intended external AI use. [P: E, p.5]

## 9. Numerical acceptance and evaluation integrity

**DC-021 (P):** Match input files, preprocessing, parameters, stopping criteria, software settings, output conventions, and resource allocation within each pair. Compare TALC to matched TALC execution, or matched local execution for fallback. Keep extraction outside the measured task in both modes. Dataset-specific preparation after extraction, configuration, initiation, inspection, and manual organization stay inside it. [P: C, pp.2-4]

**DC-022 (P/C):** For a nonzero manual reference use the proposal's relative L2 difference:

\[
e_{\mathrm{rel}} = \frac{\|x_{\mathrm{auto}}-x_{\mathrm{manual}}\|_2}{\|x_{\mathrm{manual}}\|_2}.
\]

Define whether the comparison uses complex or another justified representation, with fixed axis/order/scaling conventions before evaluation. Do not fit a phase, gain, normalization, alignment, or crop after seeing a discrepancy merely to obtain agreement. Any scientifically justified transformation must be part of the frozen protocol applied consistently.

Numerical thresholds are `UNKNOWN`, not arbitrary defaults. The exact zero-reference rule and any near-zero stability rule remain unresolved. A proposed option is a separately justified absolute-error criterion for zero references; no run may receive a numerical pass using that option until its formula, threshold, and independent basis are accepted. Never replace a zero denominator with an unreviewed epsilon.

**DC-023 (P):** A fully sampled synthetic Cartesian known-answer case and an independent Fourier reconstruction are required for the initial correctness check. Each additional recipe needs appropriate independent or separately justified checks. Two modes that share a wrong interpretation can agree numerically, so agreement alone is insufficient. [P: C, p.3; E, p.5]

**DC-024 (P/C):** Separate pilot/development decisions from frozen evaluation. Justify tolerances and action-count granularity during pilots; freeze the recipe, configuration, datasets admitted for evaluation, criteria, and counting rule before measuring. A later correction creates a versioned protocol change and new paired evaluation, retaining the earlier failures and the reason for change. Do not tune tolerances or select favorable repeats after observing results.

An ML train/validation/test split is not required by this reconstruction-workflow project. The relevant protection is against retrospective changes to acceptance, selection, normalization, or counting. If a pilot dataset is reused, disclose that fact and the limits of the resulting evidence; do not claim an independent held-out assessment.

**DC-025 (P):** Record observable operator actions using the same frozen rule for both modes; do not count individual keystrokes or software-only operations. Keep learning, setup, and one-time development separate from operational measurements. Preserve failed attempts and recovery actions. Report a reduction as a verified benefit only when its paired outputs pass the criteria. Targets of three repetitions per mode and one dataset per received configuration are planning targets, not completed evidence. [P: C, p.3; F, pp.5-6]

## 10. Repository, CI, and release

**DC-026 (P/C):** The repository contains original source, reviewed configuration examples, tests using synthetic inputs, generation scripts, environment specifications, documentation, and permitted summaries. Laboratory data, exported k-space, extractor code, credentials, private links, and unreviewed outputs remain outside it and outside the AI environment. Do not include the original proposal PDF or unnecessary personal identifiers in this kit's release.

Apply the same boundary to commits/history, Git LFS payloads, attachments, issues/PRs, CI logs, caches/artifacts, notebooks, screenshots, release archives, and shared terminal output. A private repository does not automatically satisfy the AI or redistribution boundary.

**DC-027 (C):** Use `.gitignore` only as accidental-staging protection. It does not hide already tracked files and is not an AI/filesystem access control. Use explicit release allowlists, local checks of staged content, and owner review. Do not force-add excluded material. If restricted material was already committed, an ignore rule does not remove it from history. [S5]

**DC-028 (P/C):** Public CI/reviewer reproduction uses synthetic generation and no laboratory secrets, mounts, extractor, or TALC. Do not run untrusted CI on a host with laboratory access. The final release must have a tag/commit, reviewed contents, and a clean-checkout reproduction record with failures and limitations disclosed. Synthetic reproduction does not reproduce private experimental findings by itself. [P: D, p.4]

**DC-029 (P/C):** Maintain `AI_USE.md` with material assistance, tool/mode, model when available, affected code/text, corrections/rejections, and verification evidence. Do not copy restricted prompts, logs, or data into that record. [P: D-E, pp.4-5]

## 11. Incident handling and changes

**DC-030 (C):** On suspected exposure, stop the affected transmission/publication, avoid repeating the contents, and preserve evidence privately. The operator informs the relevant owner/maintainer and follows the applicable response process; affected credentials require revocation/rotation by the authorized person. Deleting a local file does not prove removal from remote histories, caches, or chats. The assistant must not perform unilateral cleanup or hide evidence.

**DC-031 (C):** Changes to data classes, AI access, interface semantics, export fields, numerical criteria, retention, or allowed destinations require a versioned decision, impact review, and new relevant evidence. A new acquisition type is not admitted by renaming an old manifest. Minor editorial changes do not imply changed permissions.

## 12. Verification matrix

These are acceptance specifications, not implemented or executed tests. All executable tests proposed here use synthetic/dummy fixtures. Private permission, storage, and real-input checks are carried out by the operator without sending their contents to AI.

| Evidence ID | Requirements | Check/control | Required expected outcome | Current state |
|---|---|---|---|---|
| V01 | DC-001-003 | Inspect AI tool permissions/mounts using harmless dummy locations; record client/mode | Restricted roots/credentials absent or access technically denied; no agent execution on real inputs | Not verified |
| V02 | DC-004-006 | Private permission and inventory review | Intended use/environment confirmed; AI/public sharing separately decided | Not verified |
| V03 | DC-007,014 | Synthetic source checksums, output collision, traversal, symlink, input/output alias cases | Source unchanged; unsafe targets rejected before writing | Not implemented |
| V04 | DC-010-012 | Missing role/metadata, wrong dtype/shape/size, unknown fields, NaN/Inf, external-link fixtures | Input rejected with a structured private error; no reconstruction | Not implemented |
| V05 | DC-013-016 | Unknown option, shell-like payload, unsupported recipe, mocked network attempt | Configuration rejected; no shell interpretation or external transmission | Not implemented |
| V06 | DC-017-018 | Simulated nonzero exit, missing/truncated output, verification failure, rerun | Failure retained; no false verified state or overwritten evidence | Not implemented |
| V07 | DC-019-020 | Dummy secret/path/URL markers in synthetic diagnostic records; unexpected export fields | Candidate rejected or markers absent by construction; raw records never exported | Not implemented |
| V08 | DC-021-024 | Known synthetic Cartesian image, independent Fourier result, paired outputs, zero-reference case | Pass/fail follows a justified frozen protocol; unknown zero rule blocks acceptance | Not implemented; thresholds unresolved |
| V09 | DC-024-025 | Review evaluation freeze and versioned action checklists | Same rules/resources; failures and recovery retained; no retrospective threshold tuning | Not verified |
| V10 | DC-026-028 | Dummy forbidden file in staging/archive plan; clean synthetic reproduction | Release blocked for forbidden material; approved route needs no private input | Not implemented |
| V11 | DC-008-009,029-031 | Operator review of retention/environment/AI-use/change/incident records | Roles and decisions recorded without publishing private values | Not verified |

For each eventual result, record test/check ID, exact code and contract versions, environment, date, expected/actual outcome, responsible reviewer, and private or approved shareable evidence location. A review of this document is not a substitute for V01-V11.

## 13. Gates and current limitations

| Gate | Required before proceeding | Current document conclusion |
|---|---|---|
| Safe drafting/synthetic development | Reviewed context; no restricted AI access | Supported within the stated boundary; runtime test evidence still required |
| Laboratory dataset admission | Intended-use evidence; verified interface/semantics; validated input; effective execution boundaries | Not established by this draft |
| Recipe evaluation | Admitted inputs; independently checked recipe; frozen protocol/tolerances/counting; matched resources | Not established by this draft |
| External AI diagnostic sharing | Explicit purpose, minimal approved content, permitted external use | Must be decided per candidate; no blanket approval |
| Public release | Rights/field allowlist; content review; synthetic reproduction; tag/commit/evidence | Not approved by this draft |
| Archival/deletion | Agreed destination, retention responsibility, transfer verification, deletion authority | Pending owner/laboratory decisions |

Open decisions and closure evidence are listed in `DATA_CONTRACT_DECISIONS.md`. No real input was inspected, no extractor was reviewed, no BART reconstruction was run, no institutional permission was obtained, and no technical control was deployed as part of preparing this draft.

## 14. Source references

- **P:** supplied ENSF 620 Project Proposal, sections A-F, pp.1-6. The original PDF stays outside this kit.
- **U:** later owner-reported environment and input-inventory updates, explicitly distinguished from P in `PROJECT_CONTEXT_FOR_AI.md`.
- **S1:** [Rigour Vibe specification workflow, pinned reference](https://github.com/EthanMacDonald/Rigour_Vibe/blob/307d910663ee481279c319852ef4120e793e0207/prompts/rvb-create-spec.mdc).
- **S2:** [GitHub repository instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions).
- **S3:** [VS Code prompt files](https://code.visualstudio.com/docs/agent-customization/prompt-files) and [migration between agent environments](https://code.visualstudio.com/docs/agent-customization/migrate-customizations).
- **S4:** [GitHub content exclusion](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/content-exclusion) and [September 2026 app/CLI update](https://github.blog/changelog/2026-09-02-content-exclusions-generally-available-in-copilot-app-and-cli/).
- **S5:** [Git ignore-file semantics](https://git-scm.com/docs/gitignore).
- **S6:** [VS Code AI security guidance](https://code.visualstudio.com/docs/agents/run/security) and [agent sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing).

Software compatibility information was checked on 2026-10-23. Recheck it when the installed client or execution mode changes. This contract is a project engineering specification, not a claim of institutional approval, statutory compliance, or zero leakage risk.
