"""Command-line interface for tinker-uv."""

from __future__ import annotations

import typer

from tinker_uv import __version__

app = typer.Typer(help="Command-line utility for tinker-uv.")


@app.command()
def hello(
    name: str = typer.Argument("world", help="Name to greet."),
) -> None:
    """Print a greeting."""
    typer.echo(f"Hello, {name}!")


@app.command()
def version() -> None:
    """Show the installed CLI version."""
    typer.echo(__version__)


def main() -> None:
    """CLI entrypoint."""
    app()


if __name__ == "__main__":
    main()
