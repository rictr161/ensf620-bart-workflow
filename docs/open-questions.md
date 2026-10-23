# Open Questions and Stop Conditions

Updated: 2026-10-23. Pending means not established in this record, not permission
to guess or silently substitute information.

| ID | Question | Current status |
| --- | --- | --- |
| DATA-01 | File, acquisition and dataset counts per configuration? | Private inventory pending |
| DATA-02 | Raw variables, complex representation and every dimension meaning? | Extractor/metadata documentation needed |
| DATA-03 | Export format, scaling, centering and channel conventions? | Input contract pending |
| DATA-04 | 3D CS file format, sampling geometry and actual mask? | Not established |
| DATA-05 | Meaning of acceleration 8; actual count of 10 volumes? | Reported/expected only |
| DATA-06 | Meaning and units of "200"? | Unresolved |
| EXTRACT-01 | Exact extractor name/version and invocation? | Python and "GE recon code" reported |
| EXTRACT-02 | Python/libraries, OS/architecture requirements? | Unknown; do not reuse the synthetic environment by assumption |
| EXTRACT-03 | Supported configurations and exported metadata? | Unknown |
| AUTH-01 | Documented permitted uses and processing/storage locations? | Confirm before each experimental dataset |
| AUTH-02 | TrueNAS retention and student-copy deletion terms? | Confirm with laboratory supervisor/steward |
| AUTH-03 | Which summaries/outputs may be shared? | Do not infer permission |
| ENV-01 | Full BART commit and actual Makefile.local? | Only v1.0.00/short 37f3c5f and selected flags observed |
| ENV-02 | TALC environment and resource configuration? | Separate record pending |
| VERIFY-01 | Pilot-justified numerical tolerance and action-count rule? | Human approval before main evaluation |
| VERIFY-02 | Negative tests and clean-checkout reproduction? | Not performed in this starter |
| GIT-01 | Intended course repository? | Identified: `git@github.com:rictr161/ensf620-bart-workflow.git`; reported empty before initial publication; SSH authenticated as `rictr161` |
| GIT-02 | Commit identity and reviewer access? | Pending; no credentials in files |

Pause affected experimental work if authority is unclear; continue with synthetic
inputs. Missing acquisition information blocks recipes depending on it, not all
learning. Unresolved numerical discrepancies block promotion to evaluation.
Record exclusions and reasons at the November 6 gate.
