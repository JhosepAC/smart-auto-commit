from core.ai.models.ai_request import (
    AIRequest,
)
from core.ai.models.prompt_context import (
    PromptContext,
)
from core.ai.services.ai_orchestrator import (
    AIOrchestrator,
)
from core.ai.services.prompt_service import (
    PromptService,
)
from core.git.commit_context_builder import (
    CommitContextBuilder,
)
from core.git.repository_validator import (
    GitRepositoryValidator,
)


class AICommitGenerator:
    """
    Generate AI-powered commits.
    """

    def __init__(
        self,
        repository_path: str,
    ) -> None:
        self.repository_path = repository_path

        self.orchestrator = AIOrchestrator()

        self.prompt_service = PromptService()

        self.context_builder = CommitContextBuilder(repository_path)

        self.validator = GitRepositoryValidator(repository_path)

    def generate_commit(
        self,
    ) -> str:
        """
        Generate intelligent commit.
        """

        context = self.context_builder.build_context()

        branch_name = self.validator.get_current_branch()

        prompt_context = PromptContext(
            repository_name=("smart-auto-commit"),
            branch_name=branch_name,
            changed_files=(context.high_importance_files),
            commit_summary=(context.summary),
            semantic_type="feat",
        )

        prompt = self.prompt_service.build_commit_prompt(prompt_context)

        request = AIRequest(
            prompt=prompt,
            temperature=0.2,
            max_tokens=200,
        )

        response = self.orchestrator.generate(
            "ollama",
            request,
        )

        return response.content
