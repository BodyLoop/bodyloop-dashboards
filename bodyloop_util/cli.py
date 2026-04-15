import typer
from .sync import web_app as web_app_sync
from .compare import web_app as web_app_compare

cli_app = typer.Typer()

@cli_app.command()
def sync():
    """Syncs probands and results with BodyLoop. Open the web interface to upload an Excel file and sync it with BodyLoop."""
    web_app_sync.run(debug=True, host="0.0.0.0")
    
@cli_app.command()
def compare():
    """Compares viatars"""
    web_app_compare.run(debug=True, host="0.0.0.0")
    
@cli_app.callback(invoke_without_command=True)
def no_command(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())

def main():
    cli_app()

if __name__ == "__main__":
    main()
