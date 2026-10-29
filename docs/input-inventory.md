# Input Inventory — Shareable Summary

This inventory summarizes Ricardo's reports of experimental input availability,
earlier acquisition descriptions and unresolved correspondence between those
reports. No laboratory files were inspected for this summary. Detailed private
identifiers, storage paths and steward records are not included here.

The [project context](project-context.md) describes the development scope and
synthetic-phantom approach. The [README input requirements](../README.md#input-requirements)
describe the files used by the existing synthetic example.

## Current reported experimental inputs

Ricardo describes the current experimental inputs as brain MRI 3D Cartesian
BART `.cfl`/`.hdr` files, including CS work. The verification column below records
what is established in the shared project documentation.

| Reported configuration | Reported input stage and format | Reconstruction verification |
| --- | --- | --- |
| 3D Cartesian | BART-format reconstruction inputs, `.cfl`/`.hdr` | Not established in the shared record |
| 3D CS | BART-format reconstruction inputs, `.cfl`/`.hdr` | Not established in the shared record |

The rows describe configuration categories. They do not establish a count of
distinct datasets, acquisitions or files. Reported availability does not establish
file inspection, completeness, a verified recipe or reconstruction evidence.

## Historical availability reports

Earlier reports described receipt of 2D Cartesian, 3D Cartesian and 3D CS material.
The earlier 2D Cartesian input stage was original scanner files in `.h5` format.
Its current format, conversion status and availability as a reconstruction-ready
input are not established by that historical description.

A temporary "No" for 3D CS was corrected by Ricardo to "Yes" as a reporting error.
The correction did not represent a new receipt or a change in availability.
Individual receipt dates remain unrecorded in this summary.

The proposal listed 4D Cartesian, 4D CS, 2D radial and 3D radial as pending. Those
categories remain outside the current implementation scope. Their proposal-stage
status does not establish present or future availability.

## Earlier 3D CS description

The following details come from an earlier report. Their correspondence with the
current brain datasets has not been established.

| Field | Earlier reported information | Status of that report |
| --- | --- | --- |
| Sampling | "Poisson distributed" | Geometry and mask not verified |
| Acceleration | Factor 8 | Definition and actual sampling not verified |
| Volumes | "Should be 10 volumes" | Expected count, not an established count |
| Additional quantity | "200" | Meaning and units unknown |
| Format | Not supplied | No format established by that earlier report |

The description does not establish axis meanings, trajectory, mask or a
reconstruction recipe. The current `.cfl`/`.hdr` report does not fill in the
missing format of that earlier record.

## Historical extraction context

Ricardo previously reported Python code described as "GE recon code" for 3D
Cartesian data. That description does not identify a particular GE product or
establish the utility's metadata relationship to the current inputs.

Extraction, `.h5` conversion and installation or debugging of that utility are
outside the current workflow implementation scope. Outstanding provenance
questions remain historical or upstream context, rather than current
implementation blockers.

## Provenance and permitted-use record

The proposal describes non-human spherical-phantom GRE measurements provided
through a supervisor-arranged laboratory collaboration, with access beginning
September 23, 2026. The project documents are identified in [sources](sources.md).
Correspondence between that proposal-stage description and the current brain MRI
input report is not established in this summary.

The September access date does not establish each file's receipt date or
permission for every intended use. Supervisor involvement is recorded, while
confirmation of permitted-use and retention terms remains pending in the shared
project record. The non-human description does not establish permission for
public redistribution.

The provenance and handling information identified for private records includes
source/steward, identifier/version, receipt date, completeness, permitted uses and
locations, retention and sharing rules for each included dataset. Those private
values and the completeness of the records are not established by this summary.

AI access and action boundaries are defined by the
[accepted contract](DATA_CONTRACT.md). Outstanding decisions on permitted uses,
destinations, sharing and retention are recorded in the
[contract decision register](DATA_CONTRACT_DECISIONS.md).
