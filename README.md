# ENSF 620 — BART Reconstruction Workflow

Author: Ricardo Andrés Aguilar Trejo  
Documentation consolidated: 2026-10-23; current context clarified subsequently  
Stage: familiarization evidence and contextual documentation review

## Question and scope

To what extent can an automated BART-based workflow reduce the manual intervention
required to reconstruct experimental MRI data in an HPC environment while
maintaining numerical equivalence with verified reference reconstructions?

The instructor's recommended core is **one verified 3D Cartesian manual–automated
pair**, with the main evaluation capped at the three datasets identified in the
proposal. Python is the primary workflow language, providing a simpler interface
for configuring, validating, executing and recording reviewed BART procedures.
The current implementation scope is Cartesian 2D and 3D reconstruction, including
compressed sensing; radial and 4D are outside that scope. Intended support,
reported availability, validated recipes and implemented functionality remain
distinct. The project organizes BART use; it does not modify BART's reconstruction
algorithms. Operator intervention is the primary outcome. Runtime and memory are
secondary outcomes.

Current experimental inputs are author-reported BART `.cfl`/`.hdr` files for brain
MRI 3D Cartesian reconstruction, including CS work. Their availability does not
establish inspection or validation. Scanner extraction and `.h5` conversion are
outside the current workflow implementation boundary.

## Current evidence

Ricardo executed a fully sampled **64 × 64, single-channel, 2D** synthetic example
on his Mac. BART generated the image and k-space and reconstructed the image.
A separate NumPy implementation reconstructed the same k-space. The supplied
console outputs and five figures support the following exploratory measurements:

| Comparison | Reported relative L2 error |
| --- | ---: |
| BART vs reference | 1.442448308e-07 |
| NumPy vs reference | 9.412963986e-08 |
| BART vs NumPy | 1.029663011e-07 |

**No numerical acceptance threshold was applied.** This is not yet the evaluated
manual–automated comparison, an experimental 3D baseline, a performance benchmark,
or validation of all BART functionality.

The current local platform is a MacBook Pro with Apple M5 and 24 GB memory,
replacing the Windows/WSL platform described in the submitted proposal. TALC needs
a separate environment record.

BART-generated synthetic phantoms will be used to develop and test matched manual
and automated procedures. Fixtures, settings, tests and acceptance criteria remain
to be defined and verified. DICOM comparison is only a proposed complementary
reference; it is not approved ground truth or a defined validation protocol.

## Navigation

- [Project context and evaluation boundaries](docs/project-context.md)
- [Familiarization milestone](docs/milestones/01-familiarization.md)
- [Synthetic procedure and verification limits](tests/synthetic_2d/README.md)
- [Local macOS environment](environment/local-macos.md)
- [BART installation record](environment/bart-installation.md)
- [Input inventory](docs/input-inventory.md)
- [Open questions](docs/open-questions.md)
- [Data and AI boundaries](docs/data-and-ai-boundaries.md)
- [Local Git and GitHub workflow](docs/git-workflow.md)
- [Copilot handoff](docs/copilot-handoff.md)
- [AI use disclosure](AI_USE.md)
- [Sources and provenance](docs/sources.md)
- [Reported results and figure copies](results/familiarization-2d-20261023/README.md)

## Layout

```text
src/          Future workflow implementation; not implemented yet
configs/      Future reviewed settings; no experimental recipe yet
tests/        Verification documentation; formal regression suite still pending
scripts/      Imported Python checker and visualization scripts
environment/  Environment records and dependency snapshots
docs/         Project notes, inventory, questions and handoff
results/      Reviewed synthetic measurements and uploaded figure copies
.github/      Repository guidance for Copilot
```

The first five directories follow the proposal. `docs/`, `results/`, and `.github/`
are organizational additions. Placeholder READMEs describe unimplemented components;
they do not claim those components exist.

## Assembly checkpoint and reproduction

At the 2026-10-23 pre-publication checkpoint, the staged listing includes the two
scripts copied from the local exercise, selected original text reports, and both
Python dependency snapshots. The starter deliberately omitted these files until
Ricardo could import them from his Mac:

```text
scripts/check_fourier_numpy.py
scripts/visualize_synthetic.py
```

The initial `main` branch push at commit `aad0525` is supported by author-supplied
terminal output. This does not establish publication of the current working branch,
clean-checkout reproduction, experimental validation or implementation of contract
controls.

Earlier assembly notes recorded SSH authentication as `rictr161` and identified the
following destination:

```text
git@github.com:rictr161/ensf620-bart-workflow.git
```

Do not include credentials or laboratory files. Review the imported contents before
committing; presence in a listing is not a byte-for-byte provenance check.

The [synthetic procedure](tests/synthetic_2d/README.md) documents the original
commands and a proposed reproduction route. Reproduction from this assembled
repository and from a clean checkout remains pending. The direct dependency files
are not complete locks; preserve the original `pip freeze` snapshots too.

## Boundaries and next work

Keep laboratory raw data, extracted k-space, derived laboratory images,
GE/laboratory extraction code, credentials and private storage links outside the
repository and AI-accessible context. A private repository does not authorize
sharing restricted material. Keep the upstream BART source and the existing
virtual environment separate. Generate synthetic arrays rather than committing
all run outputs.

Scientific work still pending includes clean-checkout reproduction, permitted-use/
retention records, a verified experimental reference recipe, its automated
counterpart, fixed tolerances/action-count rules, and HPC evaluation. Keep
experimental BART files, DICOM images, extractor code, credentials, private
storage and HPC access outside AI context and the shared repository. TALC remains
the planned HPC target; ARC is only a possible alternative.

No project licence has yet been selected. Do not invent a licence or redistribute
third-party/laboratory code.
