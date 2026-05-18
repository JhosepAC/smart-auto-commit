from pathlib import Path

from core.git.models import (
    SmartStagingResult,
    StagingCandidate,
)
from core.git.status_scanner import (
    GitStatusScanner,
)
from core.logging.logger import logger


class SmartStagingEngine:
    """
    Intelligent staging engine.
    """

    BLOCKED_EXTENSIONS = {
        ".log",
        ".tmp",
        ".cache",
        ".env",
        ".sqlite",
        ".db",
        ".pyc",
    }

    BLOCKED_DIRECTORIES = {
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        "node_modules",
        ".venv",
    }

    SENSITIVE_FILENAMES = {
        ".env",
        ".env.local",
        ".secrets",
    }

    def __init__(
        self,
        repository_path: str | Path,
    ) -> None:
        self.repository_path = Path(repository_path).resolve()

        self.status_scanner = GitStatusScanner(self.repository_path)

    def analyze_staging_candidates(
        self,
    ) -> SmartStagingResult:
        """
        Analyze repository staging files.
        """

        logger.info("Analyzing staging candidates")

        repository_status = self.status_scanner.scan_status()

        allowed_files = []

        blocked_files = []

        for modified_file in repository_status.modified_files:
            candidate = self._evaluate_file(modified_file.path)

            if candidate.allowed:
                allowed_files.append(candidate)

            else:
                blocked_files.append(candidate)

        result = SmartStagingResult(
            allowed_files=allowed_files,
            blocked_files=blocked_files,
            total_allowed=len(allowed_files),
            total_blocked=len(blocked_files),
        )

        logger.info(
            (
                "Smart staging analysis "
                f"completed: "
                f"{result.total_allowed} allowed, "
                f"{result.total_blocked} blocked"
            )
        )

        return result

    def stage_allowed_files(
        self,
    ) -> list[str]:
        """
        Return allowed staging files.
        """

        result = self.analyze_staging_candidates()

        allowed_paths = [candidate.path for candidate in (result.allowed_files)]

        logger.info((f"Allowed staging files: " f"{len(allowed_paths)}"))

        return allowed_paths

    def _evaluate_file(
        self,
        file_path: str,
    ) -> StagingCandidate:
        """
        Evaluate file staging eligibility.
        """

        path = Path(file_path)

        if path.name in self.SENSITIVE_FILENAMES:
            return StagingCandidate(
                path=file_path,
                allowed=False,
                reason=("Sensitive file detected"),
            )

        if path.suffix.lower() in self.BLOCKED_EXTENSIONS:
            return StagingCandidate(
                path=file_path,
                allowed=False,
                reason=("Blocked file extension"),
            )

        for part in path.parts:
            if part in self.BLOCKED_DIRECTORIES:
                return StagingCandidate(
                    path=file_path,
                    allowed=False,
                    reason=("Blocked directory"),
                )

        return StagingCandidate(
            path=file_path,
            allowed=True,
            reason="Allowed",
        )
