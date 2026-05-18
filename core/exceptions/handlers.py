from core.exceptions.base import ApplicationError
from core.logging.logger import logger


class ExceptionHandler:
    """
    Global exception handler.
    """

    @staticmethod
    def handle(error: Exception) -> None:
        """
        Handle application exceptions.
        """

        if isinstance(error, ApplicationError):
            logger.error(f"Application error: {error}")

        else:
            logger.exception(f"Unexpected error: {error}")
