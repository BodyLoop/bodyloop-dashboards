# tinker-uv

This project now exposes a Typer-based CLI.

## Installation guide

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

### Install locally

1. Clone the repository.
2. Sync dependencies:

	`uv sync`

3. Run the CLI:

	`uv run tinker-uv --help`

## CLI usage

After installing dependencies/syncing the project, run:

- `tinker-uv --help`
- `tinker-uv hello`
- `tinker-uv hello Aman`
- `tinker-uv version`

If you prefer, you can run commands through uv as well:

- `uv run tinker-uv hello`

## Contribution guide

Contributions are welcome.

1. Fork or clone this repository.
2. Create a feature branch.
3. Install dependencies with `uv sync`.
4. Make your changes.
5. Verify the CLI still works, for example:
	- `uv run tinker-uv --help`
	- `uv run tinker-uv hello`
6. Commit with a clear message and open a pull request.

### Suggested contribution workflow

- Keep changes focused and small.
- Update documentation when behavior changes.
- Add or update tests when introducing new logic.
