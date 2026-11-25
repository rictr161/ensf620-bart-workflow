# Operator-Intervention Measurement Checklist

**Status:** Task 9.3 documentation prepared under the protocol approved by
Ricardo in Task 9.2. No measurement runs have been performed.

Use this checklist with the [approved operator-intervention protocol](./operator-intervention-protocol.md).
It records a planned sequence, not evidence that a run occurred. Do not enter
results, exit codes, counts, or observations until the prospective run is
performed. Historical execution records are not measurements under this
checklist.

## 1. Required pair order

Perform one manual and one automated run in this exact order:

| Order | Case | Route |
|---:|---|---|
| 1 | Cartesian 2D | Manual |
| 2 | Cartesian 2D | Automated |
| 3 | Cartesian 3D | Manual |
| 4 | Cartesian 3D | Automated |
| 5 | Cartesian 3D CS, original single-channel case | Manual |
| 6 | Cartesian 3D CS, original single-channel case | Automated |
| 7 | Cartesian 3D CS, multichannel extended case | Manual |
| 8 | Cartesian 3D CS, multichannel extended case | Automated |

Within each pair, use the same prepared input and equivalent effective
scientific settings and requested outputs. Keep the same local host, BART build,
and comparable resource conditions. Record actual environment details and any
known competing load or interruption; do not infer equality from a past run.
Do not generate figures or perform reference comparisons.

## 2. Common preparation — outside the measured runs

Complete and record these preparations before the first case-specific action.
They are not part of the measured runs:

1. **Tools and environment:** identify the selected repository, BART executable,
   Python executable, and local platform. The recorded tutorial setup uses
   `$HOME/software/bart-1.0.00/bart` and
   `$HOME/bart-learning/.venv/bin/python`; confirm the actual current choices
   rather than assuming old versions are current. The tutorials' Section 1
   environment checks are the source for BART version, Python version, and
   platform identification.
2. **Prepared inputs:** confirm the exact BART base paths below and that their
   `.hdr`/`.cfl` pairs and previously recorded preparation checks are available.
   Do not regenerate, alter, or replace inputs. If a pair or required evidence
   is absent or invalid, mark preparation pending and do not start its
   measurement.
3. **Established settings:** confirm the case-specific settings in Section 3
   against the tutorials and the approved protocol. Do not tune, infer, or
   change them for this checklist.
4. **Destinations:** establish the common measurement root and the case parent
   directories in Section 4. Keep each final run-directory leaf absent until
   its run. The manual route creates its leaf as a counted action; the
   automated route must receive a leaf that does not yet exist. Confirm the
   automated sidecar-log paths in Section 4 are also new and unused.
5. **Evidence locations:** confirm that operational logs/records will be
   retained in each run directory, or in the documented sibling workflow log
   for automated invocations, and that the separate study intervention ledger
   location is available. The study ledger is not operational evidence.
6. **Instructions and checks:** have the cited tutorial blocks and applicable
   checkers available before measurement. The manual multichannel checks in
   Section 6.4 are fixed measured actions; do not run them as preparation or
   substitute an unreviewed check.

Recorded local-layout variables and version checks, adapted from the tutorial
Section 1 blocks:

```bash
cd "$HOME/projects/ensf620-bart-workflow" || exit "$?"
REPO="$(pwd -P)"
BART="$HOME/software/bart-1.0.00/bart"
PYTHON="$HOME/bart-learning/.venv/bin/python"
PREP_ROOT="$HOME/bart-learning/bart-workflow-preparations"
MEAS_ROOT="$HOME/bart-learning/bart-workflow-reconstructions/operator-intervention-measurements"

test -x "$BART" && test -x "$PYTHON"
"$PYTHON" -c 'import numpy'
"$BART" version -V
"$PYTHON" --version
uname -srm
```

Treat these as recorded-layout examples; confirm actual choices before
measurement. Do not copy environment/version values from earlier reports as
current measurements.

Recorded input bases:

| Case | Prepared input(s) |
|---|---|
| Cartesian 2D | `$HOME/bart-learning/bart-workflow-preparations/generation-01/kspace` |
| Cartesian 3D | `$HOME/bart-learning/bart-workflow-preparations/generation-3d-01/kspace` |
| Cartesian 3D CS, original | `$HOME/bart-learning/bart-workflow-preparations/generation-3d-cs-01/kspace_undersampled`, plus `mask3d` and `sensitivities` from that same directory |
| Cartesian 3D CS, multichannel extended | `$HOME/bart-learning/bart-workflow-preparations/generation-3d-ecalib-01/kspace_undersampled`; neither route supplies a mask or sensitivities |

For the 2D and fully sampled 3D preparations, the existing pair-check commands
are documented in the tutorial setup/preparation sections:

```text
"$PYTHON" "$REPO/scripts/check_preparation_pair.py" \
  "$HOME/bart-learning/bart-workflow-preparations/generation-01" kspace

"$PYTHON" "$REPO/scripts/check_preparation_pair_3d.py" \
  "$HOME/bart-learning/bart-workflow-preparations/generation-3d-01" kspace
```

For the original CS preparation, use the already-documented input/mask and
sensitivity checks in Sections 5–6 of the
[manual Cartesian 3D CS tutorial](./tutorials/manual-cartesian-3d-cs.md), or
confirm their existing preparation records. Do not repeat synthetic
preparation.

The preparation paths were supplied for this task, but their current file
presence and output-destination availability have not been checked here.

## 3. Frozen effective settings

These are the already-established settings for the planned pairs:

| Case | Effective settings to confirm before each pair |
|---|---|
| Cartesian 2D | Fully sampled, single-channel 64 × 64; centered unitary inverse FFT over axes 0 and 1. |
| Cartesian 3D | Fully sampled, single-channel 64 × 64 × 64; centered unitary inverse FFT over axes 0, 1, and 2. |
| Cartesian 3D CS, original | Single-channel undersampled k-space with the same preparation's supplied `mask3d` and constant `sensitivities`; `manual-cartesian-3d-cs` profile: FISTA, `dau2`, wavelet regularization on axes 0–2 with weight 0.01, 100 iterations, step 0.95, random shift disabled, data scaling 1. |
| Cartesian 3D CS, multichannel extended | Same prepared multichannel k-space for both routes (the reviewed case has eight channels). Generate a mask with `pattern`, estimate sensitivities with `ecalib` using calibration region `64:16:16`, kernel `6:6:6`, threshold `0.001`, crop `0.8`, and exactly one map set (`-m 1`); use the `manual-cartesian-3d-cs` profile and `pics` settings listed above. The case is multichannel; one map set does not mean one channel. |

