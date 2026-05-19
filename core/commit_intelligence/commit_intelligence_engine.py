from core.commit_intelligence.architectural_impact_writer import (
    ArchitecturalImpactWriter,
)

from core.commit_intelligence.commit_narrative_builder import (
    CommitNarrativeBuilder,
)

from core.commit_intelligence.commit_reasoning_engine import (
    CommitReasoningEngine,
)

from core.commit_intelligence.intelligent_commit_formatter import (
    IntelligentCommitFormatter,
)

from core.commit_intelligence.intelligent_scope_detector import (
    IntelligentScopeDetector,
)

from core.commit_intelligence.semantic_commit_enricher import (
    SemanticCommitEnricher,
)

from core.commit_intelligence.semantic_title_generator import (
    SemanticTitleGenerator,
)

from core.semantic.ast.ast_models import (
    IntelligentCommit,
    RepositorySemanticContext,
    SemanticIntentProfile,
)


class CommitIntelligenceEngine:
    """
    Advanced commit intelligence engine.
    """

    def __init__(
        self,
    ) -> None:
        self.scope_detector = IntelligentScopeDetector()

        self.title_generator = SemanticTitleGenerator()

        self.narrative_builder = CommitNarrativeBuilder()

        self.impact_writer = ArchitecturalImpactWriter()

        self.reasoning_engine = CommitReasoningEngine()

        self.enricher = SemanticCommitEnricher()

        self.formatter = IntelligentCommitFormatter()

    def generate(
        self,
        context: RepositorySemanticContext,
        intent: SemanticIntentProfile,
    ) -> IntelligentCommit:
        """
        Generate intelligent commit.
        """

        scope = self.scope_detector.detect(context)

        title = self.title_generator.generate(
            context,
            intent,
        )

        summary = self.narrative_builder.build(
            context,
            intent,
        )

        architectural_impact = self.impact_writer.generate(intent)

        reasoning = self.reasoning_engine.build(intent)

        semantic_context = self.enricher.enrich(
            context,
            intent,
        )

        commit = IntelligentCommit(
            commit_type=(context.dominant_commit_type),
            scope=scope,
            title=title,
            summary=summary,
            architectural_impact=(architectural_impact),
            technical_reasoning=(reasoning),
            semantic_context=(semantic_context),
            full_message="",
        )

        commit.full_message = self.formatter.format(commit)

        return commit
