from core.ai.models.ai_response import (
    AIResponse,
)


class AIResponseNormalizer:
    """
    Normalize AI responses.
    """

    def normalize(
        self,
        response: AIResponse,
    ) -> AIResponse:
        """
        Normalize AI response content.
        """

        normalized_content = response.content.strip()

        return AIResponse(
            success=response.success,
            content=normalized_content,
            provider=response.provider,
            tokens_used=response.tokens_used,
            error=response.error,
        )