## 4. Destinations and records

Proposed root:

```text
$HOME/bart-learning/bart-workflow-reconstructions/operator-intervention-measurements/
```

Create/confirm only the root and case parent directories during common
preparation. Keep the listed run-directory leaves new and unused:

| Case | Manual destination | Automated destination |
|---|---|---|
| Cartesian 2D | `cartesian-2d/manual-01` | `cartesian-2d/automated-01` |
| Cartesian 3D | `cartesian-3d/manual-01` | `cartesian-3d/automated-01` |
| Cartesian 3D CS, original | `cartesian-3d-cs-original/manual-01` | `cartesian-3d-cs-original/automated-01` |
| Cartesian 3D CS, multichannel extended | `cartesian-3d-cs-multichannel/manual-01` | `cartesian-3d-cs-multichannel/automated-01` |

The paths in the table are relative to the proposed root. The manual route
creates its final destination with one separately defined `mkdir` block after
the pre-run review; count that block as one **Execution** intervention. The
automated route must not create its final leaf beforehand: the workflow
requires a destination that does not already exist and creates its own run
directory. Preserve each automated CLI's console output and process exit code
in a new sibling log, not in that not-yet-created leaf:
`cartesian-2d/automated-01-workflow.log`,
`cartesian-3d/automated-01-workflow.log`,
`cartesian-3d-cs-original/automated-01-workflow.log`, and
`cartesian-3d-cs-multichannel/automated-01-workflow.log`. Confirm these paths
are absent during common preparation; the invocation block creates the log
while leaving the workflow destination absent until the workflow itself runs.

Keep the study-only intervention ledger separately, for example at
`$HOME/bart-learning/bart-workflow-reconstructions/operator-intervention-measurements/study/intervention-ledger.csv`.
Preparing or filling that ledger and calculating its totals are excluded from
the intervention count. Do not copy it into a run's operational record.

### Equivalent operational evidence

For each run, retain the case and route, exact input/output identities,
commands/invocations, operator-supplied and effective settings, relevant
software/environment versions, separate operation and check outcomes,
produced outputs/logs, and any failures, corrections, recovery, or deviation.
Manual commands write their logs to the run directory; the automated workflow
provides its stage records and operation logs there. A person separately
preserving a missing required operational artifact is one evidence-recording
action under the protocol. Do not make duplicate copies solely to create an
action. Keep the intervention ledger separate.

## 5. Action IDs and fixed counting conventions

The IDs below are stable identifiers for this checklist. The plan column
describes intended actions; the execution and result fields remain blank until
a run occurs.

- `CFG`: one independently edited-and-saved named configuration transaction,
  if one occurs. For this plan, scientific and path values are passed in the
  listed BART or workflow invocation, so no separate configuration artifact
  is planned. Record `N/A` if none occurs; count an independent edit/save once
  if it does occur.
- `PR`: the approved pre-run human review, once per route.
- `DIR`: the manual route's single `mkdir` block, one **Execution** action.
- `OP`: each separately submitted BART invocation or complete automated
  workflow invocation is one **Execution** action. The blocks below are fixed
  before measurement and must not be combined or split after observing results.
- `CHK`: one independently launched check is one **Check or review** action.
  Reviewing its result later as a separate action is counted separately.
- `MID`: a planned manual intermediate human review is one **Check or review**
  action when it actually occurs. The automated route has no human
  intermediate reviews.
- `FIN`: the approved final human review, once per route, after the route has
  finished or stopped.
- `EV`: one independent save/preservation of operational evidence when
  required and not already saved by an invocation. Mark `N/A` if no separate
  human preservation action is needed.
- Internal automated checks and wrapper calls are software-only and are not
  counted. They must not introduce pauses or interactive questions.

The start of a run is its first case-specific configuration transaction, if
any, or otherwise its `PR` action. Its end is after the route finishes or
stops, required output checks are complete, and `FIN` and any required
operational evidence preservation are complete. Do not include common
preparation or study-ledger work.

## 6. Ordered route actions and verified instructions

For each manual BART operation, use the command block cited below with only the
prepared-input and new-output paths substituted. Capture its actual exit code
and preserve its log. If an operation or mandatory check fails, stop dependent
manual stages, preserve the attempt, and record the failure. Do not retry
silently or replace a failed attempt.

### 6.1 Cartesian 2D

**Manual — `C2D-M`**

| Order / ID | Planned action | Category | Exact source or instruction |
|---|---|---|---|
| 1 `C2D-M-CFG` | Separate configuration transaction, only if performed; otherwise `N/A`. | Configuration | Values are in the invocation below. |
| 2 `C2D-M-PR` | Review the input, route, new destination, and frozen settings. | Check or review | Protocol pre-run block. |
| 3 `C2D-M-DIR` | Create the manual run leaf once. | Execution | One `mkdir "$MEAS_ROOT/cartesian-2d/manual-01"` block; its parent is prepared beforehand. |
| 4 `C2D-M-OP1` | Run the direct BART inverse FFT. | Execution | Manual 2D tutorial, Section 5; use the input and destination from Sections 2 and 4 here. Do not run the Python workflow. |
| 5 `C2D-M-CHK1` | Independently validate the reconstruction pair. | Check or review | Complete adapted output-check block below, based on the manual 2D tutorial, Section 6. |
| 6 `C2D-M-FIN` | Review the operation result, output-check result, effective settings, and available logs. | Check or review | Protocol final block. |
| 7 `C2D-M-EV` | Separately preserve any required operational evidence not already in the log/record. | Operational evidence recording | Conditional under Section 4; otherwise `N/A`. |

