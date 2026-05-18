from ollama import chat

from core.ai.models.ai_request import (
    AIRequest,
)
from core.ai.models.ai_response import (
    AIResponse,
)
from core.ai.providers.base_provider import (
    BaseAIProvider,
)
from core.logging.logger import (
    logger,
)


class OllamaProvider(
    BaseAIProvider,
):
    """
    Ollama local AI provider.
    """

    provider_name = "ollama"

    MODEL_NAME = "qwen3:4b"

    def generate_response(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """
        Generate Ollama response.
        """

        logger.info(("Generating response " "using Ollama"))

        try:
            response = chat(
                model=self.MODEL_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": (request.prompt),
                    }
                ],
            )

            content = response["message"]["content"]

            return AIResponse(
                success=True,
                content=content,
                provider=(self.provider_name),
                tokens_used=0,
                error=None,
            )

        except Exception as error:
            logger.exception(("Ollama generation " f"failed: {error}"))

            return AIResponse(
                success=False,
                content="",
                provider=(self.provider_name),
                tokens_used=0,
                error=str(error),
            )
