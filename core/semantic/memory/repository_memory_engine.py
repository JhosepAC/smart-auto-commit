from core.semantic.ast.ast_models import (
    RepositoryEvolutionProfile,
    RepositorySemanticContext,
)

from core.semantic.memory.evolution_tracker import (
    EvolutionTracker,
)

from core.semantic.memory.repository_profiler import (
    RepositoryProfiler,
)

from core.semantic.memory.semantic_history_tracker import (
    SemanticHistoryTracker,
)

from core.semantic.memory.semantic_pattern_analyzer import (
    SemanticPatternAnalyzer,
)

from core.semantic.memory.trend_analyzer import (
    TrendAnalyzer,
)


class RepositoryMemoryEngine:
    """
    Repository semantic memory engine.
    """

    def __init__(
        self,
    ) -> None:
        self.history_tracker = SemanticHistoryTracker()

        self.pattern_analyzer = SemanticPatternAnalyzer()

        self.evolution_tracker = EvolutionTracker()

        self.profiler = RepositoryProfiler()

        self.trend_analyzer = TrendAnalyzer()

    def build_profile(
        self,
        contexts: list[RepositorySemanticContext],
    ) -> RepositoryEvolutionProfile:
        """
        Build repository evolution profile.
        """

        history = self.history_tracker.build_history(contexts)

        patterns = self.pattern_analyzer.dominant_patterns(history)

        trends = self.evolution_tracker.architectural_trends(history)

        activity_score = self.trend_analyzer.calculate_activity_score(history)

        maturity = self.profiler.determine_maturity(activity_score)

        ai_context = self.profiler.build_ai_context(
            patterns,
            trends,
        )

        dominant_components = sorted(history["components"].keys())

        return RepositoryEvolutionProfile(
            total_analyzed_commits=(len(contexts)),
            dominant_patterns=(patterns),
            dominant_components=(dominant_components),
            architectural_trends=(trends),
            repository_activity_score=(activity_score),
            semantic_maturity=(maturity),
            ai_evolution_context=(ai_context),
        )
