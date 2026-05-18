from pathlib import Path

from core.git.exceptions import (
    DetachedHeadError,
    InvalidGitHeadError,
)
from core.git.repository_detector import (
    GitRepositoryDetector,
)
from core.logging.logger import logger
from core.utils.filesystem import (
    FileSystemUtils,
)


class GitRepositoryValidator:
    """
    Advanced Git repository validator.
    """

    def __init__(
        self,
        repository_path: str | Path,
    ) -> None:
        self.detector = GitRepositoryDetector(repository_path)

        self.detector.validate_repository()

        self.detector.ensure_repository_structure()

        self.git_directory = self.detector.get_git_directory()

    def validate_head(self) -> None:
        """
        Validate Git HEAD file.
        """

        logger.info("Validating Git HEAD")

        head_path = self.git_directory / "HEAD"

        if not FileSystemUtils.file_exists(head_path):
            raise InvalidGitHeadError("Git HEAD file not found")

        head_content = FileSystemUtils.read_text_file(head_path).strip()

        if not head_content:
            raise InvalidGitHeadError("Git HEAD file is empty")

        logger.info("Git HEAD validated successfully")

    def get_current_branch(self) -> str:
        """
        Return current Git branch.
        """

        head_path = self.git_directory / "HEAD"

        head_content = FileSystemUtils.read_text_file(head_path).strip()

        if not head_content.startswith("ref:"):
            raise DetachedHeadError(("Repository is in detached " "HEAD state"))

        reference = head_content.replace(
            "ref: ",
            "",
        )

        branch_name = reference.split("/")[-1]

        logger.info(f"Current Git branch: " f"{branch_name}")

        return branch_name

    def validate_git_config(self) -> None:
        """
        Validate Git configuration file.
        """

        logger.info("Validating Git config")

        config_path = self.git_directory / "config"

        if not FileSystemUtils.file_exists(config_path):
            raise InvalidGitHeadError("Git config file not found")

        logger.info("Git config validated successfully")

    def validate_repository_state(
        self,
    ) -> None:
        """
        Validate repository operational state.
        """

        logger.info("Validating repository state")

        self.validate_head()

        self.validate_git_config()

        branch = self.get_current_branch()

        logger.info(("Repository operational state " f"validated on branch: {branch}"))