**Automated — `C2D-A`**

| Order / ID | Planned action | Category | Exact source or instruction |
|---|---|---|---|
| 1 `C2D-A-CFG` | Separate configuration transaction, only if performed; otherwise `N/A`. | Configuration | Values are in the invocation below. |
| 2 `C2D-A-PR` | Review the input, route, absent destination, and frozen settings. | Check or review | Protocol pre-run block. |
| 3 `C2D-A-OP1` | Submit one workflow CLI invocation. Leave the destination leaf absent. | Execution | `src/README.md`, terminal example; no figure option. |
| 4 `C2D-A-AUTO` | Allow internal input/output validation to proceed or stop the workflow. | Software-only | Not a human intervention; no pause or review between stages. |
| 5 `C2D-A-FIN` | After the CLI returns, review the outcome, stage records, effective settings, and logs. | Check or review | Protocol final block. |
| 6 `C2D-A-EV` | Separately preserve any required operational evidence not already produced. | Operational evidence recording | Conditional under Section 4; otherwise `N/A`. |

### 6.2 Cartesian 3D

**Manual — `C3D-M`**

| Order / ID | Planned action | Category | Exact source or instruction |
|---|---|---|---|
| 1 `C3D-M-CFG` | Separate configuration transaction, only if performed; otherwise `N/A`. | Configuration | Values are in the invocation below. |
| 2 `C3D-M-PR` | Review the input, route, new destination, and frozen settings. | Check or review | Protocol pre-run block. |
| 3 `C3D-M-DIR` | Create the manual run leaf once. | Execution | One `mkdir "$MEAS_ROOT/cartesian-3d/manual-01"` block; its parent is prepared beforehand. |
| 4 `C3D-M-OP1` | Run the direct BART inverse FFT. | Execution | Manual 3D tutorial, Section 5. |
| 5 `C3D-M-CHK1` | Independently validate the reconstruction pair. | Check or review | Captured checker block below. |
| 6 `C3D-M-FIN` | Review the operation result, output-check result, effective settings, and available logs. | Check or review | Protocol final block. |
| 7 `C3D-M-EV` | Separately preserve any required operational evidence not already in the log/record. | Operational evidence recording | Conditional under Section 4; otherwise `N/A`. |

**Automated — `C3D-A`**

| Order / ID | Planned action | Category | Exact source or instruction |
|---|---|---|---|
| 1 `C3D-A-CFG` | Separate configuration transaction, only if performed; otherwise `N/A`. | Configuration | Values are in the invocation below. |
| 2 `C3D-A-PR` | Review the input, route, absent destination, and frozen settings. | Check or review | Protocol pre-run block. |
| 3 `C3D-A-OP1` | Submit one workflow CLI invocation. Leave the destination leaf absent. | Execution | `src/README.md`, terminal example; no figure option. |
| 4 `C3D-A-AUTO` | Allow internal validation to proceed or stop the workflow. | Software-only | Not a human intervention; no pause or review between stages. |
| 5 `C3D-A-FIN` | After the CLI returns, review the outcome, stage records, effective settings, and logs. | Check or review | Protocol final block. |
| 6 `C3D-A-EV` | Separately preserve any required operational evidence not already produced. | Operational evidence recording | Conditional under Section 4; otherwise `N/A`. |

### 6.3 Cartesian 3D CS, original single-channel case

**Manual — `CSO-M`**

| Order / ID | Planned action | Category | Exact source or instruction |
|---|---|---|---|
| 1 `CSO-M-CFG` | Separate configuration transaction, only if performed; otherwise `N/A`. | Configuration | The reviewed profile values are in the invocation below. |
| 2 `CSO-M-PR` | Review the k-space, same-preparation mask and sensitivities, route, destination, and settings. | Check or review | Protocol pre-run block; rely on the same preparation's recorded checks. |
| 3 `CSO-M-DIR` | Create the manual run leaf once. | Execution | One `mkdir "$MEAS_ROOT/cartesian-3d-cs-original/manual-01"` block; its parent is prepared beforehand. |
| 4 `CSO-M-OP1` | Run direct BART `pics` with the supplied mask and sensitivities. | Execution | Manual 3D CS tutorial, Section 8; do not generate or replace its mask/maps. |
| 5 `CSO-M-CHK1` | Independently validate the reconstruction pair. | Check or review | Captured checker block below. |
| 6 `CSO-M-FIN` | Review the operation, output check, effective settings, and available logs. | Check or review | Protocol final block. |
| 7 `CSO-M-EV` | Separately preserve any required operational evidence not already in the log/record. | Operational evidence recording | Conditional under Section 4; otherwise `N/A`. |

**Automated — `CSO-A`**

| Order / ID | Planned action | Category | Exact source or instruction |
|---|---|---|---|
| 1 `CSO-A-CFG` | Separate configuration transaction, only if performed; otherwise `N/A`. | Configuration | Values are in the invocation below. |
| 2 `CSO-A-PR` | Review the inputs, route, absent destination, and frozen settings. | Check or review | Protocol pre-run block. |
| 3 `CSO-A-OP1` | Submit one workflow CLI invocation. Leave the destination leaf absent. | Execution | `src/README.md`, supplied-mask/profile example; no figure option. |
| 4 `CSO-A-AUTO` | Allow internal input, mask, sensitivity, and output checks to proceed or stop the workflow. | Software-only | Not a human intervention; no pause or review between stages. |
| 5 `CSO-A-FIN` | After the CLI returns, review the outcome, stage records, effective settings, and logs. | Check or review | Protocol final block. |
| 6 `CSO-A-EV` | Separately preserve any required operational evidence not already produced. | Operational evidence recording | Conditional under Section 4; otherwise `N/A`. |

### 6.4 Cartesian 3D CS, multichannel extended case

Both routes use the same `generation-3d-ecalib-01/kspace_undersampled` input.
Each route obtains its own `sampling_mask`, sensitivities, eigenvalues, and
reconstruction in its own destination. Do not supply `mask3d` or sensitivities.

**Manual — `CSX-M`**

