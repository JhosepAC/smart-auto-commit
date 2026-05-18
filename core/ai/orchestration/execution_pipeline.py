from core.ai.models.ai_request import (
    AIRequest,
)
from core.ai.models.ai_response import (
    AIResponse,
)
from core.ai.orchestration.fallback_manager import (
    FallbackManager,
)
from core.ai.orchestration.response_normalizer import (
    AIResponseNormalizer,
)
from core.ai.orchestration.response_validator import (
    AIResponseValidator,
)
from core.ai.orchestration.retry_policy import (
    RetryPolicy,
)
from core.ai.providers.provider_registry import (
    ProviderRegistry,
)
from core.logging.logger import logger


class AIExecutionPipeline:
    """
    Execute resilient AI pipeline.
    """

    def __init__(
        self,
    ) -> None:
        self.registry = ProviderRegistry()

        self.validator = AIResponseValidator()

        self.normalizer = AIResponseNormalizer()

        self.retry_policy = RetryPolicy()

        self.fallback_manager = FallbackManager()

    def execute(
        self,
        provider_name: str,
        request: AIRequest,
    ) -> AIResponse:
        """
        Execute resilient AI request.
        """

        logger.info(("Executing AI pipeline " f"with provider: " f"{provider_name}"))

        attempt = 0

        while self.retry_policy.should_retry(attempt):
            attempt += 1

            try:
                provider = self.registry.get_provider(provider_name)

                response = provider.generate_response(request)

                normalized_response = self.normalizer.normalize(response)

                if self.validator.validate(normalized_response):
                    logger.info(("AI pipeline " "completed " "successfully"))

                    return normalized_response

                logger.warning(("Invalid AI response " "detected"))

            except Exception as error:
                logger.exception(("AI provider execution " f"failed: {error}"))

        logger.warning(("Primary provider failed. " "Using fallback provider."))

        fallback_provider = self.fallback_manager.get_fallback_provider()

        provider = self.registry.get_provider(fallback_provider)

        return provider.generate_response(request)
