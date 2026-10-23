# Data, Repository and AI Boundaries

This package contains project-owned notes and synthetic-example scripts, supplied
synthetic measurements/PNGs, selected environment reports and public-reference links.
It does not include the proposal PDFs or institutional identifier. File presence and
reviewed text do not replace a final author review of everything being shared.

## Separation

```text
~/software/bart-1.0.00/           External BART release source/executable
~/bart-learning/                 Original synthetic runs and practice virtual environment
~/projects/ensf620-bart-workflow/ Reviewed project code, notes and shareable evidence
Approved laboratory storage     Restricted data/extractor; not exposed to AI tools
```

Keep laboratory measurements, extracted k-space, derived laboratory images,
GE/laboratory extraction code, credentials, private links and unreviewed logs
outside the shared repository and AI context. Do not link them into the workspace
through symlinks, additional folders or chat attachments. A private repository
is not authorization to disclose restricted material.

## Controls and limitations

`.gitignore` affects routine treatment of untracked files; it is not a read-permission
control, does not remove earlier history and does not restrict an AI service.
Copilot instructions are behavioral guidance, not a sandbox. Opening only this
project reduces unnecessary context, but a command-enabled agent may still access
other locations depending on permissions. Review available isolation, network
access and approvals; do not enable automatic approval or approve private-data access.

Before committing or pushing, inspect the actual staged files. Never force-add
laboratory material. If a secret is committed, stop and follow the course's incident
guidance; deleting it from the newest snapshot does not erase Git history.

## Processing and retention

The proposal assigns laboratory handling and TALC submission to Ricardo and excludes
extraction from the paired comparison. Record permitted uses, approved locations,
retention on TrueNAS and deletion of temporary/student-controlled copies. Do not
infer these terms from this document or delete shared originals without agreement.
