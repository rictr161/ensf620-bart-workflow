# ENSF 620 — BART Reconstruction Workflow

Author: Ricardo Andrés Aguilar Trejo  

## Project overview

This ENSF 620 project investigates whether an automated workflow can reduce manual
intervention in MRI reconstruction while maintaining numerical equivalence with
verified reference reconstructions. Python is the primary implementation language
for configuring, validating, executing and recording reviewed BART procedures.

The technical scope is **Cartesian 2D and 3D reconstruction, including compressed
sensing (CS)**. The workflow will organize existing BART commands. Changes to BART's
reconstruction algorithms, radial and 4D reconstruction, scanner extraction and
`.h5` conversion are outside the current implementation scope.

Development and testing will use **BART-generated synthetic phantoms**. Current
experimental inputs are reported as brain MRI 3D Cartesian BART `.cfl`/`.hdr`
files, including CS work. These private inputs remain outside the shared
repository. The [input inventory](docs/input-inventory.md) distinguishes reported
availability from verified reconstruction readiness.

Operator intervention is the primary evaluation outcome; runtime and memory are
secondary outcomes in the planned HPC evaluation. The
[project context](docs/project-context.md) records the instructor's recommendations
and evaluation planning.

## Current status

### Available evidence

Ricardo executed a fully sampled **64 × 64, single-channel, 2D** synthetic example
on his Mac. BART generated the image and k-space and reconstructed the image.
A separate NumPy implementation reconstructed the same k-space. The repository
contains the Python checker and visualization scripts, text reports and five
figures. The reported exploratory measurements are:

| Comparison | Reported relative L2 error |
| --- | ---: |
| BART vs reference | 1.442448308e-07 |
| NumPy vs reference | 9.412963986e-08 |
| BART vs NumPy | 1.029663011e-07 |

**No numerical acceptance threshold was applied.** This is not yet the evaluated
manual–automated comparison, an experimental 3D baseline, a performance benchmark,
or validation of all BART functionality.

The [synthetic procedure](tests/synthetic_2d/README.md) describes the exercise and
its proposed reproduction route. The
[results record](results/familiarization-2d-20261023/README.md) documents the
measurements, figures and provenance. The recorded local platform is a MacBook Pro
with Apple M5 and 24 GB memory; software details are in the
[macOS environment record](environment/local-macos.md).

### Work still pending

- The automated Python workflow in `src/` and verified experimental reconstruction
  configurations in `configs/`.
- A verified 3D Cartesian manual reference procedure and its automated counterpart.
- Additional synthetic fixtures, a formal regression suite, and approved numerical
  tolerances and operator-action counting rules.
- Reproduction from this repository and a clean checkout, a separate TALC
  environment record, and HPC evaluation.

DICOM comparison remains a proposed complementary reference without an approved
validation protocol.

### Accepted access policy

Ricardo has accepted the
[AI data-access and action contract](docs/DATA_CONTRACT.md), **version 0.3.0**.
It defines access and authority for supervised AI-assisted development; it does not
define the software specification or evaluation protocol. Acceptance and remaining
boundary decisions are recorded in the
[contract decision register](docs/DATA_CONTRACT_DECISIONS.md). Technical enforcement
is not established or verified by the contract.

## Installation and environment

The setup information currently covers the recorded synthetic 2D exercise on
macOS with Apple Silicon. A fresh installation based on these records and
reproduction from a clean checkout have not yet been verified.

### Recorded software

| Component | Recorded version | Role in the existing example |
| --- | --- | --- |
| BART | v1.0.00 | Synthetic image generation, Fourier transforms and NRMSE calculation |
| Python | 3.13.17 | Execution of the checker and visualization scripts |
| NumPy | 2.5.4 | Array handling and the independent inverse Fourier calculation |
| Matplotlib | 3.11.2 | Figure generation |

These versions describe the environment used for the recorded exercise. The
[macOS environment record](environment/local-macos.md) includes the hardware,
compiler, libraries and observed BART build flags.

