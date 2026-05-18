from core.container.app_container import AppContainer
from core.logging.logger import logger


class Application:
    """
    Main application bootstrap.
    """

    def __init__(self) -> None:
        self.container = AppContainer()

    def bootstrap(self) -> None:
        """
        Bootstrap application.
        """

        logger.info("Bootstrapping Smart Auto Commit")

        health_service = self.container.services.health_service()

        health = health_service.check_health()

        logger.info(f"Application status: {health}")
