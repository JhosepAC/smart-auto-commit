from core.semantic.ast.ast_models import (
    RepositorySemanticContext,
    SemanticIntentProfile,
)


class SemanticTitleGenerator:
    """
    Generate semantic commit titles.
    """

    def generate(
        self,
        context: RepositorySemanticContext,
        intent: SemanticIntentProfile,
    ) -> str:
        """
        Generate intelligent commit title.
        """

        commit_type = context.dominant_commit_type

        if commit_type == "feat":
            return "implement advanced " "semantic analysis capabilities"

        if commit_type == "fix":
            return "resolve semantic " "processing inconsistencies"

        if commit_type == "refactor":
            return "refactor semantic " "processing architecture"

        if commit_type == "perf":
            return "optimize semantic " "analysis performance"

        return "improve repository " "semantic intelligence"
