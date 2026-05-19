from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
    SemanticContext,
)

from core.semantic.context.ai_context_adapter import (
    AIContextAdapter,
)

from core.semantic.context.architectural_reasoner import (
    ArchitecturalReasoner,
)

from core.semantic.context.context_summarizer import (
    ContextSummarizer,
)

from core.semantic.context.impact_reasoner import (
    ImpactReasoner,
)


class SemanticContextBuilder:
    """
    Build semantic technical context.
    """

    def __init__(
        self,
    ) -> None:
        self.summarizer = ContextSummarizer()

        self.architectural_reasoner = ArchitecturalReasoner()

        self.impact_reasoner = ImpactReasoner()

        self.ai_context_adapter = AIContextAdapter()

    def build(
        self,
        analysis: ASTAnalysisResult,
    ) -> SemanticContext:
        """
        Build semantic context.
        """

        technical_summary = self.summarizer.build_summary(analysis)

        architectural_summary = self.architectural_reasoner.summarize(analysis)

        impact_summary = self.impact_reasoner.summarize(analysis)

        reasoning_chain = self._build_reasoning_chain(analysis)

        ai_context = self.ai_context_adapter.build(analysis)

        return SemanticContext(
            technical_summary=(technical_summary),
            architectural_summary=(architectural_summary),
            impact_summary=(impact_summary),
            reasoning_chain=(reasoning_chain),
            ai_context=(ai_context),
        )

    def _build_reasoning_chain(
        self,
        analysis: ASTAnalysisResult,
    ) -> list[str]:
        """
        Build semantic reasoning chain.
        """

        reasoning = []

        if analysis.endpoints:
            reasoning.append(("Endpoint modifications " "suggest API evolution"))

        if analysis.semantic_dependencies:
            reasoning.append(("Internal dependencies " "indicate architectural impact"))

        if analysis.critical_modules:
            reasoning.append(
                ("Critical modules affected " "requiring careful validation")
            )

        if analysis.heuristic_analysis:
            reasoning.append(
                (
                    "Heuristic engine inferred "
                    f"{analysis.heuristic_analysis.dominant_commit_type} "
                    "semantic intent"
                )
            )

        if not reasoning:
            reasoning.append(("General semantic changes " "detected"))

        return reasoning
