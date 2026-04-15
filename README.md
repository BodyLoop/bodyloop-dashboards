# bodyloop-util

This project now exposes a Typer-based CLI.

## Installation guide

### Prerequisites

- [uv](https://docs.astral.sh/uv/)

### One-shot run

You can use `uvx` to run the tool without installing it:

```
uvx --refresh https://github.com/bodyloop/bodyloop-util/archive/refs/heads/main.zip
```

### Install locally

Install the tool with:

```
uv tool install --refresh https://github.com/bodyloop/bodyloop-util/archive/refs/heads/main.zip
```

Run the tool with:

```
bodyloop-util
```

### Creating an editable install

1. Clone the repository.
2. Sync dependencies:

	`uv sync`

3. Run the CLI:

	`uv run bodyloop-util`

## CLI usage

After installing dependencies/syncing the project, run:

- `bodyloop-util`

## Contribution guide

Contributions are welcome.

1. Fork or clone this repository.
2. Create a feature branch.
3. Install dependencies with `uv sync`.
4. Make your changes.
5. Verify the CLI still works, for example:
	- `uv run bodyloop-util`
6. Commit with a clear message and open a pull request.

