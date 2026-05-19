from core.semantic.ast.ast_models import (
    SemanticIntentProfile,
)


class CommitReasoningEngine:
    """
    Build technical commit reasoning.
    """

    def build(
        self,
        intent: SemanticIntentProfile,
    ) -> list[str]:
        """
        Generate technical reasoning.
        """

        reasoning = []

        reasoning.append(("Improves semantic " "repository understanding"))

        reasoning.append(("Expands AI contextual " "reasoning capabilities"))

        reasoning.append(("Strengthens architectural " "semantic analysis"))

        if intent.primary_intent == "architectural refactoring":
            reasoning.append(("Reduces future " "maintenance complexity"))

        return reasoning
