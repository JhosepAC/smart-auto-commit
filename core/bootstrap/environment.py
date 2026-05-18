import platform
import sys

from core.exceptions.base import ConfigurationError
from core.logging.logger import logger


class EnvironmentValidator:
    """
    Validate runtime environment.
    """

    MINIMUM_PYTHON_VERSION = (3, 12)

    @classmethod
    def validate_python_version(cls) -> None:
        """
        Validate Python runtime version.
        """

        current = sys.version_info[:2]

        if current < cls.MINIMUM_PYTHON_VERSION:
            raise ConfigurationError(
                (
                    "Unsupported Python version. "
                    f"Minimum required: {cls.MINIMUM_PYTHON_VERSION}"
                )
            )

        logger.info(f"Python version validated: {platform.python_version()}")

    @staticmethod
    def validate_operating_system() -> None:
        """
        Validate supported operating system.
        """

        supported_systems = [
            "Windows",
            "Linux",
            "Darwin",
        ]

        current_system = platform.system()

        if current_system not in supported_systems:
            raise ConfigurationError(f"Unsupported operating system: {current_system}")

        logger.info(f"Operating system validated: {current_system}")
