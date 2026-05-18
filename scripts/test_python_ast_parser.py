from core.semantic.services.semantic_analysis_service import (
    SemanticAnalysisService,
)


def main() -> None:
    service = SemanticAnalysisService()

    result = service.analyze_file(("core/ai/services/" "ai_commit_generator.py"))

    if not result:
        print("No semantic result")

        return

    print()

    print("Python AST Analysis")

    print("-------------------")

    print()

    print(f"Language: " f"{result.language}")

    print()

    print("Functions:")

    for function in result.functions:
        print((f"- {function.name} " f"(async={function.is_async})"))

    print()

    print("Classes:")

    for class_node in result.classes:
        print((f"- {class_node.name}"))

    print()

    print("Frameworks:")

    for framework in result.detected_frameworks:
        print(f"- {framework}")

    print()


if __name__ == "__main__":
    main()
