from abc import ABC

from core.ai.interfaces.provider import (
    AIProviderInterface,
)


class BaseAIProvider(
    AIProviderInterface,
    ABC,
):
    """
    Base AI provider.
    """

    provider_name: str
