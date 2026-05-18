from dataclasses import dataclass


@dataclass(slots=True)
class AIResponse:
    """
    Represent AI provider response.
    """

    success: bool

    content: str

    provider: str

    tokens_used: int

    error: str | None
