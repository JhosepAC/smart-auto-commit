from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
)


class GlobalImpactAnalyzer:
    """
    Analyze repository-wide impact.
    """

    def determine_risk(
        self,
        analyses: list[ASTAnalysisResult],
    ) -> str:
        """
        Determine global repository risk.
        """

        impact_scores = []

        for analysis in analyses:
            if analysis.impact_analysis:
                impact_scores.append(analysis.impact_analysis.impact_score)

        if not impact_scores:
            return "low"

        average = sum(impact_scores) / len(impact_scores)

        if average >= 15:
            return "critical"

        if average >= 10:
            return "high"

        if average >= 5:
            return "medium"

        return "low"
