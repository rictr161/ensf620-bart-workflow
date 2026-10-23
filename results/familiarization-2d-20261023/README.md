# Observed Synthetic Familiarization Evidence

This summary transcribes Ricardo's supplied outputs and copies his five uploaded
PNGs. It is not an assistant-run numerical experiment. The original complex arrays,
local scripts and complete run directory were not available in the assistant's
workspace when this starter was prepared.

## Provenance

Original run label: `synthetic-2d-20261021-212148`.  
Independent-check directory: `numpy-check-20261023T043232860963Z`.  
Reported comparison UTC: `2026-10-23T04:32:32.860963+00:00`.  
Plot directory label: `figures-20261023T053046251432Z`.  
Note consolidation: 2026-10-23.

The imported `comparison.txt`, `nrmse.txt`, `started-utc.txt` and `plot-info.txt`
now appear in this directory's staged listing. The two scripts are included in
`scripts/`. The list establishes file presence, not independent byte equality
against every original. Do not reconstruct or overwrite historical logs from a
summary; preserve the original run separately.

| Comparison | Relative L2 error | Denominator |
| --- | ---: | --- |
| BART vs reference | 1.442448308e-07 | Norm of reference |
| NumPy vs reference | 9.412963986e-08 | Norm of reference |
| BART vs NumPy | 1.029663011e-07 | Norm of NumPy reconstruction |

Shape (64, 64); axes (0, 1); centered/unitary. Disk: complex64; NumPy calculation
and comparison: complex128. Python 3.13.17, NumPy 2.5.4. No numerical acceptance
threshold was applied. These are not performance or operator-action measurements.

## Supplied figures

| Figure | Content |
| --- | --- |
| [01_reference.png](figures/01_reference.png) | Reference magnitude |
| [02_kspace.png](figures/02_kspace.png) | Centered k-space, ln(1 + magnitude) |
| [03_bart.png](figures/03_bart.png) | BART reconstruction magnitude |
| [04_numpy.png](figures/04_numpy.png) | NumPy reconstruction magnitude |
| [05_residual.png](figures/05_residual.png) | Absolute complex difference: NumPy minus reference |

Three image magnitudes share the 0–1 range. K-space and residual have separate
scales. The residual scale uses 1e-7, so visible structure is not a large-error
claim. Array axis 0 is displayed horizontally; no anatomical orientation is assigned.

The plotting report identifies Matplotlib 3.11.2 and says it loaded existing arrays
without reconstructing again. This does not negate the prior reconstruction.

`reported-metrics.csv` is a transcription, not a parsed original log.
`uploaded-figures-sha256.txt` hashes the supplied PNG copies, not the Mac's originals,
laboratory inputs or complex arrays. Byte equality against the Mac is unverified.

Imports are now listed. At this pre-publication checkpoint, author review and the
first project commit remain to be completed. Clean-checkout reproduction and formal
evaluation criteria remain pending. Preserve historical results and record
subsequent reruns separately.
