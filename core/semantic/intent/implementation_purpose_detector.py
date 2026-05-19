from core.semantic.ast.ast_models import (
    RepositorySemanticContext,
)


class ImplementationPurposeDetector:
    """
    Detect implementation objective.
    """

    def detect(
        self,
        context: RepositorySemanticContext,
    ) -> str:
        """
        Detect implementation purpose.
        """

        components = context.impacted_components

        if "service" in components and "parser" in components:
            return "semantic processing enhancement"

        if "database" in components:
            return "data persistence expansion"

        if "controller" in components:
            return "API capability enhancement"

        return "repository capability evolution"
