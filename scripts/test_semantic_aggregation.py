from core.semantic.aggregation.semantic_aggregator import (
    SemanticAggregator,
)

from core.semantic.services.semantic_analysis_service import (
    SemanticAnalysisService,
)

from core.semantic.ast.ast_models import ASTAnalysisResult


def main() -> None:
    service = SemanticAnalysisService()

    aggregator = SemanticAggregator()

    files = [
        "main.py",
        "core/semantic/ast/python_parser.py",
        "core/semantic/context/semantic_context_builder.py",
    ]

    analyses: list[ASTAnalysisResult] = []

    for file_path in files:
        analysis = service.analyze_file(file_path)

        if analysis is not None:
            analyses.append(analysis)

    result = aggregator.aggregate(analyses)

    print()

    print("Repository Semantic Aggregation")

    print("--------------------------------")

    print()

    print(f"Total Files: {result.total_files}")

    print()

    print(f"Dominant Commit Type: {result.dominant_commit_type}")

    print()

    print("Architectural Summary:")

    print(result.architectural_summary)

    print()

    print("Repository Summary:")

    print(result.repository_summary)

    print()

    print("Impacted Components:")

    for component in result.impacted_components:
        print(f"- {component}")

    print()

    print("Reasoning Chain:")

    for item in result.reasoning_chain:
        print(f"- {item}")

    print()

    print(f"Global Risk Level: {result.global_risk_level}")

    print()

    print("AI Repository Context:")

    print(result.ai_repository_context)

    print()


if __name__ == "__main__":
    main()
