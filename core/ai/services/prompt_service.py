from core.ai.models.prompt_context import (
    PromptContext,
)
from core.ai.prompts.commit_generation_prompt import (
    CommitGenerationPromptBuilder,
)


class PromptService:
    """
    Manage AI prompts.
    """

    def __init__(
        self,
    ) -> None:
        self.commit_builder = CommitGenerationPromptBuilder()

    def build_commit_prompt(
        self,
        context: PromptContext,
    ) -> str:
        """
        Build commit prompt.
        """

        return self.commit_builder.build_prompt(context)
