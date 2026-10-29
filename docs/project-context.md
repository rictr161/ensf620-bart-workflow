# Project Context and Evaluation Planning

This document summarizes the project's technical direction, reported input
context and planned evaluation. Its basis is the reviewed project documentation
and Ricardo's updates, identified in [Sources and evidence basis](sources.md).
The summary does not amend the submitted proposal or record new instructor
approval. Detailed software requirements and the evaluation protocol remain to
be developed and reviewed.

The accepted [AI data-access and action contract](DATA_CONTRACT.md) governs
assistant access and authority. The project and evaluation planning below have
a separate purpose from that policy.

## Project purpose and technical direction

The intended contribution is a Python workflow with a simpler interface for
configuring, validating, executing and recording reviewed BART procedures.
Python is the chosen primary implementation language. The workflow will organize
existing reconstruction procedures; a new reconstruction algorithm or automatic
parameter optimizer is outside its scope. Optional Bash/HPC launchers may invoke
the Python workflow later.

The current technical scope is Cartesian 2D and 3D reconstruction, including
compressed sensing. Radial and 4D reconstruction, changes to BART algorithms,
scanner extraction and `.h5` conversion are outside the current implementation
scope. Intended support, reported input availability, verified recipes and
implemented functionality are distinct states.

## Inputs and development basis

Ricardo reports that the current experimental inputs are brain MRI 3D Cartesian
BART `.cfl`/`.hdr` files, including CS work. The
[input inventory](input-inventory.md) records that report and its historical
context. Availability does not establish inspection or a validated reconstruction.
The shared record does not yet establish dimension meanings, sampling,
calibration or recipe-specific settings for a verified experimental procedure.

Earlier `.h5`, extractor and GE-conversion questions concern upstream provenance
and historical context. They are outside the current implementation work.
Correspondence between the earlier Poisson/R=8/10-volumes/"200" description and
the current brain datasets has not been established.

BART-generated synthetic phantoms are the confirmed development and testing
route. The planned manual and automated procedures will use matched inputs and
settings. Fixtures, reconstruction settings, tests and acceptance criteria for
that comparison remain to be defined and verified. Experimental inputs remain
outside the shared repository and AI context.

## Evaluation planning and comparison principles

### Recorded planning basis

The proposal and instructor feedback summarized in [sources](sources.md)
prioritize one verified 3D Cartesian manual–automated pair, with the main
evaluation capped at the three datasets identified in the proposal. The proposal
also describes three repeated runs per mode and dataset. These quantities are recorded evaluation
planning, not implemented software limits, AI-access rules or completed
measurements. The detailed reconstruction procedures, counting rules and
numerical acceptance criteria still require review.

### Boundary of the planned comparison

Both modes are planned to start from the same reviewed BART-format inputs and
required metadata, and finish with verified, organized outputs and a reviewed
run record. Input preparation, configuration changes, human initiation and final
review are included in the intended measured task. Scanner extraction and `.h5`
conversion are outside the workflow implementation boundary.

### Planned outcomes and measurement conditions

Operator intervention is the primary planned outcome, expressed as action counts
and paired absolute and percentage changes. The action-counting checklist and
its granularity remain to be established during pilots and fixed before the main
evaluation. The planned counts concern operator actions, with individual
keystrokes and software-only operations outside the count. Failures and recovery
will be reported separately. Learning, setup and one-time development are outside
the planned operational measurements.

The planned comparisons use matched inputs, reconstruction settings, stopping
criteria, software and resource configurations. Manual execution on the Mac
compared with automation on TALC would combine platform and workflow differences,
so that comparison would not isolate an automation effect. Runtime and memory
are secondary outcomes; queue waiting time will be recorded separately.

### Planned numerical verification

The planned numerical review compares output dimensions, numerical
representation and scaling. Pilot work is intended to justify tolerances before
the main evaluation; the tolerances are then fixed rather than adjusted in
response to a failed comparison. The actual numerical criteria have not yet been
approved. Agreement between outputs alone does not establish correctness;
independent or known-answer checks remain part of the verification approach.

DICOM images remain a proposed complementary reconstruction reference. They are
not approved ground truth, and no DICOM validation protocol, metrics or tolerances
have been approved. Fully sampled acquisition for that proposed comparison is
not established by the available context.

## Existing evidence and remaining work

The recorded exercise is fully sampled, single-channel, synthetic 2D data at
64 × 64, with a NumPy inverse comparison on BART-generated k-space and supplied
figures. No numerical acceptance threshold was applied. The
[results record](../results/familiarization-2d-20261023/README.md) describes the
available measurements and their provenance.

The automated workflow in `src/`, verified experimental configurations in
`configs/`, a verified experimental 3D manual baseline, measured operator-action
reduction, clean-checkout reproduction and HPC evaluation remain pending.
The [README status summary](../README.md#current-status) provides the repository's
overview of available evidence and remaining work.

## Documentation and evidence dates

The planned milestone and supplied timestamps represent different records:

| Record | Date or timestamp | Meaning |
| --- | --- | --- |
| Original first milestone | October 9, 2026 | Planned milestone date |
| [Synthetic start record](../results/familiarization-2d-20261023/started-utc.txt) | `2026-10-22T03:22:43Z` | Timestamp contained in the supplied start file |
| [NumPy comparison report](../results/familiarization-2d-20261023/comparison.txt) | `2026-10-23T04:32:32.860963+00:00` | Timestamp recorded in the comparison report |

These records do not establish completion by the original milestone or the time
of every activity. The directory label is not an independent timing record.
Git commit dates describe repository history, including the later incorporation
of work performed before the project's first commit.
