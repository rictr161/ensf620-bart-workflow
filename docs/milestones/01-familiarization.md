# Milestone 01 — Familiarization and Input Inventory

Planned date: 2026-10-09.  
Documentation consolidated: 2026-10-23.  
Status at assembly checkpoint: practical work observed; scripts/reports imported; author review and initial publication in progress.

## Commitment

Run and document a small synthetic BART example, record the local software
environment, inventory received datasets, and identify unresolved format,
acquisition-metadata and data-use questions before experimental processing.

| Component | Evidence | Remaining work |
| --- | --- | --- |
| BART example | 64 × 64 phantom, Fourier/inverse and NRMSE; scripts/text records imported | Review reproduction from the repository |
| Independent Fourier check | NumPy inverse and three relative errors | No threshold applied; broader verification pending |
| Visualization | Five synthetic PNGs; plot and dependency records imported | Reproduce from recorded code |
| Local environment | Mac M5/24 GB, BART output and Python snapshots included | Full BART commit and actual build configuration pending |
| Inventory | Three configurations reported received | Dataset-level identifiers/counts and required metadata open |
| Questions | `docs/open-questions.md` | Confirm before affected experimental processing |
| Repository | English notes and imports staged; SSH account/destination identified | Author review, initial publication and clean-checkout test |

## Evidence dates

Original run label: `synthetic-2d-20261021-212148`.  
Independent comparison UTC: `2026-10-23T04:32:32.860963+00:00`.  
Plot directory UTC label: `20261023T053046251432Z`.  
Exact initial execution timestamp: see the imported `started-utc.txt` in
`results/familiarization-2d-20261023/`; do not infer it from the run-folder name.
SSH authentication has been demonstrated. Actual project commit/publication evidence
must come from Git history and returned Git output; this checkpoint precedes them.

Do not present this work as demonstrated by October 9. It is familiarization, not
the operational manual–automated experiment.

## Completion review

Confirm that imported evidence matches the notes and sharing boundaries. Unknowns
can remain explicitly recorded in an inventory; they must not be replaced with
guesses or a claim that experimental inputs are ready. Human documentation review
and clean-checkout reproduction are still pending. The independent check was
exercised, not passed under a previously fixed numerical acceptance threshold.