| Order / ID | Planned action | Category | Exact source or instruction |
|---|---|---|---|
| 1 `CSX-M-CFG` | Separate configuration transaction, only if performed; otherwise `N/A`. | Configuration | Values are in the direct BART invocations below. |
| 2 `CSX-M-PR` | Review the same multichannel k-space, route, destination, and frozen settings. | Check or review | Protocol pre-run block. Resolve the current input and destination readiness item in Section 8 before starting. |
| 3 `CSX-M-DIR` | Create the manual run leaf once. | Execution | One `mkdir "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01"` block; its parent is prepared beforehand. |
| 4 `CSX-M-OP1` | Estimate this run's pattern from the prepared k-space. | Execution | Direct BART `pattern` invocation shown below. |
| 5 `CSX-M-CHK1` | Read and validate the multichannel k-space and generated mask, then resolve and validate the frozen `ecalib` settings and their compatibility. | Check or review | Complete manual Python block immediately after the `pattern` invocation below; uses read/validation functions from `src/bart_workflow.py` only. |
| 6 `CSX-M-MID1` | Review the pattern operation and check before proceeding to calibration, if performed. | Check or review | Fixed manual intermediate checkpoint; do not proceed to `ecalib` if `CSX-M-CHK1` fails. |
| 7 `CSX-M-OP2` | Estimate one set of sensitivity maps and eigenvalues from the same k-space. | Execution | Direct BART `ecalib` invocation shown below. |
| 8 `CSX-M-CHK2` | Validate the k-space, generated sensitivities, and eigenvalues, including dimensions, channels, one map set, storage, and finiteness. | Check or review | Complete manual Python block immediately after the `ecalib` invocation below; uses read/validation functions from `src/bart_workflow.py` only. |
| 9 `CSX-M-MID2` | Review the calibration operation and sensitivity/eigenvalue check before `pics`, if performed. | Check or review | Fixed manual intermediate checkpoint; do not proceed to `pics` if `CSX-M-CHK2` fails. |
| 10 `CSX-M-OP3` | Run direct BART `pics` with this run's generated mask and sensitivities. | Execution | Same reviewed `pics` settings as the original CS case; invocation below. |
| 11 `CSX-M-CHK3` | Independently validate the reconstruction output pair. | Check or review | Captured checker block below; subject to Section 8 prerequisites. |
| 12 `CSX-M-FIN` | After the route finishes or stops, review pattern, sensitivity, reconstruction, checks, effective settings, logs, and outputs. | Check or review | Protocol final block; no inter-stage pause is added to the automated pair. |
| 13 `CSX-M-EV` | Separately preserve any required operational evidence not already in the logs/record. | Operational evidence recording | Conditional under Section 4; otherwise `N/A`. |

The manual BART invocations are separate fixed blocks in this checklist. The
Python checks between them are also separate fixed blocks, each counted
only as its existing `CHK` action. They reuse reading and validation logic
from the version of `src/bart_workflow.py` used for the study; this shares
check logic and does not claim algorithmic independence. The snippets do not
call `run_reconstruction`, `main`, or any function that launches BART.

```bash
if "$BART" pattern \
  "$HOME/bart-learning/bart-workflow-preparations/generation-3d-ecalib-01/kspace_undersampled" \
  "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/sampling_mask" \
  > "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/sampling-pattern.log" 2>&1; then
  measurement_pattern_status=0
else
  measurement_pattern_status=$?
fi
printf 'BART pattern exit code: %s\n' "$measurement_pattern_status" \
  >> "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/sampling-pattern.log"
if [ "$measurement_pattern_status" -eq 0 ]; then
  printf 'SUCCESS: BART pattern completed.\n'
else
  printf 'ERROR: BART pattern failed (exit code %s); stop before dependent stages.\n' \
    "$measurement_pattern_status" >&2
fi
```

Manual pattern and k-space validation (`CSX-M-CHK1`):

```bash
if "$PYTHON" -B - \
  "$REPO" \
  "$HOME/bart-learning/bart-workflow-preparations/generation-3d-ecalib-01/kspace_undersampled" \
  "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/sampling_mask" \
  "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01" \
  > "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/pattern-check.txt" 2>&1 <<'PY'
import sys
from pathlib import Path

repo = Path(sys.argv[1])
kspace_path = Path(sys.argv[2])
mask_path = Path(sys.argv[3])
run_directory = Path(sys.argv[4])
sys.path.insert(0, str(repo / "src"))

from bart_workflow import (
    ReconstructionConfig,
    _resolve_ecalib_settings,
    _validate_binary_mask,
    _validate_cs_kspace,
    _validate_cs_mask_shape,
    _validate_ecalib_compatibility,
    _validate_masked_kspace,
    read_bart_array,
)

print(f"K-space files: {kspace_path}.hdr and {kspace_path}.cfl")
kspace = read_bart_array(kspace_path)
print(f"K-space shape: {kspace.shape}")
print("PASS: BART pair dimensions, binary size, and finite values.")
_validate_cs_kspace(kspace)
print("PASS: Cartesian 3D compressed-sensing k-space structure.")

print(f"Sampling-mask files: {mask_path}.hdr and {mask_path}.cfl")
mask = read_bart_array(mask_path)
print(f"Sampling-mask shape: {mask.shape}")
print("PASS: BART pair dimensions, binary size, and finite values.")
_validate_cs_mask_shape(mask, kspace)
print("PASS: mask spatial shape and singleton trailing axes.")
_validate_binary_mask(mask)
print("PASS: mask is binary and contains acquired and omitted positions.")
_validate_masked_kspace(mask, kspace)
print("PASS: omitted mask positions contain zero k-space across channels.")

config = ReconstructionConfig(
    kspace=kspace_path,
    output_directory=run_directory,
    spatial_dimensionality=3,
    ecalib_calibration_region="64:16:16",
    ecalib_kernel_size="6:6:6",
    ecalib_threshold=0.001,
    ecalib_crop=0.8,
    ecalib_map_sets=1,
)
ecalib_settings = _resolve_ecalib_settings(config)
print(f"Resolved ecalib settings: {ecalib_settings}")
_validate_ecalib_compatibility(ecalib_settings, kspace, mask)
print("PASS: ecalib settings and fully sampled calibration region are compatible.")
PY
then
  measurement_pattern_check_status=0
else
  measurement_pattern_check_status=$?
fi
printf 'CSX-M-CHK1 exit code: %s\n' "$measurement_pattern_check_status" \
  >> "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/pattern-check.txt"
if [ "$measurement_pattern_check_status" -eq 0 ]; then
  cat "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/pattern-check.txt"
  printf 'SUCCESS: CSX-M-CHK1 passed; the operator may review before ecalib.\n'
else
  cat "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/pattern-check.txt" >&2
  printf 'ERROR: CSX-M-CHK1 failed (exit code %s); stop before ecalib.\n' \
    "$measurement_pattern_check_status" >&2
fi
```

