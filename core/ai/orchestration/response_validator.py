from core.ai.models.ai_response import (
    AIResponse,
)


class AIResponseValidator:
    """
    Validate AI responses.
    """

    MIN_CONTENT_LENGTH = 10

    def validate(
        self,
        response: AIResponse,
    ) -> bool:
        """
        Validate AI response quality.
        """

        if not response.success:
            return False

        if not response.content:
            return False

        if len(response.content.strip()) < self.MIN_CONTENT_LENGTH:
            return False

        return True
