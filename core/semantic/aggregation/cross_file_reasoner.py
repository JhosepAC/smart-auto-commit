from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
)


class CrossFileReasoner:
    """
    Build cross-file semantic reasoning.
    """

    def build_reasoning(
        self,
        analyses: list[ASTAnalysisResult],
    ) -> list[str]:
        """
        Generate repository reasoning.
        """

        reasoning = []

        endpoint_count = sum(len(analysis.endpoints) for analysis in analyses)

        dependency_count = sum(
            len(analysis.semantic_dependencies) for analysis in analyses
        )

        if endpoint_count >= 1:
            reasoning.append(("Repository changes " "include API evolution"))

        if dependency_count >= 5:
            reasoning.append(("Multiple internal " "dependencies affected"))

        critical_modules = sum(len(analysis.critical_modules) for analysis in analyses)

        if critical_modules >= 1:
            reasoning.append(("Critical architectural " "modules impacted"))

        if not reasoning:
            reasoning.append(("General repository " "changes detected"))

        return reasoning
