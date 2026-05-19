from collections import Counter

from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
)


class SemanticSynthesizer:
    """
    Synthesize repository semantics.
    """

    def dominant_commit_type(
        self,
        analyses: list[ASTAnalysisResult],
    ) -> str:
        """
        Determine dominant commit type.
        """

        commit_types = []

        for analysis in analyses:
            heuristic = analysis.heuristic_analysis

            if heuristic:
                commit_types.append(heuristic.dominant_commit_type)

        if not commit_types:
            return "chore"

        counts = Counter(commit_types)

        return counts.most_common(1)[0][0]

    def impacted_components(
        self,
        analyses: list[ASTAnalysisResult],
    ) -> list[str]:
        """
        Aggregate impacted components.
        """

        components = set()

        for analysis in analyses:
            for component in analysis.architectural_components:
                components.add(component.component_type)

        return sorted(components)
