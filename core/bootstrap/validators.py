from pathlib import Path

from core.exceptions.base import ConfigurationError
from core.logging.logger import logger


class StartupValidator:
    """
    Validate startup requirements.
    """

    REQUIRED_DIRECTORIES = [
        "logs",
        "config",
        "tests",
    ]

    REQUIRED_FILES = [
        "config/application.yaml",
    ]

    @classmethod
    def validate_directories(cls) -> None:
        """
        Validate required directories.
        """

        for directory in cls.REQUIRED_DIRECTORIES:
            path = Path(directory)

            if not path.exists():
                logger.warning(f"Directory not found. Creating: {directory}")

                path.mkdir(parents=True, exist_ok=True)

        logger.info("Required directories validated")

    @classmethod
    def validate_required_files(cls) -> None:
        """
        Validate required files.
        """

        for file_path in cls.REQUIRED_FILES:
            path = Path(file_path)

            if not path.exists():
                raise ConfigurationError(f"Required file not found: {file_path}")

        logger.info("Required files validated")
