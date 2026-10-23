# Project Context and Method

Consolidated 2026-10-23 from the proposal, feedback and Ricardo's implementation
updates. See `sources.md` for source identification.

## Committed scope

The contribution is configuration, input validation, BART execution, provenance and
comparison, not a new reconstruction algorithm or automatic parameter optimization.
The instructor recommends one verified 3D Cartesian manual–automated pair and a
main evaluation capped at the three datasets already received. Current receipt
reports establish configurations, not an inspected count of usable datasets.

The proposed seven configurations are 2D/3D/4D Cartesian, 3D/4D CS, and 2D/3D radial.
Later configurations are optional and must meet the November 6, 2026 gate for
inputs, authority, reconstruction recipe and checks. Do not guess missing metadata.
The proposal targets three repeated runs per mode and dataset; these are planned,
not already measured.

## Comparison boundary

Both modes start from the same exported k-space and required metadata and finish
with verified, organized outputs and a reviewed record. GE extraction is upstream
and outside the comparison. Input preparation, configuration changes, initiation
and final review remain inside the measured task. Human initiation is retained.

## Outcomes and verification

Operator-action counts and paired absolute/percentage changes are primary.
Establish the checklist granularity during pilots and freeze it before evaluation.
Do not count individual keystrokes or software-only operations. Report failures
and recovery separately. Keep learning, setup and one-time development separate.

Match inputs, reconstruction settings, stopping criteria, software and resource
configuration for each pair. Do not compare manual execution on the Mac against
automation on TALC as an automation effect. Runtime and memory are secondary;
queue waiting time is recorded separately.

Match output dimensions, numerical representation and scaling. Justify tolerances
in pilots before the main evaluation; do not relax them just to pass. Agreement
alone does not establish correctness. Preserve independent/known-answer checks.

## Current implementation

The observed work is a fully sampled synthetic 64 × 64 example, a NumPy inverse
comparison and figures. It is not the verified experimental 3D manual baseline,
automated counterpart, operational action reduction or HPC evaluation. `src/` and
experimental `configs/` are not implemented yet.

## Dates

The first milestone was planned for October 9. The independent report is dated
2026-10-23T04:32:32.860963+00:00. Keep planned and actual dates distinct. Consult the
imported `results/familiarization-2d-20261023/started-utc.txt` rather than inferring
exact start time from a folder label.
Use real commit dates; do not manufacture retrospective development history.
