import subprocess
from pathlib import Path

from core.git.commit_quality_validator import (
    CommitQualityValidator,
)
from core.git.conventional_commit_generator import (
    ConventionalCommitGenerator,
)
from core.git.models import (
    CommitExecutionResult,
)

from core.git.smart_staging_engine import (
    SmartStagingEngine,
)

from core.git.repository_safety_guard import (
    RepositorySafetyGuard,
)

from core.logging.logger import logger


class CommitExecutionEngine:
    """
    Execute Git commits safely.
    """

    def __init__(
        self,
        repository_path: str | Path,
    ) -> None:
        self.repository_path = Path(repository_path).resolve()

        self.generator = ConventionalCommitGenerator(self.repository_path)

        self.validator = CommitQualityValidator(self.repository_path)

        self.staging_engine = SmartStagingEngine(self.repository_path)

        self.safety_guard = RepositorySafetyGuard(self.repository_path)

    def execute_commit(
        self,
        dry_run: bool = True,
    ) -> CommitExecutionResult:
        """
        Execute Git commit safely.
        """

        logger.info(("Starting commit execution " f"(dry_run={dry_run})"))

        safety_report = self.safety_guard.validate_repository_safety()

        if not safety_report.safe:
            logger.warning("Repository safety validation failed")

            return CommitExecutionResult(
                success=False,
                commit_message="",
                commit_hash=None,
                stdout="",
                stderr=("Repository safety validation " "failed"),
                dry_run=dry_run,
            )

        validation_report = self.validator.validate_commit()

        if not validation_report.is_valid:
            logger.warning("Commit validation failed")

            return CommitExecutionResult(
                success=False,
                commit_message="",
                commit_hash=None,
                stdout="",
                stderr=("Commit quality validation " "failed"),
                dry_run=dry_run,
            )

        generated_commit = self.generator.generate_commit()

        commit_message = generated_commit.full_message

        if dry_run:
            logger.info("Dry-run commit execution completed")

            return CommitExecutionResult(
                success=True,
                commit_message=(commit_message),
                commit_hash=None,
                stdout=("Dry-run successful"),
                stderr="",
                dry_run=True,
            )

        self._stage_allowed_files()

        result = subprocess.run(
            [
                "git",
                "commit",
                "-m",
                commit_message,
            ],
            cwd=self.repository_path,
            capture_output=True,
            text=True,
            check=False,
        )

        success = result.returncode == 0

        commit_hash = None

        if success:
            commit_hash = self._get_last_commit_hash()

            logger.info(("Commit executed " f"successfully: " f"{commit_hash}"))

        else:
            logger.error("Commit execution failed")

        return CommitExecutionResult(
            success=success,
            commit_message=commit_message,
            commit_hash=commit_hash,
            stdout=result.stdout,
            stderr=result.stderr,
            dry_run=False,
        )

    def _stage_allowed_files(
        self,
    ) -> None:
        """
        Stage only allowed files.
        """

        allowed_files = self.staging_engine.stage_allowed_files()

        logger.info((f"Staging " f"{len(allowed_files)} " f"allowed files"))

        for file_path in allowed_files:
            subprocess.run(
                [
                    "git",
                    "add",
                    file_path,
                ],
                cwd=self.repository_path,
                capture_output=True,
                text=True,
                check=False,
            )

    def _get_last_commit_hash(
        self,
    ) -> str:
        """
        Get latest commit hash.
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
