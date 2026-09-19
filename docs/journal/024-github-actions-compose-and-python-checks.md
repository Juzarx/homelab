# Day 24 - Starting phase 7, compose validation and python checks

**Date:** 2026-09-16

**Objective:** Set up GitHub Actions to validate compose files and lint python scripts

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 23](./023-restart-buttons-and-status-in-control-panel.md)
- [GitHub Actions docs](https://docs.github.com/en/actions)
- [flake8 docs](https://flake8.pycqa.org/)

## Docker compose validation workflow
- Created the `.github/workflows` folder on the repo, on the pc not on any vm, actions run on github's own servers.
- Created the [compose validation workflow](/.github/workflows/validate-compose.yml).
- Workflow finds every docker-compose file in the repo and validates it with `docker compose config -q`, only runs when a compose file changes.
- Pushed and checked the Actions tab, ran correctly against the real compose files.
- Tested it catches real problems on a separate branch, intentionally broke a compose file's indentation, pushed, got a red failed check.
- Deleted the test branch after confirming it worked.

## Python checks workflow
- Created the [python checks workflow](/.github/workflows/python-checks.yml).
- Uses actions/setup-python to install python on the runner, then installs and runs flake8 against the scripts folder.
- Set max line length to 120 instead of flake8's default 79, more realistic for the code already written.
- Pushed and checked what flake8 reports against the existing scripts.
