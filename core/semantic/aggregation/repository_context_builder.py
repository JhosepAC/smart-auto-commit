from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
)


class RepositoryContextBuilder:
    """
    Build repository AI context.
    """

    def build(
        self,
        analyses: list[ASTAnalysisResult],
    ) -> str:
        """
        Build repository semantic context.
        """

        lines = []

        lines.append((f"Files analyzed: " f"{len(analyses)}"))

        total_functions = sum(len(analysis.functions) for analysis in analyses)

        total_classes = sum(len(analysis.classes) for analysis in analyses)

        lines.append((f"Functions: " f"{total_functions}"))

        lines.append((f"Classes: " f"{total_classes}"))

        frameworks = set()

        for analysis in analyses:
            frameworks.update(analysis.detected_frameworks)

        if frameworks:
            lines.append(("Frameworks: " + ", ".join(sorted(frameworks))))

        return "\n".join(lines)
