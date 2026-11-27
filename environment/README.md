# Environment Records

`local-macos.md` records supplied hardware/software evidence.
`bart-installation.md` distinguishes the guided recipe from returned outputs.
The requirements files contain direct versions, not complete locks.

The imported `python-requirements-verification.txt`,
`python-requirements-visualization.txt` and `bart-build.txt` are included. Do not
reconstruct missing package versions or treat these records as a tested fresh
installation. Ricardo reports use from a new, separate local Python environment
with the existing BART executable, and one ARC Slurm run using the modules and
paths stated in the shared script. The owner-reported details and evidence gaps
are recorded in [environment validation results](../docs/environment-validation-results.md);
they are not complete environment locks or independent execution logs. A
general HPC environment record and matched resource conditions have not been
established.
