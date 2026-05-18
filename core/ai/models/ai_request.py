from dataclasses import dataclass


@dataclass(slots=True)
class AIRequest:
    """
    Represent AI provider request.
    """

    prompt: str

    temperature: float

    max_tokens: int
