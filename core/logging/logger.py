from pathlib import Path
import sys

from loguru import logger as loguru_logger

from core.config.settings import settings


class LoggerManager:
    """
    Centralized logging manager for the application.
    """

    def __init__(self) -> None:
        self.logs_directory = Path("logs")
        self.logs_directory.mkdir(exist_ok=True)

        self.log_file = settings.logging.file

        self._configure_logger()

    def _configure_logger(self) -> None:
        """
        Configure Loguru logger.
        """

        # Remove default logger
        loguru_logger.remove()

        # Console logger
        loguru_logger.add(
            sys.stdout,
            level=settings.logging.level,
            format=(
                "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
                "<level>{level: <8}</level> | "
                "<cyan>{name}</cyan>:<cyan>{function}</cyan>:"
                "<cyan>{line}</cyan> - "
                "<level>{message}</level>"
            ),
            colorize=True,
        )

        # File logger
        loguru_logger.add(
            self.log_file,
            level=settings.logging.level,
            rotation="10 MB",
            retention="30 days",
            compression="zip",
            encoding="utf-8",
            enqueue=True,
            backtrace=True,
            diagnose=True,
            format=(
                "{time:YYYY-MM-DD HH:mm:ss} | "
                "{level: <8} | "
                "{name}:{function}:{line} - "
                "{message}"
            ),
        )

    @staticmethod
    def get_logger():
        """
        Return configured logger instance.
        """

        return loguru_logger


# =========================================================
# GLOBAL LOGGER INSTANCE
# =========================================================

logger = LoggerManager().get_logger()
