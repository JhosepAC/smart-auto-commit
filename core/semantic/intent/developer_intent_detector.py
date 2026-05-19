from core.semantic.ast.ast_models import (
    RepositorySemanticContext,
)


class DeveloperIntentDetector:
    """
    Detect primary developer intent.
    """

    def detect(
        self,
        context: RepositorySemanticContext,
    ) -> tuple[str, list[str]]:
        """
        Detect semantic developer intent.
        """

        primary = "maintenance"

        secondary = []

        commit_type = context.dominant_commit_type

        if commit_type == "feat":
            primary = "feature implementation"

            secondary.append("repository expansion")

        elif commit_type == "fix":
            primary = "bug resolution"

            secondary.append("stability improvement")

        elif commit_type == "refactor":
            primary = "architectural refactoring"

            secondary.append("code maintainability")

        elif commit_type == "perf":
            primary = "performance optimization"

            secondary.append("runtime improvement")

        if context.global_risk_level in {
            "high",
            "critical",
        }:
            secondary.append("high impact changes")

        return primary, secondary