Do not proceed to `ecalib` unless the actual `CSX-M-CHK1` exit code is `0`
and its result has received the planned human intermediate review.

```bash
if "$BART" ecalib \
  -r 64:16:16 -k 6:6:6 -t 0.001 -c 0.8 -m 1 \
  "$HOME/bart-learning/bart-workflow-preparations/generation-3d-ecalib-01/kspace_undersampled" \
  "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/sensitivities" \
  "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/eigenvalues" \
  > "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/ecalib.log" 2>&1; then
  measurement_ecalib_status=0
else
  measurement_ecalib_status=$?
fi
printf 'BART ecalib exit code: %s\n' "$measurement_ecalib_status" \
  >> "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/ecalib.log"
if [ "$measurement_ecalib_status" -eq 0 ]; then
  printf 'SUCCESS: BART ecalib completed.\n'
else
  printf 'ERROR: BART ecalib failed (exit code %s); stop before dependent stages.\n' \
    "$measurement_ecalib_status" >&2
fi
```

Manual sensitivity and eigenvalue validation (`CSX-M-CHK2`):

```bash
if "$PYTHON" -B - \
  "$REPO" \
  "$HOME/bart-learning/bart-workflow-preparations/generation-3d-ecalib-01/kspace_undersampled" \
  "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/sensitivities" \
  "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/eigenvalues" \
  > "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/calibration-check.txt" 2>&1 <<'PY'
import sys
from pathlib import Path

repo = Path(sys.argv[1])
kspace_path = Path(sys.argv[2])
sensitivity_path = Path(sys.argv[3])
eigenvalues_path = Path(sys.argv[4])
sys.path.insert(0, str(repo / "src"))

from bart_workflow import (
    _validate_cs_kspace,
    _validate_eigenvalues,
    _validate_sensitivity_maps,
    read_bart_array,
)

print(f"K-space files: {kspace_path}.hdr and {kspace_path}.cfl")
kspace = read_bart_array(kspace_path)
print(f"K-space shape: {kspace.shape}")
print("PASS: BART pair dimensions, binary size, and finite values.")
_validate_cs_kspace(kspace)
print("PASS: Cartesian 3D compressed-sensing k-space structure.")

print(f"Sensitivity files: {sensitivity_path}.hdr and {sensitivity_path}.cfl")
sensitivities = read_bart_array(sensitivity_path)
print(f"Sensitivity shape: {sensitivities.shape}")
print("PASS: BART pair dimensions, binary size, and finite values.")
_validate_sensitivity_maps(sensitivities, kspace)
print("PASS: spatial shape, channel count, one map set, and nonzero sensitivities.")

print(f"Eigenvalue files: {eigenvalues_path}.hdr and {eigenvalues_path}.cfl")
eigenvalues = read_bart_array(eigenvalues_path)
print(f"Eigenvalue shape: {eigenvalues.shape}")
print("PASS: BART pair dimensions, binary size, and finite values.")
_validate_eigenvalues(eigenvalues, kspace)
print("PASS: eigenvalue spatial shape and singleton map-set axes.")
PY
then
  measurement_sensitivity_check_status=0
else
  measurement_sensitivity_check_status=$?
fi
printf 'CSX-M-CHK2 exit code: %s\n' "$measurement_sensitivity_check_status" \
  >> "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/calibration-check.txt"
if [ "$measurement_sensitivity_check_status" -eq 0 ]; then
  cat "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/calibration-check.txt"
  printf 'SUCCESS: CSX-M-CHK2 passed; the operator may review before pics.\n'
else
  cat "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/calibration-check.txt" >&2
  printf 'ERROR: CSX-M-CHK2 failed (exit code %s); stop before pics.\n' \
    "$measurement_sensitivity_check_status" >&2
fi
```

Do not proceed to `pics` unless the actual `CSX-M-CHK2` exit code is `0` and
its result has received the planned human intermediate review.

```bash
if "$BART" pics \
  --fista --wavelet dau2 -R W:7:0:0.01 -i 100 -s 0.95 -n -w 1 \
  -p "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/sampling_mask" \
  "$HOME/bart-learning/bart-workflow-preparations/generation-3d-ecalib-01/kspace_undersampled" \
  "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/sensitivities" \
  "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/reconstruction" \
  > "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/reconstruction.log" 2>&1; then
  measurement_pics_status=0
else
  measurement_pics_status=$?
fi
printf 'BART pics exit code: %s\n' "$measurement_pics_status" \
  >> "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/reconstruction.log"
if [ "$measurement_pics_status" -eq 0 ]; then
  printf 'SUCCESS: BART pics completed.\n'
else
  printf 'ERROR: BART pics failed (exit code %s).\n' \
    "$measurement_pics_status" >&2
fi
```

Submit each BART operation and each `CHK` block separately as listed. Each
whole block remains its already-defined single intervention; its internal
logging, imports, and validation calls do not add interventions. Capture the
real exit code immediately, retain it in that block's run log, and display a
success/error summary. Leave the terminal session open on failure. Stop
dependent manual stages after a failed operation or mandatory check, preserving
the failed attempt and recording any later correction or recovery separately.

**Automated — `CSX-A`**

