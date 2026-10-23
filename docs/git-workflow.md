# Local Git and GitHub Workflow

This is a stepwise guide. Do not run every command blindly or repeat initialization.
At the 2026-10-23 pre-publication checkpoint, local Git is initialized on `main`,
39 files are staged, and SSH authentication succeeded as `rictr161`. Ricardo reports
that `git@github.com:rictr161/ensf620-bart-workflow.git` exists and is empty.
Actual commit/push completion must be checked against subsequent Git output/history.

## Choose the correct history

Local project folder: `~/projects/ensf620-bart-workflow`. Keep it separate from
BART source and the original synthetic runs. Never initialize Git around the home
folder or laboratory storage.

If the course repository already exists with commits, clone that repository and
import these reviewed files without overwriting existing content. Do not create
unrelated history and force-push over it. An initialized but uncommitted local
folder is not yet established project history.

## Populate and initialize

The two executed Python scripts and selected synthetic text/environment records
have been imported and appear in the supplied staged listing. Preserve original
runs and review the copied contents. Do not recursively copy a virtual environment,
laboratory data folder, credentials or unreviewed logs into the project.

For a genuinely new repository:

```bash
git init -b main
git status --short --branch
```

Initialization creates local tracking, not a GitHub repository. No commits yet on
`main` is expected. A Git indicator in the prompt does not mean files are uploading.

## Author identity

These local author settings are not authentication. Replace the email placeholder
with the chosen commit email; obtain the exact noreply email from account settings
if desired, rather than inventing one.

```bash
git config --local user.name "Ricardo Andrés Aguilar Trejo"
git config --local user.email "REPLACE_WITH_YOUR_COMMIT_EMAIL"
```

## Review and first commit

Only after the imported contents and notes have been reviewed:

```bash
git add README.md AI_USE.md .gitignore .github docs environment scripts tests configs src results
git diff --cached --stat
git diff --cached --check
git --no-pager diff --cached
```

Read the selected changes. Then:

```bash
git commit -m "Document macOS familiarization and initial synthetic verification"
git --no-pager log -1 --oneline
```

The initial commit documents earlier work. Do not fabricate dated commits for steps
performed before Git tracking. Keep missing imports/verification explicit.

## GitHub connection — SSH

Use Ricardo's existing SSH key; do not generate another key or install GitHub CLI
for this route. The returned `ssh -T git@github.com` output authenticated `rictr161`.
Never copy private keys or passphrases into the repository. SSH authentication and
commit authorship are separate settings.

The destination already exists. After the first local commit, and only if `origin`
has not been configured, add the supplied SSH address:

```bash
git remote add origin git@github.com:rictr161/ensf620-bart-workflow.git
git remote -v
```

Check both printed URLs. If `origin` already exists, inspect it; do not overwrite
or remove it blindly. Adding a remote records a destination, not an upload.

After reviewing the staged content and confirming the destination, publish:

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

## Later work

From a reviewed clean state:

```bash
git switch -c feature/describe-one-small-change
```

Make bounded changes, inspect diffs, run checks, update AI disclosure and commit.
Push the branch only after review and integrate deliberately. Saving, committing
and pushing are separate actions. Copilot access is another configuration decision.
