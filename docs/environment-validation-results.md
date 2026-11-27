# Environment Validation Results

## Evidence basis and reporting

This record consolidates Ricardo's report of workflow use with acquired BART
inputs. No laboratory files were inspected for this record. It distinguishes
configuration shown in the shared ARC script, records available in the
repository, and owner-reported execution and review. A script configuration is
not, by itself, evidence that every value was used effectively by a completed
job.

The local runs and ARC run are operational evidence for the reported cases.
They do not establish scientific or clinical acceptance, equivalence between
Mac and ARC outputs, or support for every possible BART input.

## Local acquired-data runs

Ricardo reports that he ran the reconstruction workflow on his Mac using
laboratory inputs in BART format. He also reports using it from a new, separate
local Python environment at
`/Users/ricardoaguilar/bart-learning/bart-clean-simple-01`. This was a clean
Python environment separated from the original development environment; it was
not a fresh operating-system installation or a new BART build. The BART
executable was the existing
`/Users/ricardoaguilar/software/bart-1.0.00/bart`.

No local execution logs, exit codes, resource measurements, or paired-output
comparison for these acquired-data runs are included in the repository evidence
available for this consolidation. The execution is therefore attributed to
Ricardo's report, not represented as independently verified from run records.

## ARC Slurm run

Ricardo reports preparing the environment, transferring the code and input to
ARC, submitting a Slurm job, and successfully running the workflow without
graphical windows. This is owner-reported success; no numeric job or stage
status is available. The working directory stated in the shared script was
`/home/ricardo.aguilartrejo/bart-arc-test`. The script referenced
`repository/src/bart_workflow.py`, `.venv/bin/python`, the declared modules
`python/3.12.5` and `bart/1.0.00`, the input base path
`inputs/KSpace_CS_3_R8_Pass1/kspace_pass9_cc8`, and the planned output
directory `results/pass9-cs-01`.

The table below reproduces the **configuration shown in the shared script**.
It is not a transcription of job logs or proof that each value was effective
in the completed run.

| Component | Configuration shown in the script |
|---|---|
| Dimensionality | 3D |
| Compressed-sensing reconstruction | Enabled |
| Sampling information | `--sampling-source bart-pattern` |
| Sensitivities | `--sensitivity-source ecalib` |
| Calibration region | `128:16:16` |
| Calibration kernel | `6:6:6` |
| Calibration threshold | `0.001` |
| Calibration crop | `0.8` |
| ESPIRiT map sets | `1` |
| Requested PICS algorithm | FISTA |
| Wavelet | `dau2` |
| Regularization weight | `0.01` |
| Iterations | `100` |
| Step | `0.95` |
| Random-shift disabling | Enabled |
| Data scaling | `1.0` |
| Figures during the job | Not requested |

No Slurm job identifier, execution log, numeric exit code, elapsed time,
measured memory use, effective ARC software version, or Git revision for this
run is recorded here. In particular, a proposed reduction of requested memory
from `16G` to `8G` is not evidence of the final memory request or actual memory
consumption.

## Download and local visual review

Ricardo reports downloading only `reconstruction.hdr` and `reconstruction.cfl`
from the ARC transfer server to
`/Users/ricardoaguilar/bart-learning/arc-results/pass9-cs-01`. He then opened
the reconstruction with the local
[`view_bart_slices.py`](../src/view_bart_slices.py) viewer. Ricardo's final
confirmation was **“listo todo perfecto”**, referring to the download and
visual review. This is recorded as an owner-reported successful retrieval and
review, not as a separate log-backed or scientific-quality acceptance result.

The viewer is a local inspection utility for an existing scalar BART
reconstruction. Its current behavior and input limits are documented in the
[automated workflow guide](tutorials/automated-cartesian-workflow.md#optional-interactive-slice-viewer).

## Limits and work outside this delivery

This evidence does not establish:

- Binary identity or numerical equivalence between Mac and ARC reconstructions.
- Processing of the full laboratory dataset, multiple ESPIRiT map sets, 2D CS,
  or non-Cartesian trajectories.
- General validation of arbitrary acquired inputs.
- Scientific or clinical acceptance of image quality.
- ARC time savings or measured memory use.
- A comparison against a fully sampled ground truth for the undersampled
  acquisitions. No such reference is established or required to close these
  operational checks.

The reported use is limited to local acquired-input use and one ARC volume described
above. Batch processing, additional datasets and calibration/map-set variants,
2D CS, and non-Cartesian trajectories remain outside this delivery.

## Relationship to the PRD

The local and ARC reports establish owner-reported use of the current
non-interactive workflow with particular acquired BART inputs, not general
compatibility. The shared script documents requested options, but without job
records it does not verify effective settings, per-stage outcomes, output
checks, or the workflow's run-record behavior under FR-30 and FR-32. The
reported Slurm use is non-graphical, but does not expand the workflow's
supported routes or interface requirements (FR-23, FR-25, FR-26, and FR-39).
The synthetic preparation and comparison obligations (FR-22 and FR-33 through
FR-37) remain evidenced by their records in Blocks 7–9; the acquired-data
report does not replace those comparisons or the operator-intervention
evidence.
