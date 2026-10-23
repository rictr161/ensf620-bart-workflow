# Input Inventory — Shareable Summary

Consolidated: 2026-10-23. Source: Ricardo's reports, not inspection of laboratory files.
Detailed identifiers, private paths and steward records remain in approved storage.

| Configuration | Received | Reported input stage | Extension | Readiness |
| --- | --- | --- | --- | --- |
| 2D Cartesian | Yes | Original scanner files | `.h5` | Not verified |
| 3D Cartesian | Yes | Original scanner files | `.h5` | Not verified |
| 3D CS | Yes | Not confirmed | Not confirmed | Not verified |

These are configuration categories, not independently established dataset or file
counts. A previous "No" for 3D CS was corrected by Ricardo as a reporting error,
not a new receipt/availability change. Individual receipt dates remain unrecorded.

## 3D CS description supplied by Ricardo

| Field | Reported information | Status |
| --- | --- | --- |
| Sampling | "Poisson distributed" | Geometry/mask not verified |
| Acceleration | Factor 8 | Definition/actual sampling not verified |
| Volumes | "Should be 10 volumes" | Expected count only |
| Additional quantity | "200" | Meaning and units unknown |
| Format | Not supplied | Do not infer `.h5` from other configurations |

Do not interpret "200" as matrix size, slices or another quantity. The short label
does not establish axis meanings, trajectory, mask or a reconstruction recipe.

## Extraction

Ricardo received code for the 3D Cartesian data, described as "GE recon code", used
with Python. Exact name/version, requirements, invocation, outputs and compatibility
with macOS/arm64 or Python 3.13.17 remain pending. Do not guess a particular GE
product. Applicability to the other configurations is also unconfirmed.

## Provenance and authority

The proposal describes non-human spherical-phantom GRE measurements provided through
a supervisor-arranged laboratory collaboration, with access beginning September 23,
2026. This proposal-stage access date does not establish each file's receipt or
permission for every intended use. The supervisor has been involved, but the
permitted-use record and retention terms need explicit documentation.

Privately record source/steward, identifier/version, receipt date, completeness,
permitted uses and locations, retention and sharing rules for each included dataset.
Non-human measurements are not automatically publicly redistributable.

The proposal listed 4D Cartesian, 4D CS, 2D radial and 3D radial as pending. Their
current status has not been reconfirmed in this inventory.
