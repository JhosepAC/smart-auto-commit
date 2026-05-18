from core.bootstrap.application import Application
from core.logging.logger import logger


def start_command() -> None:
    """
    Start Smart Auto Commit application.
    """

    logger.info("Starting Smart Auto Commit runtime")

    application = Application()

    application.bootstrap()

    logger.info("Smart Auto Commit runtime started successfully")
