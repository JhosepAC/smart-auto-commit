from core.semantic.ast.ast_models import (
    RepositorySemanticContext,
)


class SemanticHistoryTracker:
    """
    Track repository semantic history.
    """

    def build_history(
        self,
        contexts: list[RepositorySemanticContext],
    ) -> dict[str, dict[str, int]]:
        """
        Build semantic history.
        """

        commit_types: dict[str, int] = {}

        components: dict[str, int] = {}

        for context in contexts:
            commit_type = context.dominant_commit_type

            commit_types[commit_type] = commit_types.get(commit_type, 0) + 1

            for component in context.impacted_components:
                components[component] = components.get(component, 0) + 1

        return {
            "commit_types": commit_types,
            "components": components,
        }
