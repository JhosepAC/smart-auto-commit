from core.semantic.ast.ast_models import (
    ArchitecturalComponent,
    ASTClass,
)


class ArchitectureDetector:
    """
    Detect architectural patterns.
    """

    COMPONENT_PATTERNS = {
        "service": "service",
        "repository": "repository",
        "controller": "controller",
        "middleware": "middleware",
        "router": "router",
        "manager": "manager",
    }

    def detect(
        self,
        classes: list[ASTClass],
    ) -> list[ArchitecturalComponent]:
        """
        Detect architectural components.
        """

        components = []

        for class_node in classes:
            class_name = class_node.name.lower()

            for (
                pattern,
                component_type,
            ) in self.COMPONENT_PATTERNS.items():
                if pattern in class_name:
                    components.append(
                        ArchitecturalComponent(
                            name=(class_node.name),
                            component_type=(component_type),
                            framework=None,
                            line_number=(class_node.line_number),
                        )
                    )

        return components
