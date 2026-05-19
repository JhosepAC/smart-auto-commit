from core.semantic.ast.ast_models import (
    ArchitecturalComponent,
    SemanticRelationship,
)


class RelationshipMapper:
    """
    Map semantic relationships.
    """

    def map_relationships(
        self,
        components: list[ArchitecturalComponent],
    ) -> list[SemanticRelationship]:
        """
        Build architectural relationships.
        """

        relationships = []

        services = [
            component
            for component in components
            if (component.component_type == "service")
        ]

        repositories = [
            component
            for component in components
            if (component.component_type == "repository")
        ]

        for service in services:
            for repository in repositories:
                relationships.append(
                    SemanticRelationship(
                        source=service.name,
                        target=repository.name,
                        relationship_type=("service_repository"),
                    )
                )

        return relationships
