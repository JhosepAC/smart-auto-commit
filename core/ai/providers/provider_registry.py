from core.ai.interfaces.provider import (
    AIProviderInterface,
)
from core.ai.providers.mock_provider import (
    MockAIProvider,
)

from core.ai.providers.ollama_provider import (
    OllamaProvider,
)


class ProviderRegistry:
    """
    AI provider registry.
    """

    def __init__(
        self,
    ) -> None:
        self.providers = {
            "mock": MockAIProvider(),
            "ollama": OllamaProvider(),
        }

    def get_provider(
        self,
        provider_name: str,
    ) -> AIProviderInterface:
        """
        Retrieve AI provider.
        """

        provider = self.providers.get(provider_name)

        if provider is None:
            raise ValueError(("Provider not found: " f"{provider_name}"))

        return provider
