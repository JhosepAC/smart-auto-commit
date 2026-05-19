from core.commit_intelligence.commit_intelligence_engine import (
    CommitIntelligenceEngine,
)

from core.semantic.aggregation.semantic_aggregator import (
    SemanticAggregator,
)

from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
)

from core.semantic.intent.intent_engine import (
    IntentEngine,
)

from core.semantic.memory.repository_memory_engine import (
    RepositoryMemoryEngine,
)

from core.semantic.services.semantic_analysis_service import (
    SemanticAnalysisService,
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
    repository_contexts = [
        build_context(
            [
                "core/semantic/ast/python_parser.py",
                "core/semantic/aggregation/semantic_aggregator.py",
            ]
        ),
    ]

    memory_engine = RepositoryMemoryEngine()

    evolution_profile = memory_engine.build_profile(
        repository_contexts,
    )

    current_context = build_context(
        [
            "core/commit_intelligence/commit_intelligence_engine.py",
            "core/commit_intelligence/semantic_title_generator.py",
        ]
    )

    intent_engine = IntentEngine()

    intent_profile = intent_engine.analyze(
        current_context,
        evolution_profile,
    )

    engine = CommitIntelligenceEngine()

    commit = engine.generate(
        current_context,
        intent_profile,
    )

    print()

    print("Advanced Commit Intelligence")

    print("-----------------------------")

    print()

    print(commit.full_message)

    print()

    print("Semantic Context:")

    print(commit.semantic_context)

    print()


if __name__ == "__main__":
    main()
