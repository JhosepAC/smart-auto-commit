from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
)


class AIContextAdapter:
    """
    Build AI-ready semantic context.
    """

    def build(
        self,
        analysis: ASTAnalysisResult,
    ) -> str:
        """
        Generate AI semantic context.
        """

        lines = []

        lines.append(f"Language: {analysis.language}")

        lines.append((f"Functions: " f"{len(analysis.functions)}"))

        lines.append((f"Classes: " f"{len(analysis.classes)}"))

        lines.append((f"Dependencies: " f"{len(analysis.semantic_dependencies)}"))

        if analysis.heuristic_analysis:
            lines.append(
                (
                    f"Commit Type Hint: "
                    f"{analysis.heuristic_analysis.dominant_commit_type}"
                )
            )

        if analysis.impact_analysis:
            lines.append(
                (f"Criticality: " f"{analysis.impact_analysis.criticality_level}")
            )

        return "\n".join(lines)
