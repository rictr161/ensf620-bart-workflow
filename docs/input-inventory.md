# Input Inventory — Shareable Summary

Consolidated from Ricardo's reports, not inspection of laboratory files.
Detailed identifiers, private paths and steward records remain in approved storage.

The current experimental input boundary is author-reported BART `.cfl`/`.hdr` data.
The current brain MRI data are described as 3D Cartesian, including CS work. File
availability is not file inspection, recipe validation, or reconstruction evidence.

| Configuration | Historical report | Current reported input stage | Current extension | Readiness |
| --- | --- | --- | --- | --- |
| 2D Cartesian | Yes | Original scanner files | `.h5` (historical) | Not verified |
| 3D Cartesian | Yes | BART-format reconstruction input reported | `.cfl`/`.hdr` | Not verified |
| 3D CS | Yes, historical report | BART-format reconstruction input reported | `.cfl`/`.hdr` | Not verified |

These are configuration categories, not independently established dataset or file
counts. A previous "No" for 3D CS was corrected by Ricardo as a reporting error,
not a new receipt/availability change. Individual receipt dates remain unrecorded.

## Historical 3D CS description

The following details belong to an earlier report and must not be assigned to the
current brain datasets without established correspondence.

| Field | Reported information | Status |
| --- | --- | --- |
| Sampling | "Poisson distributed" | Geometry/mask not verified |
| Acceleration | Factor 8 | Definition/actual sampling not verified |
| Volumes | "Should be 10 volumes" | Expected count only |
| Additional quantity | "200" | Meaning and units unknown |
| Format | Not supplied | Do not infer `.h5` from other configurations |

Do not interpret "200" as matrix size, slices or another quantity. The short label
does not establish axis meanings, trajectory, mask or a reconstruction recipe.

## Historical extraction context

Ricardo previously reported Python code described as "GE recon code" for 3D
Cartesian data. Extraction, `.h5` conversion and installation/debugging of that
utility are outside the current workflow implementation boundary. Preserve the
historical provenance questions, but they are not current implementation blockers.
Do not guess a particular GE product or transfer its metadata to the current data.

## Provenance and authority

The proposal describes non-human spherical-phantom GRE measurements provided through
a supervisor-arranged laboratory collaboration, with access beginning September 23,
2026. This proposal-stage access date does not establish each file's receipt or
permission for every intended use. The supervisor has been involved, but the
permitted-use record and retention terms need explicit documentation.

Privately record source/steward, identifier/version, receipt date, completeness,
permitted uses and locations, retention and sharing rules for each included dataset.
Non-human measurements are not automatically publicly redistributable.

The proposal listed 4D Cartesian, 4D CS, 2D radial and 3D radial as pending. They
remain outside the current implementation scope; their historical status is not a
claim about future availability.
