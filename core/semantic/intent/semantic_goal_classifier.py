from core.semantic.ast.ast_models import (
    RepositorySemanticContext,
)


class SemanticGoalClassifier:
    """
    Classify semantic repository objective.
    """

    def classify(
        self,
        context: RepositorySemanticContext,
    ) -> str:
        """
        Classify repository semantic goal.
        """

        commit_type = context.dominant_commit_type

        if commit_type == "feat":
            return "repository capability expansion"

        if commit_type == "refactor":
            return "architectural optimization"

        if commit_type == "fix":
            return "repository stabilization"

        if commit_type == "perf":
            return "runtime optimization"

        return "general repository maintenance"
