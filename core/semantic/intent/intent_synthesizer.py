from core.semantic.ast.ast_models import (
    SemanticIntentProfile,
)


class IntentSynthesizer:
    """
    Build AI intent context.
    """

    def build_context(
        self,
        profile: SemanticIntentProfile,
    ) -> str:
        """
        Build AI intent reasoning context.
        """

        lines = []

        lines.append((f"Primary intent: " f"{profile.primary_intent}"))

        lines.append(
            (f"Architectural intention: " f"{profile.architectural_intention}")
        )

        lines.append((f"Implementation goal: " f"{profile.implementation_goal}"))

        lines.append((f"Semantic objective: " f"{profile.semantic_objective}"))

        if profile.behavioral_reasoning:
            lines.append("Behavioral reasoning:")

            for item in profile.behavioral_reasoning:
                lines.append(f"- {item}")

        return "\n".join(lines)
