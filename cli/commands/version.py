import typer

from core.shared.constants import (
    APPLICATION_NAME,
    APPLICATION_VERSION,
)


def version_command() -> None:
    """
    Show application version.
    """

    typer.echo("")

    typer.secho(
        (f"{APPLICATION_NAME} " f"v{APPLICATION_VERSION}"),
        fg=typer.colors.GREEN,
        bold=True,
    )

    typer.echo("")
