from pathlib import Path

from core.git.commit_context_builder import (
    CommitContextBuilder,
)
from core.git.models import (
    GeneratedCommit,
)
from core.git.semantic_change_classifier import (
    SemanticChangeClassifier,
)
from core.logging.logger import logger


class ConventionalCommitGenerator:
    """
    Generate conventional commits automatically.
    """

    def __init__(
        self,
        repository_path: str | Path,
    ) -> None:
        self.repository_path = Path(repository_path).resolve()

        self.context_builder = CommitContextBuilder(self.repository_path)

        self.classifier = SemanticChangeClassifier(self.repository_path)

    def generate_commit(
        self,
    ) -> GeneratedCommit:
        """
        Generate conventional commit.
        """

        logger.info("Generating conventional commit")

        context = self.context_builder.build_context()

        classification = self.classifier.classify_changes()

        scope = self._detect_scope(context)

        title = self._generate_title(
            classification.commit_type,
            context,
        )

        full_message = f"{classification.commit_type}" f"({scope}): " f"{title}"

        generated_commit = GeneratedCommit(
            commit_type=(classification.commit_type),
            scope=scope,
            title=title,
            full_message=(full_message),
        )

        logger.info(("Conventional commit " f"generated: " f"{full_message}"))

        return generated_commit

    def _detect_scope(
        self,
        context,
    ) -> str:
        """
        Detect commit scope.
        """

        categories = context.impacted_categories

        languages = context.impacted_languages

        if "documentation" in categories:
            return "docs"

        if "configuration" in categories:
            return "config"

        if "Python" in languages:
            return "core"

        return "general"

    def _generate_title(
        self,
        commit_type: str,
        context,
    ) -> str:
        """
        Generate commit title.
        """

        file_count = context.total_files_changed

        if commit_type == "feat":
            return "implement repository " "change analysis improvements"

        if commit_type == "fix":
            return "resolve repository " "analysis issues"

        if commit_type == "docs":
            return "update project " "documentation"

        if commit_type == "refactor":
            return "refactor repository " "analysis architecture"

        if commit_type == "test":
            return "add repository " "analysis tests"

        if file_count == 1:
            return "update repository component"

        return "update repository " "analysis modules"
