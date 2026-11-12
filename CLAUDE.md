## Rules

Follow every rule in these files before and while changing code:

@CONTRIBUTING.md
@AGENTS.md

## Where you may work

* This repo is LetsgetDangerousX/Python440, a personal fork of TheAlgorithms/Python used for a CS 440 lab.
* you may read issues on TheAlgorithms/Python.
* Never push to, open a pull request on, or comment on TheAlgorithms/Python.
* All branches and pull requests go on LetsgetDangerousX/Python440

## Rules for a change

* change one algorithm file per pull request
* do not change code and doctests in the same pull request
* do not edit README.md or DIRECTORY.md
* keep existing type hints, docstrings, and doctests
* make the smallest change that resolves the issue

## Checking your work

Run these on the changed file and show me the real output:

* `ruff check <file>`
* `ruff format --check <file>`
* `python -m doctest -v <file>`

Do not say the task is done until all three pass.

## Workflow

1. Read the issue: `gh issue view <number> --repo TheAlgorithms/Python`
2. Explain what is wrong and your planned change. Wait for my OK.
3. Make the change on a new branch named `fix/issue-<number>`.
4. Run the checks above and fix anything that fails.
5. Ask the contributing-reviewer subagent to review the change.
6. Ask me before committing, pushing, or opening the pull request.