| Order / ID | Planned action | Category | Exact source or instruction |
|---|---|---|---|
| 1 `CSX-A-CFG` | Separate configuration transaction, only if performed; otherwise `N/A`. | Configuration | Values are in the single workflow invocation below. |
| 2 `CSX-A-PR` | Review the same multichannel k-space, route, absent destination, and frozen settings. | Check or review | Protocol pre-run block. |
| 3 `CSX-A-OP1` | Submit one workflow CLI invocation with pattern and `ecalib` selected. Do not create the destination leaf. | Execution | Verified terminal CLI options in `src/README.md` and `src/bart_workflow.py`. |
| 4 `CSX-A-AUTO` | Workflow validates pattern, calibration inputs/maps, and reconstruction before dependent stages; it proceeds or stops without requesting human review. | Software-only | Not a human intervention. Do not add pauses. |
| 5 `CSX-A-FIN` | After the CLI returns or stops, review all stage records, pattern, sensitivities, reconstruction, effective settings, and logs. | Check or review | Protocol final block. |
| 6 `CSX-A-EV` | Separately preserve any required operational evidence not already produced. | Operational evidence recording | Conditional under Section 4; otherwise `N/A`. |

Verified workflow invocation:

```bash
if "$PYTHON" "$REPO/src/bart_workflow.py" \
  --kspace "$HOME/bart-learning/bart-workflow-preparations/generation-3d-ecalib-01/kspace_undersampled" \
  --output-directory "$MEAS_ROOT/cartesian-3d-cs-multichannel/automated-01" \
  --spatial-dimensionality 3 \
  --compressed-sensing \
  --sampling-source bart-pattern \
  --sensitivity-source ecalib \
  --ecalib-calibration-region 64:16:16 \
  --ecalib-kernel-size 6:6:6 \
  --ecalib-threshold 0.001 \
  --ecalib-crop 0.8 \
  --ecalib-map-sets 1 \
  --reconstruction-profile manual-cartesian-3d-cs \
  --bart-executable "$BART" \
  > "$MEAS_ROOT/cartesian-3d-cs-multichannel/automated-01-workflow.log" 2>&1; then
  measurement_workflow_cs_extended_status=0
else
  measurement_workflow_cs_extended_status=$?
fi
printf 'Workflow exit code: %s\n' "$measurement_workflow_cs_extended_status" \
  >> "$MEAS_ROOT/cartesian-3d-cs-multichannel/automated-01-workflow.log"
cat "$MEAS_ROOT/cartesian-3d-cs-multichannel/automated-01-workflow.log"
if [ "$measurement_workflow_cs_extended_status" -eq 0 ]; then
  printf 'SUCCESS: extended CS workflow completed.\n'
else
  printf 'ERROR: extended CS workflow failed (exit code %s).\n' \
    "$measurement_workflow_cs_extended_status" >&2
fi
```

### Verified manual/automated commands for the first three cases

The following operation syntax and checker interfaces are from the cited
tutorials and existing terminal examples. Substitute the corresponding output
path from Section 4; do not change scientific arguments.

Manual BART operations:

```bash
if "$BART" fft -i -u 3 \
  "$HOME/bart-learning/bart-workflow-preparations/generation-01/kspace" \
  "$MEAS_ROOT/cartesian-2d/manual-01/reconstruction" \
  > "$MEAS_ROOT/cartesian-2d/manual-01/reconstruction.log" 2>&1; then
  measurement_fft_2d_status=0
else
  measurement_fft_2d_status=$?
fi
printf 'BART fft exit code: %s\n' "$measurement_fft_2d_status" \
  >> "$MEAS_ROOT/cartesian-2d/manual-01/reconstruction.log"
if [ "$measurement_fft_2d_status" -eq 0 ]; then
  printf 'SUCCESS: Cartesian 2D BART fft completed.\n'
else
  printf 'ERROR: Cartesian 2D BART fft failed (exit code %s).\n' \
    "$measurement_fft_2d_status" >&2
fi
```

```bash
if "$BART" fft -i -u 7 \
  "$HOME/bart-learning/bart-workflow-preparations/generation-3d-01/kspace" \
  "$MEAS_ROOT/cartesian-3d/manual-01/reconstruction" \
  > "$MEAS_ROOT/cartesian-3d/manual-01/reconstruction.log" 2>&1; then
  measurement_fft_3d_status=0
else
  measurement_fft_3d_status=$?
fi
printf 'BART fft exit code: %s\n' "$measurement_fft_3d_status" \
  >> "$MEAS_ROOT/cartesian-3d/manual-01/reconstruction.log"
if [ "$measurement_fft_3d_status" -eq 0 ]; then
  printf 'SUCCESS: Cartesian 3D BART fft completed.\n'
else
  printf 'ERROR: Cartesian 3D BART fft failed (exit code %s).\n' \
    "$measurement_fft_3d_status" >&2
fi
```

```bash
if "$BART" pics \
  --fista --wavelet dau2 -R W:7:0:0.01 -i 100 -s 0.95 -n -w 1 \
  -p "$HOME/bart-learning/bart-workflow-preparations/generation-3d-cs-01/mask3d" \
  "$HOME/bart-learning/bart-workflow-preparations/generation-3d-cs-01/kspace_undersampled" \
  "$HOME/bart-learning/bart-workflow-preparations/generation-3d-cs-01/sensitivities" \
  "$MEAS_ROOT/cartesian-3d-cs-original/manual-01/reconstruction" \
  > "$MEAS_ROOT/cartesian-3d-cs-original/manual-01/reconstruction.log" 2>&1; then
  measurement_cs_original_pics_status=0
else
  measurement_cs_original_pics_status=$?
fi
printf 'BART pics exit code: %s\n' "$measurement_cs_original_pics_status" \
  >> "$MEAS_ROOT/cartesian-3d-cs-original/manual-01/reconstruction.log"
if [ "$measurement_cs_original_pics_status" -eq 0 ]; then
  printf 'SUCCESS: original CS BART pics completed.\n'
else
  printf 'ERROR: original CS BART pics failed (exit code %s).\n' \
    "$measurement_cs_original_pics_status" >&2
fi
```

