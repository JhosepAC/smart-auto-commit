from core.semantic.ast.ast_models import (
    SemanticDependency,
)


class CouplingDetector:
    """
    Detect architectural coupling.
    """

    def calculate_score(
        self,
        dependencies: list[SemanticDependency],
    ) -> int:
        """
        Calculate coupling score.
        """

        unique_targets = {dependency.target_module for dependency in dependencies}

        dependency_count = len(unique_targets)

        if dependency_count >= 15:
            return 10

        if dependency_count >= 10:
            return 8

        if dependency_count >= 5:
            return 5

        if dependency_count >= 3:
            return 3

        return 1
