from core.ai.models.ai_request import (
    AIRequest,
)
from core.ai.models.ai_response import (
    AIResponse,
)
from core.ai.providers.base_provider import (
    BaseAIProvider,
)


class MockAIProvider(
    BaseAIProvider,
):
    """
    Mock AI provider for testing.
    """

    provider_name = "mock"

    def generate_response(
        self,
        request: AIRequest,
    ) -> AIResponse:
        return AIResponse(
            success=True,
            content=("feat(core): " "implement intelligent " "commit analysis"),
            provider=self.provider_name,
            tokens_used=42,
            error=None,
        )
