from core.ai.models.ai_request import (
    AIRequest,
)
from core.ai.models.ai_response import (
    AIResponse,
)
from core.ai.orchestration.execution_pipeline import (
    AIExecutionPipeline,
)
from core.ai.services.prompt_service import (
    PromptService,
)


class AIOrchestrator:
    """
    Coordinate AI execution.
    """

    def __init__(
        self,
    ) -> None:
        self.pipeline = AIExecutionPipeline()

        self.prompt_service = PromptService()

    def generate(
        self,
        provider_name: str,
        request: AIRequest,
    ) -> AIResponse:
        """
        Generate AI response.
        """

        return self.pipeline.execute(
            provider_name,
            request,
        )
