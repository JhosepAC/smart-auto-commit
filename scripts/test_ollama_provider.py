from core.ai.models.ai_request import (
    AIRequest,
)
from core.ai.services.ai_orchestrator import (
    AIOrchestrator,
)


def main() -> None:
    orchestrator = AIOrchestrator()

    request = AIRequest(
        prompt=(
            "Generate a professional "
            "conventional commit "
            "for implementing "
            "AI orchestration pipeline"
        ),
        temperature=0.2,
        max_tokens=100,
    )

    response = orchestrator.generate(
        "ollama",
        request,
    )

    print()

    print("Ollama Provider")

    print("----------------")

    print()

    print(f"Success: " f"{response.success}")

    print(f"Provider: " f"{response.provider}")

    print()

    print("Generated Commit:")

    print(response.content)

    print()


if __name__ == "__main__":
    main()
