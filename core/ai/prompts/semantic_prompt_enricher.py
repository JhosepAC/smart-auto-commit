from core.ai.prompts.deterministic_prompt_rules import (
    DETERMINISTIC_RULES,
)


class SemanticPromptEnricher:
    """
    Enrich AI prompts.
    """

    def enrich(
        self,
        prompt: str,
    ) -> str:
        """
        Add deterministic AI rules.
        """

        rules = "\n".join(f"- {rule}" for rule in (DETERMINISTIC_RULES))

        return f"{prompt}\n\n" f"Deterministic Rules:\n" f"{rules}"
