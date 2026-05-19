from core.semantic.ast.ast_models import (
    RepositorySemanticContext,
)


class ArchitecturalIntentAnalyzer:
    """
    Analyze architectural intentions.
    """

    def analyze(
        self,
        context: RepositorySemanticContext,
    ) -> str:
        """
        Analyze repository architecture intent.
        """

        components = context.impacted_components

        if "service" in components:
            return "service layer expansion"

        if "parser" in components:
            return "semantic parsing evolution"

        if "controller" in components:
            return "API layer evolution"

        return "general architectural maintenance"
