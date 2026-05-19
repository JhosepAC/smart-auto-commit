from core.ai.clients.ollama_client import (
    OllamaClient,
)

from core.ai.prompts.prompt_builder import (
    PromptBuilder,
)

from core.ai.validators.ai_response_validator import (
    AIResponseValidator,
)

from core.ai.validators.commit_response_cleaner import (
    CommitResponseCleaner,
)

from core.logging.logger import (
    logger,
)

from core.semantic.ast.ast_models import (
    IntelligentCommit,
    SemanticIntentProfile,
)


class AICommitGenerator:
    """
    Generate AI-enhanced commits.
    """

    def __init__(
        self,
    ) -> None:
        self.client = OllamaClient()

        self.prompt_builder = PromptBuilder()

        self.validator = AIResponseValidator()

        self.cleaner = CommitResponseCleaner()

    def generate(
        self,
        intelligent_commit: IntelligentCommit,
        intent: SemanticIntentProfile,
    ) -> str:
        """
        Generate AI commit.
        """

        logger.info("Generating AI commit")

        prompt = self.prompt_builder.build_commit_prompt(
            intelligent_commit,
            intent,
        )

        response = self.client.generate(prompt)

        response = self.cleaner.clean(response)

        if not self.validator.validate(response):
            logger.warning(("Invalid AI response, " "using fallback"))

            return intelligent_commit.full_message

        logger.info("AI commit generated")

        return response
