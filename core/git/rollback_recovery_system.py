import subprocess
from pathlib import Path

from core.git.models import (
    RecoveryResult,
    RepositoryCheckpoint,
)
from core.git.repository_validator import (
    GitRepositoryValidator,
)
from core.git.status_scanner import (
    GitStatusScanner,
)
from core.logging.logger import logger


class RollbackRecoverySystem:
    """
    Handle repository rollback recovery.
    """

    def __init__(
        self,
        repository_path: str | Path,
    ) -> None:
        self.repository_path = Path(repository_path).resolve()

        self.validator = GitRepositoryValidator(self.repository_path)

        self.status_scanner = GitStatusScanner(self.repository_path)

    def create_checkpoint(
        self,
    ) -> RepositoryCheckpoint:
        """
        Create repository checkpoint.
        """

        logger.info("Creating repository checkpoint")

        branch = self.validator.get_current_branch()

        head_commit = self._get_head_commit()

        repository_status = self.status_scanner.scan_status()

        staged_files = [file.path for file in (repository_status.staged_files)]

        modified_files = [file.path for file in (repository_status.modified_files)]

        checkpoint = RepositoryCheckpoint(
            branch=branch,
            head_commit=head_commit,
            staged_files=staged_files,
            modified_files=modified_files,
        )

        logger.info(("Repository checkpoint " "created successfully"))

        return checkpoint

    def restore_checkpoint(
        self,
        checkpoint: RepositoryCheckpoint,
    ) -> RecoveryResult:
        """
        Restore repository checkpoint.
        """

        logger.warning("Restoring repository checkpoint")

        reset_result = subprocess.run(
            [
                "git",
                "reset",
                "--mixed",
                checkpoint.head_commit,
            ],
            cwd=self.repository_path,
            capture_output=True,
            text=True,
            check=False,
        )

        success = reset_result.returncode == 0

        if success:
            logger.info(("Repository restored " "successfully"))

        else:
            logger.error("Repository restore failed")

        return RecoveryResult(
            success=success,
            restored_branch=(checkpoint.branch),
            restored_commit=(checkpoint.head_commit),
            stdout=reset_result.stdout,
            stderr=reset_result.stderr,
        )

    def _get_head_commit(
        self,
    ) -> str:
        """
        Get current HEAD commit hash.
        """

        result = subprocess.run(
            [
                "git",
                "rev-parse",
                "HEAD",
            ],
            cwd=self.repository_path,
            capture_output=True,
            text=True,
            check=False,
        )

        return result.stdout.strip()
