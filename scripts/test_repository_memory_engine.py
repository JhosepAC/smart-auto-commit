from core.semantic.aggregation.semantic_aggregator import (
    SemanticAggregator,
)

from core.semantic.memory.repository_memory_engine import (
    RepositoryMemoryEngine,
)

from core.semantic.services.semantic_analysis_service import (
    SemanticAnalysisService,
)

from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
)


def build_context(
    files: list[str],
):
    service = SemanticAnalysisService()

    aggregator = SemanticAggregator()

    analyses: list[ASTAnalysisResult] = []

    for file_path in files:
        analysis = service.analyze_file(file_path)

        if analysis is not None:
            analyses.append(analysis)

    return aggregator.aggregate(analyses)


def main() -> None:
    contexts = [
        build_context(
            [
                "main.py",
                "core/git/diff_engine.py",
            ]
        ),
        build_context(
            [
                "core/semantic/ast/python_parser.py",
                "core/semantic/services/semantic_analysis_service.py",
            ]
        ),
        build_context(
            [
                "core/ai/services/ai_commit_generator.py",
                "core/semantic/context/semantic_context_builder.py",
            ]
        ),
    ]

    engine = RepositoryMemoryEngine()

    profile = engine.build_profile(contexts)

    print()

    print("Repository Evolution Profile")

    print("-----------------------------")

    print()

    print(f"Analyzed Commits: {profile.total_analyzed_commits}")

    print()

    print("Dominant Patterns:")

    for pattern in profile.dominant_patterns:
        print(f"- {pattern}")

    print()

    print("Dominant Components:")

    for component in profile.dominant_components:
        print(f"- {component}")

    print()

    print("Architectural Trends:")

    for trend in profile.architectural_trends:
        print(f"- {trend}")

    print()

    print(f"Activity Score: {profile.repository_activity_score}")

    print()

    print(f"Semantic Maturity: {profile.semantic_maturity}")

    print()

    print("AI Evolution Context:")

    print(profile.ai_evolution_context)

    print()


if __name__ == "__main__":
    main()
