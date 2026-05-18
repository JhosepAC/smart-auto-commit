from pathlib import Path

from core.git.models import (
    RepositorySafetyReport,
)
from core.git.repository_validator import (
    GitRepositoryValidator,
)
from core.git.smart_staging_engine import (
    SmartStagingEngine,
)
from core.git.status_scanner import (
    GitStatusScanner,
)
from core.logging.logger import logger


class RepositorySafetyGuard:
    """
    Validate repository automation safety.
    """

    PROTECTED_BRANCHES = {
        "main",
        "master",
        "production",
        "release",
    }

    MAX_ALLOWED_FILES = 50

    MAX_RISK_SCORE = 70

    def __init__(
        self,
        repository_path: str | Path,
    ) -> None:
        self.repository_path = Path(repository_path).resolve()

        self.validator = GitRepositoryValidator(self.repository_path)

        self.status_scanner = GitStatusScanner(self.repository_path)

        self.staging_engine = SmartStagingEngine(self.repository_path)

    def validate_repository_safety(
        self,
    ) -> RepositorySafetyReport:
        """
        Validate repository safety.
        """

        logger.info("Validating repository safety")

        blocked_reasons = []

        warnings = []

        risk_score = 0

        current_branch = self.validator.get_current_branch()

        repository_status = self.status_scanner.scan_status()

        total_changed_files = (
            len(repository_status.modified_files)
            + len(repository_status.untracked_files)
            + len(repository_status.deleted_files)
        )

        if current_branch in self.PROTECTED_BRANCHES:
            blocked_reasons.append(("Protected branch detected"))

            risk_score += 50

        if total_changed_files > self.MAX_ALLOWED_FILES:
            blocked_reasons.append(("Too many changed files " "detected"))

            risk_score += 30

        staging_result = self.staging_engine.analyze_staging_candidates()

        if staging_result.total_blocked > 0:
            warnings.append(
                (f"{staging_result.total_blocked} " "blocked files detected")
            )

            risk_score += 15

        safe = risk_score < self.MAX_RISK_SCORE

        report = RepositorySafetyReport(
            safe=safe,
            risk_score=risk_score,
            blocked_reasons=blocked_reasons,
            warnings=warnings,
            current_branch=current_branch,
            total_changed_files=(total_changed_files),
        )

        logger.info(
            (
                "Repository safety validation "
                f"completed: "
                f"safe={safe}, "
                f"risk={risk_score}"
            )
        )

        return report