The complete 2D check below adapts the inline block in Section 6 of the
[manual Cartesian 2D tutorial](./tutorials/manual-cartesian-2d.md), changing
only the output path and result logging. It reads only `reconstruction` and
does not perform an inverse transform, figure, or comparison. The 3D, original
CS, and extended CS output checks use `check_preparation_pair_3d.py` with the
`reconstruction` pair argument. Each checker launch is its existing independent
`CHK` action; the check records retain its output and actual exit code.
Reviewing a check record later during `FIN` is a separate human review action.

Cartesian 2D manual output check (`C2D-M-CHK1`):

```bash
if "$PYTHON" -B - "$REPO" \
  "$MEAS_ROOT/cartesian-2d/manual-01/reconstruction" \
  > "$MEAS_ROOT/cartesian-2d/manual-01/reconstruction-check.txt" 2>&1 <<'PY'
import sys
from pathlib import Path

sys.path.insert(0, str(Path(sys.argv[1]) / "scripts"))
from check_fourier_numpy import read_bart_2d

read_bart_2d(sys.argv[2])
print(
    "VALID: reconstruction (64 x 64, singleton trailing axes, "
    "correct size, finite values)"
)
PY
then
  measurement_2d_check_status=0
else
  measurement_2d_check_status=$?
fi
printf 'C2D-M-CHK1 exit code: %s\n' "$measurement_2d_check_status" \
  >> "$MEAS_ROOT/cartesian-2d/manual-01/reconstruction-check.txt"
if [ "$measurement_2d_check_status" -eq 0 ]; then
  cat "$MEAS_ROOT/cartesian-2d/manual-01/reconstruction-check.txt"
  printf 'SUCCESS: C2D-M-CHK1 passed.\n'
else
  cat "$MEAS_ROOT/cartesian-2d/manual-01/reconstruction-check.txt" >&2
  printf 'ERROR: C2D-M-CHK1 failed (exit code %s).\n' \
    "$measurement_2d_check_status" >&2
fi
```

Cartesian 3D manual output check:

```bash
if "$PYTHON" "$REPO/scripts/check_preparation_pair_3d.py" \
  "$MEAS_ROOT/cartesian-3d/manual-01" reconstruction \
  > "$MEAS_ROOT/cartesian-3d/manual-01/reconstruction-check.txt" 2>&1; then
  measurement_3d_check_status=0
else
  measurement_3d_check_status=$?
fi
printf 'Checker exit code: %s\n' "$measurement_3d_check_status" \
  >> "$MEAS_ROOT/cartesian-3d/manual-01/reconstruction-check.txt"
if [ "$measurement_3d_check_status" -eq 0 ]; then
  printf 'SUCCESS: Cartesian 3D reconstruction check passed.\n'
else
  printf 'ERROR: Cartesian 3D reconstruction check failed (exit code %s).\n' \
    "$measurement_3d_check_status" >&2
fi
```

Original Cartesian 3D CS manual output check:

```bash
if "$PYTHON" "$REPO/scripts/check_preparation_pair_3d.py" \
  "$MEAS_ROOT/cartesian-3d-cs-original/manual-01" reconstruction \
  > "$MEAS_ROOT/cartesian-3d-cs-original/manual-01/reconstruction-check.txt" 2>&1; then
  measurement_cs_original_check_status=0
else
  measurement_cs_original_check_status=$?
fi
printf 'Checker exit code: %s\n' "$measurement_cs_original_check_status" \
  >> "$MEAS_ROOT/cartesian-3d-cs-original/manual-01/reconstruction-check.txt"
if [ "$measurement_cs_original_check_status" -eq 0 ]; then
  printf 'SUCCESS: original CS reconstruction check passed.\n'
else
  printf 'ERROR: original CS reconstruction check failed (exit code %s).\n' \
    "$measurement_cs_original_check_status" >&2
fi
```

Extended Cartesian 3D CS manual output check, after the current input and
destination readiness checks in Section 8 are resolved:

```bash
if "$PYTHON" "$REPO/scripts/check_preparation_pair_3d.py" \
  "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01" reconstruction \
  > "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/reconstruction-check.txt" 2>&1; then
  measurement_cs_extended_reconstruction_check_status=0
else
  measurement_cs_extended_reconstruction_check_status=$?
fi
printf 'Checker exit code: %s\n' "$measurement_cs_extended_reconstruction_check_status" \
  >> "$MEAS_ROOT/cartesian-3d-cs-multichannel/manual-01/reconstruction-check.txt"
if [ "$measurement_cs_extended_reconstruction_check_status" -eq 0 ]; then
  printf 'SUCCESS: extended CS reconstruction check passed.\n'
else
  printf 'ERROR: extended CS reconstruction check failed (exit code %s).\n' \
    "$measurement_cs_extended_reconstruction_check_status" >&2
fi
```

Automated CLI invocations for the first three cases:

```bash
if "$PYTHON" "$REPO/src/bart_workflow.py" \
  --kspace "$HOME/bart-learning/bart-workflow-preparations/generation-01/kspace" \
  --output-directory "$MEAS_ROOT/cartesian-2d/automated-01" \
  --spatial-dimensionality 2 \
  --fft-normalization unitary \
  --bart-executable "$BART" \
  > "$MEAS_ROOT/cartesian-2d/automated-01-workflow.log" 2>&1; then
  measurement_workflow_2d_status=0
else
  measurement_workflow_2d_status=$?
fi
printf 'Workflow exit code: %s\n' "$measurement_workflow_2d_status" \
  >> "$MEAS_ROOT/cartesian-2d/automated-01-workflow.log"
cat "$MEAS_ROOT/cartesian-2d/automated-01-workflow.log"
if [ "$measurement_workflow_2d_status" -eq 0 ]; then
  printf 'SUCCESS: Cartesian 2D workflow completed.\n'
else
  printf 'ERROR: Cartesian 2D workflow failed (exit code %s).\n' \
    "$measurement_workflow_2d_status" >&2
fi
```

