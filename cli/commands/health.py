import typer

from core.container.app_container import AppContainer


def health_command() -> None:
    """
    Validate application health.
    """

    container = AppContainer()

    health_service = container.services.health_service()

    health = health_service.check_health()

    typer.echo("")

    typer.secho(
        "Application Health Status",
        fg=typer.colors.GREEN,
        bold=True,
    )

    typer.echo("-------------------------")

    for key, value in health.items():
        typer.echo(f"{key}: {value}")

    typer.echo("")
