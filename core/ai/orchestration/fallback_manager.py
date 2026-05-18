from core.ai.config.ai_settings import (
    AISettingsManager,
)


class FallbackManager:
    """
    Handle provider fallback logic.
    """

    def __init__(
        self,
    ) -> None:
        self.settings_manager = AISettingsManager()

    def get_fallback_provider(
        self,
    ) -> str:
        """
        Retrieve fallback provider.
        """

        runtime_settings = self.settings_manager.get_runtime_settings()

        return runtime_settings.fallback_provider