### Activate the existing local environment

The recorded setup keeps BART at `~/software/bart-1.0.00` and the Python virtual
environment at `~/bart-learning/.venv`, both outside this repository. These are
Ricardo's existing installation locations; a different installation may use
different paths.

For that existing setup, activate the environment in the current terminal session:

```bash
source "$HOME/bart-learning/.venv/bin/activate"
export BART_TOOLBOX_PATH="$HOME/software/bart-1.0.00"
export PATH="$BART_TOOLBOX_PATH:$PATH"
```

Check which BART executable the session resolves and the version it reports:

```bash
command -v bart
bart version
```

Activation applies to the current terminal session. The
[synthetic procedure](tests/synthetic_2d/README.md) describes the proposed steps for
running the exercise with this environment.

### Dependency and installation records

- [Core requirements](environment/requirements-core.txt) record the direct NumPy
  dependency used by the checker.
- [Visualization requirements](environment/requirements-visualization.txt) include
  the core requirements and add Matplotlib.
- The [verification snapshot](environment/python-requirements-verification.txt)
  and [visualization snapshot](environment/python-requirements-visualization.txt)
  preserve package-version records from the environments used.

The direct requirement files are not complete environment locks. The
[BART installation record](environment/bart-installation.md) describes the guided
preparation and available build evidence, but does not contain the complete
`Makefile.local` or full build log. A complete fresh-installation procedure and a
separate TALC environment record remain pending.

## Input requirements

### Current synthetic example

The included Fourier comparison uses **fully sampled, single-channel, 64 × 64
synthetic data**, with trailing singleton dimensions. At the NumPy comparison
stage, the following BART file pairs must be present in the synthetic run directory:

| Required files | Contents | Produced by |
| --- | --- | --- |
| `reference.hdr` and `reference.cfl` | Synthetic reference image | BART phantom generation |
| `kspace.hdr` and `kspace.cfl` | Fully sampled k-space for that reference | BART forward Fourier transform |
| `reconstruction.hdr` and `reconstruction.cfl` | BART reconstruction used in the comparison | BART inverse Fourier transform |

Each `.hdr` file describes the array dimensions, and its matching `.cfl` file
contains the complex array. These arrays are generated locally using the
[synthetic procedure](tests/synthetic_2d/README.md); they are not included in the
repository.

Both Python scripts look for these exact file names in the **current working
directory**. Run them from the synthetic run directory, using the paths to the
scripts in this repository. Keep each new exercise in a separate run directory
to preserve previous results.

The existing reader is limited to this documented 64 × 64 case. Array storage and
Fourier conventions are described in the synthetic procedure; general input
handling has not yet been implemented.

### Additional input for visualization

The visualization script also needs `reconstruction_numpy.npy`, which is produced
by `check_fourier_numpy.py` inside a new `numpy-check-<timestamp>` directory.
Pass that directory as the argument to `visualize_synthetic.py`, using the actual
directory name printed by the checker.

The three BART file pairs must still be available in the current working directory.
Use the NumPy result from the same exercise as those BART files.

### Planned automated workflow

The input interface, required metadata and validation rules for the planned
Cartesian 2D/3D workflow, including CS, remain to be defined. The requirements
above describe only the existing synthetic example. The
[input inventory](docs/input-inventory.md) separately records reported experimental
input availability and unresolved information.

## Manual baseline

A verified 3D Cartesian manual reference procedure for the planned manual–automated
comparison remains pending. The currently documented manual example is the
exploratory 2D synthetic Fourier exercise described below.

### Existing synthetic example

The [complete synthetic procedure](tests/synthetic_2d/README.md) explains environment
activation, creation of a new run directory, and recording of the date and BART
build. After that preparation, run the following commands one at a time inside the
newly created synthetic run directory. Stop at the first error and preserve previous
run directories.

```bash
bart phantom -x 64 reference
bart fft -u 3 reference kspace
bart fft -i -u 3 kspace reconstruction
bart nrmse -S reference reconstruction > nrmse.txt
```

