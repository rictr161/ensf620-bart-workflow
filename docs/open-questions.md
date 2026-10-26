# Open Questions and Stop Conditions

Pending means not established in this record, not permission to guess or silently
substitute information. The current implementation boundary is author-reported
BART `.cfl`/`.hdr` inputs for brain MRI 3D Cartesian work, including CS. Earlier
extraction questions remain historical/upstream context rather than current
workflow implementation blockers.

| ID | Question | Current status |
| --- | --- | --- |
| DATA-01 | File, acquisition and dataset counts per configuration? | Private inventory pending |
| DATA-02 | Complex representation and every dimension meaning? | Current BART interface/metadata review needed |
| DATA-03 | `.cfl`/`.hdr` scaling, centering and channel conventions? | Input contract pending |
| DATA-04 | Current 3D CS sampling geometry, mask and recipe settings? | Not established |
| DATA-05 | Earlier acceleration/volume details correspond to current data? | Do not assume; correspondence unknown |
| DATA-06 | Earlier "200" detail applies to current data? | Do not assume; meaning unresolved |
| EXTRACT-01 | Historical extractor identity/version and invocation? | Upstream provenance only; not a current implementation blocker |
| EXTRACT-02 | Historical extractor dependencies and platform requirements? | Upstream provenance only; do not reuse synthetic environment by assumption |
| EXTRACT-03 | Historical extractor outputs and supported configurations? | Upstream provenance only; not a current implementation blocker |
| AUTH-01 | Documented permitted uses and processing/storage locations? | Confirm before each experimental dataset |
| AUTH-02 | TrueNAS retention and student-copy deletion terms? | Confirm with laboratory supervisor/steward |
| AUTH-03 | Which summaries/outputs may be shared? | Do not infer permission |
| ENV-01 | Full BART commit and actual Makefile.local? | Only v1.0.00/short 37f3c5f and selected flags observed |
| ENV-02 | TALC environment and resource configuration; ARC alternative? | Separate deployment record pending |
| VERIFY-01 | Pilot-justified numerical tolerance and action-count rule? | Human approval before main evaluation |
| VERIFY-02 | Negative tests and clean-checkout reproduction? | Not performed in this starter |
| GIT-01 | Current branch publication and clean-checkout evidence? | Initial `main` push at `aad0525` is author-reported; current working branch and clean checkout not established |
| GIT-02 | Commit identity and reviewer access? | Pending; no credentials in files |

Pause affected experimental work if authority is unclear; continue with synthetic
inputs. Missing acquisition information blocks recipes depending on it, not all
learning. Unresolved numerical discrepancies block promotion to evaluation.
Record exclusions and reasons at the November 6 gate.
