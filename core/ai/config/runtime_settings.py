from dataclasses import dataclass


@dataclass(slots=True)
class RuntimeAISettings:
    """
    Represent runtime AI settings.
    """

    default_provider: str

    fallback_provider: str

    dry_run_enabled: bool

    prompt_version: str