These commands generate the three BART file pairs listed under
[Input requirements](#input-requirements) and save BART's reported NRMSE in
`nrmse.txt`. In the FFT commands, the bitmask `3` selects array axes 0 and 1 for
the 2D transform.

The complete procedure also describes the independent NumPy inverse comparison
on the same synthetic k-space and the subsequent figure generation. The original
exercise had no predefined numerical acceptance threshold; reproduction from this
repository or a clean checkout has not yet been verified.

## Automated execution

The automated Python/BART workflow is **not implemented yet**. The
[source notes](src/README.md) describe the planned role of `src/`; the
[configuration notes](configs/README.md) record that no experimental reconstruction
configuration has been verified.

The existing [Python scripts](scripts/README.md) provide the NumPy comparison and
figure generation for the [documented synthetic example](#manual-baseline).
BART data generation and reconstruction are currently invoked manually in that
procedure.

The workflow's execution interface and configuration format remain to be defined.
Instructions for automated execution will accompany the reviewed implementation.

## Verification and evidence

### Checks in the current example

The [NumPy checker](scripts/check_fourier_numpy.py) checks the dimensions, binary
file sizes and finite values of the three BART arrays. It computes an independent
inverse Fourier transform of the BART-generated k-space without invoking BART,
then reports three relative L2 errors calculated from the complex arrays:
BART versus reference, NumPy versus reference, and BART versus NumPy. The reported
values are summarized under [Available evidence](#available-evidence).

The checker requires finite, nonzero comparison denominator norms and finite
errors. It has **no numerical acceptance threshold**, so completing these checks
does not establish a formal numerical pass. The
[synthetic procedure](tests/synthetic_2d/README.md) contains the execution steps
and numerical conventions.

### Recorded evidence

The following records document Ricardo's original exploratory exercise:

| Record | Contents |
| --- | --- |
| [comparison.txt](results/familiarization-2d-20261023/comparison.txt) | NumPy checker report with versions, conventions and the three relative errors |
| [nrmse.txt](results/familiarization-2d-20261023/nrmse.txt) | NRMSE reported by the BART command |
| [reported-metrics.csv](results/familiarization-2d-20261023/reported-metrics.csv) | Transcription of the reported metrics |
| [Results and figures](results/familiarization-2d-20261023/README.md) | Provenance, interpretation and links to the five supplied figures |

The figures provide visual context for the numerical comparison; magnitude images
alone do not establish agreement between complex arrays. The original complex
arrays are not included in the repository.

Reproduction from this repository or a clean checkout, a formal regression suite,
negative test cases and approved acceptance criteria remain pending. The recorded
evidence is limited to the documented 64 × 64 synthetic example and does not
establish validation of experimental 3D or CS reconstruction.

## Repository layout

The five directories below follow the organization proposed for the project.
Their intended roles and current contents are shown separately.

| Directory | Intended role | Current contents |
| --- | --- | --- |
| `src/` | Python workflow implementation | A README describing the planned workflow; implementation is pending |
| `configs/` | Reconstruction settings | A README describing configuration responsibilities; no configuration files are included yet |
| `tests/` | Verification cases | READMEs describing verification status and the exploratory synthetic 2D procedure; a formal regression suite remains pending |
| `scripts/` | Supporting utilities for data generation, execution and analysis | The NumPy checker, the synthetic visualization script and their documentation |
| `environment/` | Software setup records | macOS and BART records, reported build flags, direct dependency files and package-version snapshots |

The following locations support documentation, review and project continuity:

| Location | Role |
| --- | --- |
| `README.md` | Starting point for project scope, current usage, verification and documentation |
| `AI_USE.md` | Dated record of material AI assistance, tools and access modes, review decisions and verification performed |
| `docs/` | Project context, the accepted AI access/action contract, decision records and supporting notes |
| `results/` | Preserved reports, transcribed metrics and figure copies from the recorded synthetic exercise |
| `.github/` | Copilot instructions and a data-contract drafting prompt |

## Documentation and AI-assisted development

Use the references below for details beyond the overview and procedures in this
README. The documents are grouped by purpose.

### Project context and planning

| Document | Role |
| --- | --- |
| [Project context](docs/project-context.md) | Scope, methodology and evaluation planning |
| [Input inventory](docs/input-inventory.md) | Reported input availability and historical acquisition context |
| [Open questions](docs/open-questions.md) | Unresolved project questions, owner-reported Git context and pending evidence |
| [Sources and provenance](docs/sources.md) | Source documents and the evidence basis for project records |

### Existing synthetic exercise and environment

| Document | Role |
| --- | --- |
| [Synthetic procedure](tests/synthetic_2d/README.md) | Observed commands, numerical conventions and the proposed reproduction route |
| [Results and figures](results/familiarization-2d-20261023/README.md) | Recorded measurements, figure copies and provenance |
| [Local macOS environment](environment/local-macos.md) | Recorded hardware, software and BART build flags |
| [BART installation record](environment/bart-installation.md) | Guided preparation steps and available installation evidence |
| [Familiarization milestone](docs/milestones/01-familiarization.md) | Dated record of familiarization progress |

### AI access and action boundaries

The accepted **ENSF620-BART-DC v0.3.0** is the primary reference for AI access and
authority. It does not define the software specification or evaluation protocol.

| Document | Role |
| --- | --- |
| [Accepted access and action contract](docs/DATA_CONTRACT.md) | Accepted policy for reviewed context, restricted material and AI actions |
| [Contract decision register](docs/DATA_CONTRACT_DECISIONS.md) | Acceptance record, boundary decisions and unresolved access/action questions |
| [Workspace and data handling notes](docs/data-and-ai-boundaries.md) | Supporting guidance on workspace separation, repository handling and private processing/retention |

The workspace note explicitly defers to the accepted contract for AI access and
actions. It provides supporting context without amending the policy or defining
software requirements or an evaluation protocol.

### Collaboration guidance and AI-use records

| Document | Role |
| --- | --- |
| [Copilot instructions](.github/copilot-instructions.md) | Guidance for supervised work with the assistant |
| [Copilot handoff](docs/copilot-handoff.md) | Session context, recorded Copilot use, owner-reported Git checkpoint and suggested initial review request |
| [Git workflow](docs/git-workflow.md) | Git procedures and the historical initial-setup checkpoint |
| [AI use record](AI_USE.md) | Dated records of assistance, review decisions and checks performed |

The accepted policy takes precedence over collaboration guidance for AI access
and authority. Both the Copilot instructions and the handoff's initial review
request include the accepted contract and decision register. The handoff
distinguishes recorded assistance and owner-reported Git context from checks
needed for a new session. The dated entries in `AI_USE.md` describe assistance
and checks performed in individual sessions.

## Project history

The synthetic familiarization exercise predates the project's first commit. Its
Python scripts, selected text records and figure copies were subsequently
incorporated into this repository.

Dated accounts of the work and repository preparation are preserved in the
[familiarization milestone](docs/milestones/01-familiarization.md),
[AI use record](AI_USE.md) and [sources](docs/sources.md). The
[Git workflow](docs/git-workflow.md) retains the initial setup record and Git
procedures. The current implementation and verification state is described under
[Current status](#current-status) and
[Verification and evidence](#verification-and-evidence).

## Data and licensing

Laboratory data and derivatives, including extracted k-space, experimental BART
files and DICOM images, remain outside the shared repository and AI context.
The same applies to laboratory/GE extraction code, credentials and private storage
links. The AI assistant has no access to private storage or HPC systems.
Repository visibility does not change these boundaries.

The [accepted contract](docs/DATA_CONTRACT.md) defines AI access and action
boundaries. Its [decision register](docs/DATA_CONTRACT_DECISIONS.md) records
acceptance and outstanding boundary decisions.

A project licence has not yet been selected. Redistribution of third-party or
laboratory code requires separate review of the applicable permissions and terms.
