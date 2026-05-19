from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
)


class ArchitecturalReasoner:
    """
    Build architectural reasoning.
    """

    def summarize(
        self,
        analysis: ASTAnalysisResult,
    ) -> str:
        """
        Generate architectural summary.
        """

        components = analysis.architectural_components

        if not components:
            return "No architectural components detected"

        component_types = {component.component_type for component in components}

        return "Architectural components affected: " + ", ".join(
            sorted(component_types)
        )
