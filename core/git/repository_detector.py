from pathlib import Path

from core.git.exceptions import (
    InvalidRepositoryError,
    RepositoryNotFoundError,
)
from core.logging.logger import logger
from core.shared.constants import (
    GIT_DIRECTORY_NAME,
)
from core.utils.filesystem import (
    FileSystemUtils,
)


class GitRepositoryDetector:
    """
    Detect and validate Git repositories.
    """

    def __init__(
        self,
        repository_path: str | Path,
    ) -> None:
        self.repository_path = Path(repository_path).resolve()

        self.git_directory = self.repository_path / GIT_DIRECTORY_NAME

    def repository_exists(self) -> bool:
        """
        Check if repository path exists.
        """

        exists = self.repository_path.exists()

        logger.debug(f"Repository path exists: {exists}")

        return exists

    def is_git_repository(self) -> bool:
        """
        Check if path is a Git repository.
        """

        is_repository = self.git_directory.exists() and self.git_directory.is_dir()

        logger.debug(f"Git repository detected: " f"{is_repository}")

        return is_repository

    def validate_repository(self) -> None:
        """
        Validate repository integrity.
        """

        logger.info("Validating Git repository")

        if not self.repository_exists():
            raise RepositoryNotFoundError(
                ("Repository path does not exist: " f"{self.repository_path}")
            )

        if not self.is_git_repository():
            raise InvalidRepositoryError(("Directory is not a valid " "Git repository"))

        logger.info("Git repository validated successfully")

    def get_repository_path(self) -> Path:
        """
        Return resolved repository path.
        """

        return self.repository_path

    def get_git_directory(self) -> Path:
        """
        Return Git directory path.
        """

        return self.git_directory

    def ensure_repository_structure(self) -> None:
        """
        Validate essential Git structure.
        """

        required_paths = [
            self.git_directory / "HEAD",
            self.git_directory / "config",
        ]

        for path in required_paths:
            if not FileSystemUtils.file_exists(path):
                raise InvalidRepositoryError(
                    ("Invalid Git repository " f"structure: {path}")
                )

        logger.info("Git repository structure validated")
