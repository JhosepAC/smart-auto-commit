from dataclasses import dataclass


@dataclass(slots=True)
class ProviderSettings:
    """
    Represent AI provider settings.
    """

    provider_name: str

    enabled: bool

    model_name: str

    temperature: float

    max_tokens: int
