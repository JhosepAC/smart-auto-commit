from core.ai.models.ai_request import (
    AIRequest,
)
from core.ai.models.ai_response import (
    AIResponse,
)
from core.ai.providers.provider_registry import (
    ProviderRegistry,
)


class AIOrchestrator:
    """
    Coordinate AI providers.
    """

    def __init__(
        self,
    ) -> None:
        self.registry = ProviderRegistry()

    def generate(
        self,
        provider_name: str,
        request: AIRequest,
    ) -> AIResponse:
        """
        Generate AI response.
        """

        provider = self.registry.get_provider(provider_name)

        return provider.generate_response(request)
