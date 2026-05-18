from pathlib import Path
from typing import Any

import yaml

from core.exceptions.base import ConfigurationError


class YAMLLoader:
    """
    Responsible for loading and parsing YAML configuration files.
    """

    @staticmethod
    def load_yaml(file_path: str) -> dict[str, Any]:
        """
        Load and parse a YAML configuration file.

        Args:
            file_path: Path to YAML file

        Returns:
            Parsed YAML content as dictionary

        Raises:
            ConfigurationError: If file does not exist or parsing fails
        """

        path = Path(file_path)

        if not path.exists():
            raise ConfigurationError(f"Configuration file not found: {file_path}")

        try:
            with open(path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)

            return data or {}

        except yaml.YAMLError as error:
            raise ConfigurationError(f"Invalid YAML configuration: {error}") from error

        except Exception as error:
            raise ConfigurationError(
                f"Unexpected error loading configuration: {error}"
            ) from error
