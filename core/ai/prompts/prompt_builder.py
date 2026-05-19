from core.ai.prompts.prompt_templates import (
    COMMIT_GENERATION_TEMPLATE,
)

from core.ai.prompts.semantic_prompt_enricher import (
    SemanticPromptEnricher,
)

from core.semantic.ast.ast_models import (
    IntelligentCommit,
    SemanticIntentProfile,
)


class PromptBuilder:
    """
    Build AI prompts.
    """

    def __init__(
        self,
    ) -> None:
        self.enricher = SemanticPromptEnricher()

    def build_commit_prompt(
        self,
        intelligent_commit: IntelligentCommit,
        intent: SemanticIntentProfile,
    ) -> str:
        """
        Build semantic AI prompt.
        """

        prompt = COMMIT_GENERATION_TEMPLATE.format(
            semantic_context=(intelligent_commit.semantic_context),
            intent_context=(intent.ai_intent_context),
            commit_context=(intelligent_commit.full_message),
        )

        return self.enricher.enrich(prompt)
