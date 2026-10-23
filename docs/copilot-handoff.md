# Copilot Handoff

Copilot is planned for supervised future changes. Creating these notes or
connecting GitHub does not enable Copilot or authorize access to restricted data.
No editor/Copilot integration has yet been confirmed for this project.

Open only the reviewed project folder, not the home directory, laboratory storage,
upstream BART tree or a multi-root workspace containing restricted material. Give
specific context documents to the agent. Repository instructions are available at
`.github/copilot-instructions.md` on supported surfaces; confirm they are enabled.
Do not assume every repository file is automatically read in a particular response.

Local editor assistance uses the provided workspace. A hosted agent uses its
provided repository/execution environment, not automatically the Mac. Do not
assume BART, dependencies or local synthetic files are installed remotely.

## Suggested initial request

```text
Read README.md, docs/project-context.md, docs/open-questions.md,
docs/data-and-ai-boundaries.md, environment/local-macos.md, and
tests/synthetic_2d/README.md.

Do not edit files or run commands yet. Summarize observed evidence,
implemented and unimplemented work, and the data boundary. Identify missing
files needed to reproduce the existing exercise. Propose one small next
change and how I should verify it. Keep committed content in English;
explain the plan to me in Spanish. Do not access files outside this project
or laboratory data, images, extraction code, storage, TALC or credentials.
```

After a clean initial commit, use a dedicated branch for a bounded change. Review
the diff, run authorized synthetic checks, record outcomes and update `AI_USE.md`
before committing/pushing. Preserve historical logs; humans approve evaluation
criteria and data decisions.

Instructions are not enforced access controls. A terminal-enabled agent may reach
outside the opened folder depending on permissions. Review execution approvals and
available isolation before enabling it. Keep automatic approval off and do not
supply restricted files. A private GitHub repository does not override these limits.

The 2026-10-23 assembly checkpoint confirms that both scripts and the selected
text/dependency records appear in the staged listing. SSH authentication and the
destination address are established by Ricardo's reports; initial publication is
not yet evidenced by this checkpoint. Review current Git history before treating
commit or connection tasks as still pending.

Next priorities are documentation review, initial publication and reproduction
from recorded code. Then plan input validation and the 3D Cartesian recipe using
a non-sensitive input contract, not guessed experimental metadata.
