from core.semantic.ast.ast_models import (
    RepositorySemanticContext,
)


class IntelligentScopeDetector:
    """
    Detect semantic commit scope.
    """

    COMPONENT_SCOPE_MAP = {
        "parser": "semantic",
        "service": "core",
        "controller": "api",
        "database": "database",
        "ai": "ai",
        "cli": "cli",
        "watcher": "monitoring",
        "plugin": "plugins",
    }

    def detect(
        self,
        context: RepositorySemanticContext,
    ) -> str:
        """
        Detect semantic scope.
        """

        for component in context.impacted_components:
            normalized = component.lower()

            for (
                keyword,
                scope,
            ) in self.COMPONENT_SCOPE_MAP.items():
                if keyword in normalized:
                    return scope

        return "core"
