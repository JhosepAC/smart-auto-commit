from pathlib import Path

from core.git.diff_engine import (
    GitDiffEngine,
)
from core.git.file_change_analyzer import (
    FileChangeAnalyzer,
)
from core.git.models import (
    CommitContext,
)
from core.logging.logger import logger


class CommitContextBuilder:
    """
    Build semantic commit context.
    """

    def __init__(
        self,
        repository_path: str | Path,
    ) -> None:
        self.repository_path = Path(repository_path).resolve()

        self.diff_engine = GitDiffEngine(self.repository_path)

        self.file_analyzer = FileChangeAnalyzer()

    def build_context(
        self,
    ) -> CommitContext:
        """
        Build repository commit context.
        """

        logger.info("Building commit context")

        diffs = self.diff_engine.get_repository_diff()

        total_files_changed = len(diffs)

        total_additions = sum(diff.additions for diff in diffs)

        total_deletions = sum(diff.deletions for diff in diffs)

        impacted_languages = set()

        impacted_categories = set()

        critical_files = []

        high_importance_files = []

        for diff in diffs:
            analysis = self.file_analyzer.analyze_file(diff.file_path)

            impacted_languages.add(analysis.language)

            impacted_categories.add(analysis.category)

            if analysis.importance_score >= 6:
                high_importance_files.append(analysis.file_path)

            if analysis.importance_score >= 8:
                critical_files.append(analysis.file_path)

        summary = self._build_summary(
            total_files_changed,
            total_additions,
            total_deletions,
        )

        context = CommitContext(
            total_files_changed=(total_files_changed),
            total_additions=(total_additions),
            total_deletions=(total_deletions),
            impacted_languages=sorted(impacted_languages),
            impacted_categories=sorted(impacted_categories),
            critical_files=(critical_files),
            high_importance_files=(high_importance_files),
            summary=summary,
        )

        logger.info("Commit context built successfully")

        return context

    def _build_summary(
        self,
        total_files_changed: int,
        total_additions: int,
        total_deletions: int,
    ) -> str:
        """
        Build semantic repository summary.
        """

        return (
            f"{total_files_changed} files changed, "
            f"{total_additions} additions, "
            f"{total_deletions} deletions"
        )
