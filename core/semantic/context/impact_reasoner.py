from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
)


class ImpactReasoner:
    """
    Generate impact reasoning.
    """

    def summarize(
        self,
        analysis: ASTAnalysisResult,
    ) -> str:
        """
        Build impact summary.
        """

        impact = analysis.impact_analysis

        if not impact:
            return "Impact analysis unavailable"

        return (
            f"Impact level: "
            f"{impact.criticality_level} | "
            f"Coupling score: "
            f"{impact.coupling_score} | "
            f"Blast radius: "
            f"{impact.blast_radius}"
        )
