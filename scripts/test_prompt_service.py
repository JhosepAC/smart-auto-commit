from core.ai.models.prompt_context import (
    PromptContext,
)
from core.ai.services.prompt_service import (
    PromptService,
)


def main() -> None:
    service = PromptService()

    context = PromptContext(
        repository_name=("smart-auto-commit"),
        branch_name=("feature/prompt-system"),
        changed_files=[
            "core/git/models.py",
            "core/ai/services.py",
        ],
        commit_summary=("Added AI prompt architecture"),
        semantic_type="feat",
    )

    prompt = service.build_commit_prompt(context)

    print()

    print("Prompt Service")

    print("--------------")

    print()

    print(prompt)

    print()


if __name__ == "__main__":
    main()
