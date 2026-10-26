# Project Context and Method

Current context consolidated from the reviewed project documents and Ricardo's
author-confirmed updates. See `sources.md` for source identification. These
clarifications describe current project context; they do not amend the submitted
proposal or constitute new instructor approval.

## Committed scope

The contribution is a Python workflow with a simpler interface for configuring,
validating, executing and recording reviewed BART procedures. It is not a new
reconstruction algorithm or an automatic parameter optimizer. Optional Bash/HPC
launchers may invoke the Python workflow later; Bash is not the current primary
architecture.

The current implementation scope is Cartesian 2D and 3D reconstruction, including
compressed sensing. Radial and 4D are outside the current implementation scope.
The minimum target remains one verified 3D Cartesian manual–automated pair, with the
main evaluation capped at the three datasets identified in the proposal. Intended
support, reported dataset availability, validated recipes and implemented
functionality are separate states; not every supported configuration must enter
the main evaluation.

Current experimental inputs are author-reported as BART `.cfl`/`.hdr` files for
brain MRI 3D Cartesian reconstruction, including CS work. This report does not
establish that the files were inspected or that their reconstruction is validated.
Dimension meanings, sampling, calibration and recipe-specific settings remain
explicitly unresolved until reviewed evidence exists. Earlier `.h5`, extractor,
and GE-conversion questions remain historical context or upstream provenance;
they are not current implementation blockers. Do not transfer the earlier
Poisson/R=8/10-volumes/“200” description to these datasets without established
correspondence.

Development and testing will use BART-generated synthetic phantoms with matched
inputs and settings for manual and automated procedures. Fixtures, settings,
tests and acceptance criteria remain to be defined and verified. The proposal's
three repeated runs per mode and dataset are planning targets, not completed
measurements.

## Comparison boundary

Both modes start from the same reviewed BART-format inputs and required metadata
and finish with verified, organized outputs and a reviewed record. Scanner
extraction and `.h5` conversion are outside the workflow implementation boundary.
Input preparation, configuration changes, initiation and final review remain inside
the measured task. Human initiation is retained.

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

DICOM images are a proposed complementary reconstruction reference, not approved
ground truth or a validation protocol. Do not assume fully sampled acquisition or
select DICOM metrics or tolerances before a separate review.

## Current implementation

The observed work is a fully sampled synthetic 64 × 64 example, a NumPy inverse
comparison and figures. It is not the verified experimental 3D manual baseline,
automated counterpart, operational action reduction or HPC evaluation. `src/` and
experimental `configs/` are not implemented yet. The initial main-branch push at
commit `aad0525` is author-supplied evidence; it does not establish publication
of the current working branch, clean-checkout reproduction, experimental
validation or contract-control implementation.

## Dates

The first milestone was planned for October 9. The independent report is dated
2026-10-23T04:32:32.860963+00:00. Keep planned and actual dates distinct. Consult the
imported `results/familiarization-2d-20261023/started-utc.txt` rather than inferring
exact start time from a folder label.
Use real commit dates; do not manufacture retrospective development history.
