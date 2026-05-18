from core.ai.interfaces.prompt_builder import (
    PromptBuilderInterface,
)
from core.ai.models.prompt_context import (
    PromptContext,
)
from core.ai.prompts.prompt_templates import (
    COMMIT_GENERATION_TEMPLATE,
)


class CommitGenerationPromptBuilder(
    PromptBuilderInterface,
):
    """
    Build commit generation prompts.
    """

    def build_prompt(
        self,
        context: PromptContext,
    ) -> str:
        changed_files = "\n".join(context.changed_files)

        return COMMIT_GENERATION_TEMPLATE.format(
            repository_name=(context.repository_name),
            branch_name=(context.branch_name),
            semantic_type=(context.semantic_type),
            changed_files=(changed_files),
            commit_summary=(context.commit_summary),
        )
