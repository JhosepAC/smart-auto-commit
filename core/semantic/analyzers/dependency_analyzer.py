from core.semantic.ast.ast_models import (
    ASTImport,
    SemanticDependency,
)


class DependencyAnalyzer:
    """
    Analyze semantic dependencies.
    """

    INTERNAL_PREFIXES = {
        "core",
        "cli",
        "config",
        "plugins",
        "tests",
    }

    def analyze(
        self,
        imports: list[ASTImport],
        current_module: str,
    ) -> list[SemanticDependency]:
        """
        Analyze module dependencies.
        """

        dependencies = []

        for imported in imports:
            module_name = imported.module

            if not module_name:
                continue

            root_module = module_name.split(".")[0]

            if root_module not in self.INTERNAL_PREFIXES:
                continue

            dependencies.append(
                SemanticDependency(
                    source_module=(current_module),
                    target_module=(module_name),
                    dependency_type=("internal_import"),
                    line_number=(imported.line_number),
                )
            )

        return dependencies
