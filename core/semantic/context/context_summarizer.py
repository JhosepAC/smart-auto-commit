from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
)


class ContextSummarizer:
    """
    Generate semantic summaries.
    """

    def build_summary(
        self,
        analysis: ASTAnalysisResult,
    ) -> str:
        """
        Build technical summary.
        """

        parts = []

        if analysis.functions:
            parts.append((f"{len(analysis.functions)} " f"functions analyzed"))

        if analysis.classes:
            parts.append((f"{len(analysis.classes)} " f"classes detected"))

        if analysis.endpoints:
            parts.append((f"{len(analysis.endpoints)} " f"API endpoints found"))

        if analysis.semantic_dependencies:
            parts.append(
                (f"{len(analysis.semantic_dependencies)} " f"internal dependencies")
            )

        if not parts:
            return "Minor semantic modifications detected"

        return "Semantic analysis detected: " + ", ".join(parts)
