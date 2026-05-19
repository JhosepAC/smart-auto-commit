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
                "core/semantic/services/semantic_analysis_service.py",
            ]
        ),
        build_context(
            [
                "core/semantic/aggregation/semantic_aggregator.py",
            ]
        ),
    ]

    memory_engine = RepositoryMemoryEngine()

    evolution_profile = memory_engine.build_profile(repository_contexts)

    current_context = build_context(
        [
            "core/semantic/intent/intent_engine.py",
            "core/semantic/intent/behavioral_reasoner.py",
        ]
    )

    engine = IntentEngine()

    profile = engine.analyze(
        current_context,
        evolution_profile,
    )

    print()

    print("Advanced Semantic Intent")

    print("-------------------------")

    print()

    print(f"Primary Intent: {profile.primary_intent}")

    print()

    print("Secondary Intent:")

    for item in profile.secondary_intents:
        print(f"- {item}")

    print()

    print(f"Architectural Intention: " f"{profile.architectural_intention}")

    print()

    print(f"Implementation Goal: " f"{profile.implementation_goal}")

    print()

    print(f"Semantic Objective: " f"{profile.semantic_objective}")

    print()

    print("Behavioral Reasoning:")

    for item in profile.behavioral_reasoning:
        print(f"- {item}")

    print()

    print("AI Intent Context:")

    print(profile.ai_intent_context)

    print()


if __name__ == "__main__":
    main()
