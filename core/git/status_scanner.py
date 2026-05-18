import subprocess
from pathlib import Path

from core.git.models import (
    GitFileStatus,
    GitRepositoryStatus,
)
from core.git.repository_validator import (
    GitRepositoryValidator,
)
from core.logging.logger import logger


class GitStatusScanner:
    """
    Scan Git repository status.
    """

    def __init__(
        self,
        repository_path: str | Path,
    ) -> None:
        self.repository_path = Path(repository_path).resolve()

        self.validator = GitRepositoryValidator(self.repository_path)

        self.validator.validate_repository_state()

    def scan_status(
        self,
    ) -> GitRepositoryStatus:
        """
        Scan Git repository status.
        """

        logger.info("Scanning Git repository status")

        command = [
            "git",
            "status",
            "--short",
        ]

        result = subprocess.run(
            command,
            cwd=self.repository_path,
            capture_output=True,
            text=True,
            check=False,
        )

        output = result.stdout.strip()

        modified_files = []

        staged_files = []

        untracked_files = []

        deleted_files = []

        if not output:
            logger.info("No repository changes detected")

            return GitRepositoryStatus(
                modified_files=[],
                staged_files=[],
                untracked_files=[],
                deleted_files=[],
            )

        for line in output.splitlines():
            index_status = line[0]

            working_tree_status = line[1]

            file_path = line[3:].strip()

            file_status = GitFileStatus(
                path=file_path,
                index_status=index_status,
                working_tree_status=(working_tree_status),
            )

            if index_status == "M" or working_tree_status == "M":
                modified_files.append(file_status)

            if index_status != " ":
                staged_files.append(file_status)

            if index_status == "?" and working_tree_status == "?":
                untracked_files.append(file_status)

            if index_status == "D" or working_tree_status == "D":
                deleted_files.append(file_status)

        logger.info(
            (
                "Git status scan completed: "
                f"{len(modified_files)} modified, "
                f"{len(staged_files)} staged, "
                f"{len(untracked_files)} untracked"
            )
        )

        return GitRepositoryStatus(
            modified_files=modified_files,
            staged_files=staged_files,
            untracked_files=untracked_files,
            deleted_files=deleted_files,
        )