```bash
if "$PYTHON" "$REPO/src/bart_workflow.py" \
  --kspace "$HOME/bart-learning/bart-workflow-preparations/generation-3d-01/kspace" \
  --output-directory "$MEAS_ROOT/cartesian-3d/automated-01" \
  --spatial-dimensionality 3 \
  --fft-normalization unitary \
  --bart-executable "$BART" \
  > "$MEAS_ROOT/cartesian-3d/automated-01-workflow.log" 2>&1; then
  measurement_workflow_3d_status=0
else
  measurement_workflow_3d_status=$?
fi
printf 'Workflow exit code: %s\n' "$measurement_workflow_3d_status" \
  >> "$MEAS_ROOT/cartesian-3d/automated-01-workflow.log"
cat "$MEAS_ROOT/cartesian-3d/automated-01-workflow.log"
if [ "$measurement_workflow_3d_status" -eq 0 ]; then
  printf 'SUCCESS: Cartesian 3D workflow completed.\n'
else
  printf 'ERROR: Cartesian 3D workflow failed (exit code %s).\n' \
    "$measurement_workflow_3d_status" >&2
fi
```

```bash
if "$PYTHON" "$REPO/src/bart_workflow.py" \
  --kspace "$HOME/bart-learning/bart-workflow-preparations/generation-3d-cs-01/kspace_undersampled" \
  --output-directory "$MEAS_ROOT/cartesian-3d-cs-original/automated-01" \
  --spatial-dimensionality 3 \
  --compressed-sensing \
  --sampling-mask "$HOME/bart-learning/bart-workflow-preparations/generation-3d-cs-01/mask3d" \
  --sensitivities "$HOME/bart-learning/bart-workflow-preparations/generation-3d-cs-01/sensitivities" \
  --reconstruction-profile manual-cartesian-3d-cs \
  --bart-executable "$BART" \
  > "$MEAS_ROOT/cartesian-3d-cs-original/automated-01-workflow.log" 2>&1; then
  measurement_workflow_cs_original_status=0
else
  measurement_workflow_cs_original_status=$?
fi
printf 'Workflow exit code: %s\n' "$measurement_workflow_cs_original_status" \
  >> "$MEAS_ROOT/cartesian-3d-cs-original/automated-01-workflow.log"
cat "$MEAS_ROOT/cartesian-3d-cs-original/automated-01-workflow.log"
if [ "$measurement_workflow_cs_original_status" -eq 0 ]; then
  printf 'SUCCESS: original CS workflow completed.\n'
else
  printf 'ERROR: original CS workflow failed (exit code %s).\n' \
    "$measurement_workflow_cs_original_status" >&2
fi
```

The automated commands above are single workflow invocations. Do not call
`run_reconstruction(...)` to represent a manual run; the manual routes use the
direct BART operations listed above. Each automated CLI's output log and
captured process exit code are part of its predefined invocation block, which
remains one execution intervention. Do not add a separately submitted status
command after observing the outcome. Each workflow block displays a
success/error summary and leaves the terminal session open if it fails; do not
begin a dependent stage after a failed required operation.

## 7. Blank observation and outcome templates

Record one row for each planned action ID in each route. Mark its status as
planned until performed. Leave actual actions, results, exit codes, evidence,
counts, and observations blank beforehand.

| Case | Route | Action ID | Planned action | Action actually performed | Category | Status (planned/executed/not performed) | Result / exit code | Evidence reference | Failure, correction, recovery, or deviation |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

Per-route category totals (leave blank until the route is performed):

| Case | Route | Configuration | Execution | Check or review | Operational evidence recording | Correction | Recovery | Total |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Cartesian 2D | Manual |  |  |  |  |  |  |  |
| Cartesian 2D | Automated |  |  |  |  |  |  |  |
| Cartesian 3D | Manual |  |  |  |  |  |  |  |
| Cartesian 3D | Automated |  |  |  |  |  |  |  |
| Cartesian 3D CS, original single-channel | Manual |  |  |  |  |  |  |  |
| Cartesian 3D CS, original single-channel | Automated |  |  |  |  |  |  |  |
| Cartesian 3D CS, multichannel extended | Manual |  |  |  |  |  |  |  |
| Cartesian 3D CS, multichannel extended | Automated |  |  |  |  |  |  |  |

Per-case comparison summary (leave all values blank until both runs are
complete):

| Case | Manual total, M | Automated total, A | M − A | Percentage when M > 0 |
|---|---:|---:|---:|---:|
| Cartesian 2D |  |  |  |  |
| Cartesian 3D |  |  |  |  |
| Cartesian 3D CS, original single-channel |  |  |  |  |
| Cartesian 3D CS, multichannel extended |  |  |  |  |

Report the percentage as not applicable if `M = 0`. Keep category totals and
failure/correction/recovery records alongside the summary. Do not infer a
reduction or apply a success threshold.

## 8. Readiness and in-run check notes

The input/destination readiness checks remain pending. The manual check blocks
below are documented measured actions, not pre-run checks:

1. **Input and destination presence:** the supplied input paths and their
   current `.hdr`/`.cfl` pairs, the prepared case-parent directories, and the
   absence of each new run leaf and automated sidecar log have not been checked
   here. Confirm before starting; do not infer availability from path names.
2. **Manual multichannel pattern check:** the complete `CSX-M-CHK1` block is
   now documented in Section 6.4. It reads the k-space and generated mask,
   applies the module's shape/binary/omitted-position checks, resolves the
   frozen `ecalib` settings, and checks calibration compatibility before
   `ecalib`. This is a planned measured action, not a result; the historical
   `pattern` evidence in Task 7.6 does not substitute for it.
3. **Manual multichannel sensitivity and eigenvalue check:** the complete
   `CSX-M-CHK2` block is now documented in Section 6.4. It checks the current
   k-space, sensitivities, and eigenvalues using the existing reader and
   validators. It is a planned measured action, not a result, and must be
   completed and reviewed before `pics`.

The new blocks document how to perform the manual checks; they do not establish
that any current input or destination exists, nor that any check has passed.
The first three pairs may proceed only if their prepared inputs, existing
preparation records, and output-check readiness are confirmed. If any required
input or destination is unavailable, record preparation as pending and stop
the affected route without substituting another input or treating missing
evidence as success.
