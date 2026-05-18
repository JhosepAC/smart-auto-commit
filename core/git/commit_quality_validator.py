import re
from pathlib import Path

from core.git.conventional_commit_generator import (
    ConventionalCommitGenerator,
)
from core.git.models import (
    CommitQualityReport,
)
from core.logging.logger import logger


class CommitQualityValidator:
    """
    Validate generated commit quality.
    """

    GENERIC_TERMS = {
        "update",
        "changes",
        "fix stuff",
        "misc",
        "test",
        "temporary",
    }

    CONVENTIONAL_PATTERN = re.compile(
        (r"^(feat|fix|docs|style|" r"refactor|test|chore)" r"\([a-z0-9_-]+\): .+$")
    )

    MIN_TITLE_LENGTH = 15

    def __init__(
        self,
        repository_path: str | Path,
    ) -> None:
        self.generator = ConventionalCommitGenerator(repository_path)

    def validate_commit(
        self,
    ) -> CommitQualityReport:
        """
        Validate generated commit.
        """

        logger.info("Validating commit quality")

        generated_commit = self.generator.generate_commit()

        warnings = []

        suggestions = []

        quality_score = 100

        full_message = generated_commit.full_message

        title = generated_commit.title

        if not (self.CONVENTIONAL_PATTERN.match(full_message)):
            warnings.append(("Commit does not follow " "conventional commit format"))

            quality_score -= 30

        normalized_title = title.lower().strip()

        for term in self.GENERIC_TERMS:
            if term == normalized_title:
                warnings.append(("Generic commit title " "detected"))

                suggestions.append(("Use more descriptive " "commit wording"))

                quality_score -= 25

        if len(title) < self.MIN_TITLE_LENGTH:
            warnings.append("Commit title too short")

            suggestions.append(("Provide more technical " "context"))

            quality_score -= 15

        if generated_commit.scope == "general":
            warnings.append(("Commit scope is too generic"))

            suggestions.append(("Use more specific " "scope detection"))

            quality_score -= 10

        quality_score = max(
            quality_score,
            0,
        )

        is_valid = quality_score >= 70

        report = CommitQualityReport(
            is_valid=is_valid,
            quality_score=quality_score,
            warnings=warnings,
            suggestions=suggestions,
        )

        logger.info(("Commit quality validation " f"completed: {quality_score}"))

        return report
