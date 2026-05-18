from abc import (
    ABC,
    abstractmethod,
)

from core.ai.models.prompt_context import (
    PromptContext,
)


class PromptBuilderInterface(
    ABC,
):
    """
    Prompt builder contract.
    """

    @abstractmethod
    def build_prompt(
        self,
        context: PromptContext,
    ) -> str:
        """
        Build AI prompt.
        """
