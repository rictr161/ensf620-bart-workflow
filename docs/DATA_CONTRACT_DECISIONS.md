# Data Contract decisions and closure evidence

Contract: ENSF620-BART-DC v0.1.0-draft  
Prepared: 2026-10-23  
State: reviewable working register; no invented approval or private values.

Use this register to answer only the next consequential questions. Do not send real measurements, raw logs, extractor code, private paths, credentials, or permission correspondence to AI. A short reviewed description and an opaque reference to private evidence are sufficient.

## Established project decisions

| ID | Decision | Basis |
|---|---|---|
| D01 | AI supports development; it is not a runtime reconstruction agent or autonomous parameter optimizer | Proposal A/C/E |
| D02 | No AI access to laboratory data, derivatives, extractor, TALC, storage, or credentials | Proposal B/D/E |
| D03 | Ricardo reviews code, executes development tests, handles private inputs, and submits jobs; reviewed runtime continues after initiation | Proposal E |
| D04 | Compare manual/automated runs from the same exported inputs; upstream extraction is outside both measured tasks | Proposal C |
| D05 | Start with 3D Cartesian; availability/admission of other configurations remains conditional | Proposal B/C/F |
| D06 | Freeze numerical tolerances and action-counting rules before evaluation; retain failures | Proposal C/E/F |
| D07 | Public reproduction uses synthetic inputs without extractor, lab data, or TALC | Proposal D |
| D08 | Current local platform is reported as MacBook Pro Apple M5, 24 GB; Windows/WSL description is superseded | Later owner update |
| D09 | 2D/3D Cartesian originals are reported as `.h5`; that does not specify the exported interface | Later owner update |
| D10 | Repository/course documentation is English; working explanations are Spanish | Later owner preference |

These statements need not be asked again. If the owner corrects one, record the change and its effect explicitly. A contract revision must not be used to assume institutional permissions.

## Open decisions

| ID | Missing decision/evidence | Responsible party | What it blocks | Safe closure evidence |
|---|---|---|---|---|
| Q01 | Exact Copilot client/version, session mode, enabled tools, effective access boundaries | Ricardo | Claiming AI isolation; tool-based work beyond reviewed text | Description of client/mode and a check using harmless dummy paths; no real access test or secrets |
| Q02 | Intended-use permission and permitted processing destinations for each laboratory source | Ricardo with relevant laboratory authority | A use/destination whose authority is unclear | Private permission reference plus a reviewed status summary |
| Q03 | Actual exported format and validated interface of initial 3D Cartesian dataset | Ricardo with provider | Implementing/admitting the real input adapter | Reviewed descriptor of format, axes, complex representation, units, scaling, sampling and calibration; or wholly synthetic equivalent |
| Q04 | Extractor identity/version, dependencies, rights, and export evidence | Ricardo with provider | Complete upstream provenance; reproducing extraction | Private record; only shareable interface facts go to AI |
| Q05 | Baseline recipe and installed BART/Python build | Ricardo | Claiming a recipe works in the target environment | Reviewed command template with placeholders, version record, and synthetic evidence |
| Q06 | Numerical comparison representation, tolerances, zero/near-zero reference rules | Ricardo, with justified pilot evidence | Main numerical acceptance | Frozen protocol with formula, justification, version and synthetic pilot record; no lab outputs required for AI |
| Q07 | Operator-action granularity and timing/memory definitions | Ricardo | Main operational comparison | Frozen checklist and measurement definitions applied identically to both modes |
| Q08 | Which fields/results may leave private execution, for which audience | Ricardo with relevant laboratory authority | AI diagnostic sharing and public/course release | Separate allowlists and approval records for each intended destination |
| Q09 | TrueNAS destination approval, retention period/owner, temporary-copy deletion rule | Ricardo with supervisor/provider | Final archival/deletion actions | Private retention decision and verified-transfer record; do not expose storage path |
| Q10 | Validated admission and recipe-specific metadata for additional configurations | Ricardo with provider | Adding CS/radial/4D configurations to evaluation | Per-configuration validation and correctness evidence; no inferred mask/trajectory/dimension meanings |
| Q11 | Existing repository instructions, final location conventions, and actual release policy | Ricardo | Overwriting existing files or claiming release readiness | Reviewed current instructions and a proposed diff; no full private repository dump |

## Suggested first conversation in Copilot

Ask only Q01-Q03 first, in Spanish. If one is already answered, use the next consequential unresolved item. A useful response can be "unknown"; record it rather than guessing.

1. **Entorno de Copilot:** "¿Qué cliente y modo vas a usar, y qué herramientas tendría habilitadas? Basta describirlo; no compartas credenciales ni pantallas privadas."
2. **Autoridad del uso:** "¿Qué usos y destinos de procesamiento del laboratorio ya están confirmados y cuáles siguen pendientes? Indica el estado, sin adjuntar correspondencia privada."
3. **Interfaz exportada:** "¿Qué formato produce el extractor para el caso 3D cartesiano y cuáles son sus ejes/convenciones confirmados? Puedes responder que sigue pendiente; no adjuntes datos, headers ni el extractor."

The initial draft remains useful with unknowns. Safe documentation and synthetic development continue while affected real-data uses remain blocked.

## Proposal correction log

| Item | Earlier proposal text | Later context | Contract treatment |
|---|---|---|---|
| Local environment | Windows/WSL, 24 GB RAM | MacBook Pro Apple M5, 24 GB | Use macOS/arm64 context; measure and record actual installed versions separately |
| Input containers | Exported k-space, no concrete export layout established | Original Cartesian scanner files reported as `.h5` | Record the original container only; do not assume workflow export is HDF5 |
| Retention | TrueNAS proposed; terms to be agreed | No completed agreement supplied | Keep destination/retention unresolved |
| Verified baseline | Planned development output | No verification evidence supplied here | Do not label completed or validated |

## Acceptance record to complete later

This is a record of future review, not a signature:

| Field | Current value |
|---|---|
| Contract version accepted by owner | Not recorded |
| Acceptance date | Not recorded |
| Scope of acceptance | Not recorded; must distinguish document requirements, laboratory admission, evaluation and release |
| Private authority evidence references | Not recorded |
| Implemented controls and evidence | Not supplied |
| Remaining blockers | Q01-Q11 as applicable |

For each change record the date, decision ID, old/new wording, rationale, owner, private or shareable evidence reference, affected requirements/tests, and whether a new evaluation is required. Never fill unknown fields with invented values for presentation completeness.
