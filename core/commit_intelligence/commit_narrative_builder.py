from core.semantic.ast.ast_models import (
    RepositorySemanticContext,
    SemanticIntentProfile,
)


class CommitNarrativeBuilder:
    """
    Build semantic commit narrative.
    """

    def build(
        self,
        context: RepositorySemanticContext,
        intent: SemanticIntentProfile,
    ) -> str:
        """
        Build commit narrative.
        """

        lines = []

        lines.append(
            (
                "Introduce semantic "
                "repository intelligence "
                "enhancements focused on "
                "advanced repository cognition."
            )
        )

        lines.append("")

        lines.append((f"Primary objective: " f"{intent.semantic_objective}."))

        lines.append((f"Implementation goal: " f"{intent.implementation_goal}."))

        if context.impacted_components:
            lines.append("")

            lines.append("Impacted components:")

            for component in context.impacted_components:
                lines.append(f"- {component}")

        return "\n".join(lines)
