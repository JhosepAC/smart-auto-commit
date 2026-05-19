from core.semantic.ast.ast_models import (
    RepositoryEvolutionProfile,
)


class BehavioralReasoner:
    """
    Infer developer behavioral patterns.
    """

    def reason(
        self,
        profile: RepositoryEvolutionProfile,
    ) -> list[str]:
        """
        Generate developer reasoning.
        """

        reasoning = []

        if "Feature-driven development" in profile.dominant_patterns:
            reasoning.append(("Developer prioritizes " "incremental feature delivery"))

        if "Service layer expansion" in profile.architectural_trends:
            reasoning.append(("Repository evolving " "towards modular services"))

        if profile.semantic_maturity == "advanced":
            reasoning.append(("Repository exhibits " "advanced semantic structure"))

        if not reasoning:
            reasoning.append(("General repository " "evolution detected"))

        return reasoning
