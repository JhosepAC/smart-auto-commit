from core.semantic.ast.ast_models import (
    CriticalModule,
    ImpactAnalysis,
    SemanticDependency,
)


class ImpactAnalyzer:
    """
    Analyze architectural impact.
    """

    def analyze(
        self,
        dependencies: list[SemanticDependency],
        critical_modules: list[CriticalModule],
        coupling_score: int,
    ) -> ImpactAnalysis:
        """
        Analyze technical impact.
        """

        dependency_count = len(dependencies)

        blast_radius = dependency_count + len(critical_modules)

        impact_score = coupling_score + blast_radius

        if impact_score >= 20:
            criticality = "critical"

        elif impact_score >= 10:
            criticality = "high"

        elif impact_score >= 5:
            criticality = "medium"

        else:
            criticality = "low"

        return ImpactAnalysis(
            impact_score=impact_score,
            coupling_score=coupling_score,
            blast_radius=blast_radius,
            criticality_level=criticality,
        )
