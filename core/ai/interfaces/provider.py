from abc import (
    ABC,
    abstractmethod,
)

from core.ai.models.ai_request import (
    AIRequest,
)
from core.ai.models.ai_response import (
    AIResponse,
)


class AIProviderInterface(ABC):
    """
    AI provider contract.
    """

    @abstractmethod
    def generate_response(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """
        Generate AI response.
        """
