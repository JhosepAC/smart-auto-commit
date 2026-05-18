from pathlib import Path

from core.git.commit_context_builder import (
    CommitContextBuilder,
)
from core.git.models import (
    SemanticClassification,
)
from core.logging.logger import logger


class SemanticChangeClassifier:
    """
    Classify repository changes semantically.
    """

    FEATURE_KEYWORDS = {
        "feature",
        "add",
        "implement",
        "create",
        "introduce",
    }

    FIX_KEYWORDS = {
        "fix",
        "bug",
        "resolve",
        "correct",
        "patch",
    }

    REFACTOR_KEYWORDS = {
        "refactor",
        "cleanup",
        "optimize",
        "improve",
    }

    TEST_KEYWORDS = {
        "test",
        "spec",
    }

    DOCS_EXTENSIONS = {
        ".md",
        ".rst",
        ".txt",
    }

    CONFIG_EXTENSIONS = {
        ".json",
        ".yml",
        ".yaml",
        ".toml",
        ".ini",
    }

    def __init__(
        self,
        repository_path: str | Path,
    ) -> None:
        self.context_builder = CommitContextBuilder(repository_path)

    def classify_changes(
        self,
    ) -> SemanticClassification:
        """
        Classify repository changes.
        """

        logger.info("Classifying semantic changes")

        context = self.context_builder.build_context()

        commit_type = "chore"

        confidence_score = 0.5

        detected_patterns = []

        reasoning = "Default repository maintenance"

        languages = context.impacted_languages

        categories = context.impacted_categories

        if "documentation" in categories:
            commit_type = "docs"

            confidence_score = 0.9

            detected_patterns.append("documentation_changes")

            reasoning = "Documentation files detected"

        elif "configuration" in categories:
            commit_type = "chore"

            confidence_score = 0.8

            detected_patterns.append("configuration_changes")

            reasoning = "Configuration files detected"

        elif "source_code" in categories:
            commit_type = self._classify_code_changes(context.summary)

            confidence_score = 0.85

            detected_patterns.append("source_code_changes")

            reasoning = "Source code modifications detected"

        if any("test" in language.lower() for language in languages):
            commit_type = "test"

            confidence_score = 0.95

            detected_patterns.append("test_related_changes")

            reasoning = "Testing-related changes detected"

        classification = SemanticClassification(
            commit_type=commit_type,
            confidence_score=(confidence_score),
            detected_patterns=(detected_patterns),
            reasoning=reasoning,
        )

        logger.info(("Semantic classification " f"completed: {commit_type}"))

        return classification

    def _classify_code_changes(
        self,
        summary: str,
    ) -> str:
        """
        Classify source code changes.
        """

        normalized_summary = summary.lower()

        for keyword in self.FEATURE_KEYWORDS:
            if keyword in normalized_summary:
                return "feat"

        for keyword in self.FIX_KEYWORDS:
            if keyword in normalized_summary:
                return "fix"

        for keyword in self.REFACTOR_KEYWORDS:
            if keyword in normalized_summary:
                return "refactor"

        for keyword in self.TEST_KEYWORDS:
            if keyword in normalized_summary:
                return "test"

        return "feat"
