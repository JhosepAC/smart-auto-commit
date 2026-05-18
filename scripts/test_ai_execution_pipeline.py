from core.ai.models.ai_request import (
    AIRequest,
)
from core.ai.services.ai_orchestrator import (
    AIOrchestrator,
)


def main() -> None:
    orchestrator = AIOrchestrator()

    request = AIRequest(
        prompt=("Generate commit message"),
        temperature=0.2,
        max_tokens=100,
    )

    response = orchestrator.generate(
        "mock",
        request,
    )

    print()

    print("AI Execution Pipeline")

    print("---------------------")

    print()

    print(f"Success: " f"{response.success}")

    print(f"Provider: " f"{response.provider}")

    print(f"Tokens Used: " f"{response.tokens_used}")

    print()

    print("Content:")

    print(response.content)

    print()


if __name__ == "__main__":
    main()
