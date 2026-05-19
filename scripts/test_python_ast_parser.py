from core.semantic.services.semantic_analysis_service import (
    SemanticAnalysisService,
)


def main() -> None:
    service = SemanticAnalysisService()

    result = service.analyze_file("core/ai/services/ai_commit_generator.py")

    if not result:
        print("No semantic result")
        return

    print()
    print("Python AST Analysis")
    print("-------------------")
    print()

    print(f"Language: {result.language}")
    print()

    print("Functions:")

    for function in result.functions:
        print(f"- {function.name} (async={function.is_async})")

    print()
    print("Classes:")

    for class_node in result.classes:
        print(f"- {class_node.name}")

    print()
    print("Frameworks:")

    for framework in result.detected_frameworks:
        print(f"- {framework}")

    print()
    print("Endpoints:")

    for endpoint in result.endpoints:
        print(f"- {endpoint.method} {endpoint.path}")

    print()
    print("Architectural Components:")

    for component in result.architectural_components:
        print(f"- {component.name} ({component.component_type})")

    print()

    print("Dependencies:")

    for dependency in result.semantic_dependencies:
        print(
            (f"- " f"{dependency.source_module} " f"-> " f"{dependency.target_module}")
        )

    print()

    print("Relationships:")

    for relationship in result.semantic_relationships:
        print(
            (
                f"- "
                f"{relationship.source} "
                f"-> "
                f"{relationship.target} "
                f"({relationship.relationship_type})"
            )
        )

    print()

    print("Impact Analysis:")

    if result.impact_analysis:
        print((f"- Impact Score: " f"{result.impact_analysis.impact_score}"))

        print((f"- Coupling Score: " f"{result.impact_analysis.coupling_score}"))

        print((f"- Blast Radius: " f"{result.impact_analysis.blast_radius}"))

        print((f"- Criticality: " f"{result.impact_analysis.criticality_level}"))

    print()

    print("Critical Modules:")

    for module in result.critical_modules:
        print((f"- " f"{module.module_name} " f"({module.severity})"))

    print()

    print("Heuristic Analysis:")

    if result.heuristic_analysis:
        print(
            (f"- Dominant Type: " f"{result.heuristic_analysis.dominant_commit_type}")
        )

        print((f"- Confidence: " f"{result.heuristic_analysis.confidence_score}"))

        print()

        print("Matches:")

        for match in result.heuristic_analysis.matches:
            print(
                (
                    f"- "
                    f"{match.rule_name} "
                    f"-> "
                    f"{match.commit_type} "
                    f"({match.confidence})"
                )
            )

    print()


if __name__ == "__main__":
    main()
