from core.semantic.ast.ast_models import (
    CriticalModule,
    SemanticDependency,
)


class CriticalModuleDetector:
    """
    Detect critical architectural modules.
    """

    CRITICAL_PATTERNS = {
        "core": "Core system module",
        "auth": "Authentication module",
        "security": "Security module",
        "database": "Database module",
        "config": "Configuration module",
    }

    def detect(
        self,
        dependencies: list[SemanticDependency],
    ) -> list[CriticalModule]:
        """
        Detect critical modules.
        """

        critical_modules = []

        for dependency in dependencies:
            target = dependency.target_module.lower()

            for (
                pattern,
                reason,
            ) in self.CRITICAL_PATTERNS.items():
                if pattern in target:
                    critical_modules.append(
                        CriticalModule(
                            module_name=(dependency.target_module),
                            reason=reason,
                            severity="high",
                        )
                    )

        unique_modules = {}

        for module in critical_modules:
            unique_modules[module.module_name] = module

        return list(unique_modules.values())
