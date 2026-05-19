from core.semantic.aggregation.cross_file_reasoner import (
    CrossFileReasoner,
)

from core.semantic.aggregation.global_impact_analyzer import (
    GlobalImpactAnalyzer,
)

from core.semantic.aggregation.repository_context_builder import (
    RepositoryContextBuilder,
)

from core.semantic.aggregation.semantic_synthesizer import (
    SemanticSynthesizer,
)

from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
    RepositorySemanticContext,
)


class SemanticAggregator:
    """
    Aggregate repository semantic analysis.
    """

    def __init__(
        self,
    ) -> None:
        self.synthesizer = SemanticSynthesizer()

        self.reasoner = CrossFileReasoner()

        self.impact_analyzer = GlobalImpactAnalyzer()

        self.repository_builder = RepositoryContextBuilder()

    def aggregate(
        self,
        analyses: list[ASTAnalysisResult],
    ) -> RepositorySemanticContext:
        """
        Aggregate semantic analyses.
        """

        dominant_commit_type = self.synthesizer.dominant_commit_type(analyses)

        impacted_components = self.synthesizer.impacted_components(analyses)

        reasoning_chain = self.reasoner.build_reasoning(analyses)

        global_risk_level = self.impact_analyzer.determine_risk(analyses)

        ai_repository_context = self.repository_builder.build(analyses)

        repository_summary = self._build_summary(analyses)

        architectural_summary = self._build_architecture(impacted_components)

        return RepositorySemanticContext(
            total_files=len(analyses),
            dominant_commit_type=(dominant_commit_type),
            architectural_summary=(architectural_summary),
            repository_summary=(repository_summary),
            impacted_components=(impacted_components),
            reasoning_chain=(reasoning_chain),
            global_risk_level=(global_risk_level),
            ai_repository_context=(ai_repository_context),
        )

    def _build_summary(
        self,
        analyses: list[ASTAnalysisResult],
    ) -> str:
        """
        Build repository summary.
        """

        return (
            f"Repository semantic analysis "
            f"processed {len(analyses)} "
            f"files with aggregated "
            f"architectural reasoning"
        )

    def _build_architecture(
        self,
        components: list[str],
    ) -> str:
        """
        Build architecture summary.
        """

        if not components:
            return "No architectural components detected"

        return "Repository components affected: " + ", ".join(components)
