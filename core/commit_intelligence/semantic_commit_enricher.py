from core.semantic.ast.ast_models import (
    RepositorySemanticContext,
    SemanticIntentProfile,
)


class SemanticCommitEnricher:
    """
    Build AI semantic enrichment.
    """

    def enrich(
        self,
        context: RepositorySemanticContext,
        intent: SemanticIntentProfile,
    ) -> str:
        """
        Build semantic enrichment.
        """

        lines = []

        lines.append((f"Commit type: " f"{context.dominant_commit_type}"))

        lines.append((f"Primary intent: " f"{intent.primary_intent}"))

        lines.append((f"Architectural intention: " f"{intent.architectural_intention}"))

        lines.append((f"Semantic objective: " f"{intent.semantic_objective}"))

        return "\n".join(lines)
