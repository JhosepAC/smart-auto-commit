from core.semantic.ast.ast_models import (
    ArchitecturalComponent,
    HeuristicMatch,
)


class ArchitectureRules:
    """
    Architecture heuristic rules.
    """

    def analyze(
        self,
        components: list[ArchitecturalComponent],
    ) -> list[HeuristicMatch]:
        """
        Analyze architecture semantics.
        """

        matches = []

        repositories = [
            component
            for component in components
            if (component.component_type == "repository")
        ]

        services = [
            component
            for component in components
            if (component.component_type == "service")
        ]

        if repositories:
            matches.append(
                HeuristicMatch(
                    rule_name=("repository_pattern"),
                    commit_type="feat",
                    confidence=0.75,
                    reason=("Repository layer modified"),
                )
            )

        if services:
            matches.append(
                HeuristicMatch(
                    rule_name="service_layer",
                    commit_type="refactor",
                    confidence=0.65,
                    reason=("Service layer modified"),
                )
            )

        return matches
