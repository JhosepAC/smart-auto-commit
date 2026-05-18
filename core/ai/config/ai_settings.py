import os

from core.ai.config.provider_settings import (
    ProviderSettings,
)
from core.ai.config.runtime_settings import (
    RuntimeAISettings,
)


class AISettingsManager:
    """
    Manage AI configuration settings.
    """

    def __init__(
        self,
    ) -> None:
        self.runtime_settings = RuntimeAISettings(
            default_provider=(
                os.getenv(
                    "AI_DEFAULT_PROVIDER",
                    "mock",
                )
            ),
            fallback_provider=(
                os.getenv(
                    "AI_FALLBACK_PROVIDER",
                    "mock",
                )
            ),
            dry_run_enabled=(
                os.getenv(
                    "AI_DRY_RUN",
                    "true",
                ).lower()
                == "true"
            ),
            prompt_version=(
                os.getenv(
                    "AI_PROMPT_VERSION",
                    "v1.0.0",
                )
            ),
        )

        self.providers = {
            "mock": ProviderSettings(
                provider_name="mock",
                enabled=True,
                model_name="mock-model",
                temperature=0.2,
                max_tokens=200,
            ),
        }

    def get_provider_settings(
        self,
        provider_name: str,
    ) -> ProviderSettings:
        """
        Retrieve provider settings.
        """

        provider = self.providers.get(provider_name)

        if provider is None:
            raise ValueError(("Provider settings " f"not found: " f"{provider_name}"))

        return provider

    def get_runtime_settings(
        self,
    ) -> RuntimeAISettings:
        """
        Retrieve runtime settings.
        """

        return self.runtime_settings
