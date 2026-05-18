import typer

from cli.commands.health import health_command
from cli.commands.start import start_command
from cli.commands.version import version_command

app = typer.Typer(
    help="Smart Auto Commit CLI",
    no_args_is_help=True,
)


# =========================================================
# COMMAND REGISTRATION
# =========================================================

app.command(name="start")(start_command)

app.command(name="health")(health_command)

app.command(name="version")(version_command)
