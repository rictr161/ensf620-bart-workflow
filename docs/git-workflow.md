# Local Git and GitHub Workflow

Use this guide to review and publish changes in an existing local copy of the
ENSF 620 repository. Run the commands from the repository root.

- [Continue on an existing branch](#continue-on-an-existing-branch).
- [Start a separate change on a new branch](#start-a-separate-change-on-a-new-branch).
- [Consult the historical initial setup](#historical-initial-setup).

## Continue on an existing branch

### Inspect the branch and destination

The examples in this section use `planning/ai-dev-tasks`. Use the branch selected
for the task in branch-specific commands.

```bash
git status --short --branch
git remote -v
```

Confirm the intended branch and remote destination. If the intended branch is
already checked out, continue to the change review below. To resume a different
existing branch, first review and resolve the placement of any local changes;
then, from a reviewed clean state, select that branch. For this example:

```bash
git switch planning/ai-dev-tasks
```

### Review and stage the change

Make the intended edits and inspect the changes:

```bash
git diff --stat
git --no-pager diff
```

Complete the verification agreed for the change. Record material AI assistance
and verification actually performed in [AI_USE.md](../AI_USE.md). Stage the
explicit paths included in the reviewed change. The following example selects
this guide; replace that path with the files included in the change:

```bash
git add -- docs/git-workflow.md
git diff --cached --stat
git diff --cached --check
git --no-pager diff --cached
```

Review the complete staged file list and diff, including any files staged
earlier. The staged content is what the next commit will contain.

### Commit and publish the working branch

After reviewing the staged content, create the commit. Use a message that
describes the actual change; this example applies to a Git-guide update:

```bash
git commit -m "docs: clarify Git workflow guidance"
```

After the commit succeeds, publish the same working branch and inspect the
result:

```bash
git push origin planning/ai-dev-tasks
git status --short --branch
git --no-pager log -1 --oneline
```

Review each command's output before proceeding. Unexpected history or a rejected
push requires review; do not force-push or disable checks to bypass an error.

Select the same branch in GitHub when reviewing the published files. Integration
into `main` is a separate reviewed step. Saving, committing and pushing are
separate actions.

Copilot access is a separate configuration decision under the
[accepted AI access/action contract](DATA_CONTRACT.md).

## Start a separate change on a new branch

Create a new branch when starting a separate change. First confirm the intended
starting branch and commit, with a reviewed clean working tree:

```bash
git status --short --branch
git --no-pager log -1 --oneline
```

The new branch starts at the currently checked-out commit. Choose an unused name
that describes the change; replace the example name in both commands below.

```bash
git switch -c feature/describe-one-small-change
```

Make, review and commit the change using the procedure above. For the first
publication of that new branch:

```bash
git push -u origin feature/describe-one-small-change
```

The `-u` option establishes upstream tracking for that branch. For subsequent
sessions on it, use [Continue on an existing branch](#continue-on-an-existing-branch)
with the selected branch name.

## Historical initial setup

At the **2026-10-23 pre-publication checkpoint**, local Git was initialized on
`main`, 39 files were staged, and supplied SSH output authenticated `rictr161`.
Ricardo reported that `git@github.com:rictr161/ensf620-bart-workflow.git` existed
and was empty at that checkpoint.

The following subsections preserve the initial setup guidance. Their command
examples are instructions from that preparation, not evidence that every step
was executed. Later publication evidence is recorded separately in the
[Git questions](open-questions.md#repository-publication-and-review) and
[AI use record](../AI_USE.md). For routine work, use the
[existing-branch procedure](#continue-on-an-existing-branch) above.

### Choose the correct history

Recorded local project folder: `~/projects/ensf620-bart-workflow`. Keep it separate
from BART source and the original synthetic runs. Never initialize Git around the
home folder or laboratory storage.

If the course repository already exists with commits, clone that repository and
import these reviewed files without overwriting existing content. Do not create
unrelated history and force-push over it. An initialized but uncommitted local
folder is not yet established project history.

### Populate and initialize

The initial staged listing included the two executed Python scripts and selected
synthetic text/environment records. The setup guidance called for preserving
original runs and reviewing the copied contents. Do not recursively copy a
virtual environment, laboratory data folder, credentials or unreviewed logs into
the project.

For a genuinely new repository:

```bash
git init -b main
git status --short --branch
```

Initialization creates local tracking, not a GitHub repository. No commits yet on
`main` is expected. A Git indicator in the prompt does not mean files are uploading.

### Initial author identity

The initial guidance used Ricardo's name and a commit-email placeholder below.
These examples do not establish which settings were applied. Local author
settings are not authentication. Replace the email placeholder with the chosen
commit email; obtain the exact noreply email from account settings if desired,
rather than inventing one.

```bash
git config --local user.name "Ricardo Andrés Aguilar Trejo"
git config --local user.email "REPLACE_WITH_YOUR_COMMIT_EMAIL"
```

### Initial import and first commit

The original assembly guidance used the broad staging list below, after review
of the imported contents and notes:

```bash
git add README.md AI_USE.md .gitignore .github docs environment scripts tests configs src results
git diff --cached --stat
git diff --cached --check
git --no-pager diff --cached
```

The initial guidance called for review of the selected changes, followed by a
first commit with this example message:

```bash
git commit -m "Document macOS familiarization and initial synthetic verification"
git --no-pager log -1 --oneline
```

The initial commit documents earlier work. Do not fabricate dated commits for steps
performed before Git tracking. Record any imports or verification that remained
pending at that checkpoint.

### Initial GitHub connection and first publication — SSH

The initial SSH route used Ricardo's existing key and did not require another key
or GitHub CLI. The returned `ssh -T git@github.com` output authenticated `rictr161`.
Never copy private keys or passphrases into the repository. SSH authentication and
commit authorship are separate settings.

Ricardo reported that the destination already existed at the initial checkpoint.
The setup guidance called for adding the supplied SSH address after the first
local commit, and only if `origin` had not been configured:

```bash
git remote add origin git@github.com:rictr161/ensf620-bart-workflow.git
git remote -v
```

Check both printed URLs. If `origin` already exists, inspect it; do not overwrite
or remove it blindly. Adding a remote records a destination, not an upload.

The initial guidance described the first publication of `main` with these
commands, after content review and confirmation of the destination:

```bash
git push -u origin main
git status --short --branch
git --no-pager log -1 --oneline
```

The push sends commits; `-u` establishes upstream tracking for `main`. Saving a file
alone does not publish subsequent changes. Do not use force-push or disable checks
to bypass an error. A nonempty destination or unexpected history requires review.

Repository visibility and reviewer access must be checked separately in GitHub.
A private repository is not permission to upload restricted material. Successful
SSH authentication alone does not prove push permission or successful publication.
