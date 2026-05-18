from core.ai.models.ai_request import (
    AIRequest,
)
from core.ai.models.ai_response import (
    AIResponse,
)
from core.ai.providers.provider_registry import (
    ProviderRegistry,
)

from core.ai.services.prompt_service import (
    PromptService,
)

from core.ai.config.ai_settings import (
    AISettingsManager,
)


class AIOrchestrator:
    """
    Coordinate AI providers.
    """

    def __init__(
        self,
    ) -> None:
        self.registry = ProviderRegistry()
        self.prompt_service = PromptService()
        self.settings_manager = AISettingsManager()

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
