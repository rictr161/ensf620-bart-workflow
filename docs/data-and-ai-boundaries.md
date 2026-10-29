# Workspace Separation and Data Handling Notes

## Relationship to the accepted contract

This supporting note explains workspace separation, repository handling and
private processing and retention considerations. The accepted
[ENSF620-BART-DC v0.3.0](DATA_CONTRACT.md) is the primary policy for AI data access
and actions and takes precedence over this note on those subjects. The
[contract decision register](DATA_CONTRACT_DECISIONS.md) records acceptance,
boundary decisions and unresolved access/action questions.

This note does not amend the accepted contract or define the software
specification or evaluation protocol.

## Repository contents and workspace separation

This repository contains project-owned notes and synthetic-example scripts, supplied
synthetic measurements/PNGs, selected environment reports and public-reference links.
Current experimental BART `.cfl`/`.hdr` files and DICOM images are not included.
It does not include the proposal PDFs or institutional identifier. File presence and
reviewed text do not replace a final author review of everything being shared.

The recorded local arrangement separates the following areas:

| Area | Recorded location or boundary | Role |
| --- | --- | --- |
| BART installation | `~/software/bart-1.0.00/` | External BART release source and executable |
| Synthetic practice | `~/bart-learning/` | Original synthetic runs and the practice Python environment |
| Project repository | `~/projects/ensf620-bart-workflow/` | Reviewed project code, notes and shareable evidence |
| Private laboratory environment | Private locations are not listed here | Restricted data, extractor and storage kept outside the AI-accessible workspace |

The paths describe Ricardo's recorded setup. Other installations may use different
locations while maintaining the same separation.

Keep experimental BART files, DICOM images, laboratory measurements, extracted
k-space, derived laboratory images, GE/laboratory extraction code, credentials,
private links and unreviewed logs
outside the shared repository and AI context. Do not link them into the workspace
through symlinks, additional folders or chat attachments. A private repository
is not authorization to disclose restricted material.

## Repository handling and control limitations

`.gitignore` affects routine treatment of untracked files; it is not a read-permission
control, does not remove earlier history and does not restrict an AI service.
Copilot instructions are behavioral guidance, not a sandbox. Opening only this
project reduces unnecessary context, but a command-enabled agent may still access
other locations depending on permissions. Review available isolation, network
access and approvals; do not enable automatic approval or approve private-data access.

Before committing or pushing, inspect the actual staged files. Sharing with the
AI and public release are separate decisions for the intended purpose and audience.
Never force-add laboratory material. Suspected exposure follows the incident
handling described in the accepted contract; deleting a file from the newest
snapshot does not erase Git history.

## Private processing and retention

Ricardo is responsible for handling private inputs and separately initiating
reviewed software in a private environment within the applicable authorizations.
The AI assistant does not initiate or observe that private execution and has no
access to laboratory storage or HPC systems.

Scanner extraction and `.h5` conversion remain outside the current workflow
implementation scope, as described in the [project context](project-context.md).
TALC remains the planned HPC target; ARC is only a possible alternative.
Permitted uses, processing destinations, retention on TrueNAS and deletion of
temporary or student-controlled copies require their applicable confirmations.
These planning references do not establish authorization or retention terms.

The decision register tracks intended use and destination under `Q02`, permitted
sharing and audiences under `Q08`, and retention and deletion conditions under
`Q09`. Unresolved conditions affect the corresponding private operation; reviewed
synthetic development may continue within the accepted boundaries. Shared originals
must not be deleted without prior agreement.
