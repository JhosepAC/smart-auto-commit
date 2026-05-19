from typing import Any

import requests

from core.logging.logger import (
    logger,
)


class OllamaClient:
    """
    Real Ollama local client.
    """

    BASE_URL = "http://localhost:11434"

    DEFAULT_MODEL = "deepseek-coder"

    def generate(
        self,
        prompt: str,
        model: str | None = None,
        temperature: float = 0.1,
    ) -> str:
        """
        Generate AI response.
        """

        logger.info("Generating Ollama response")

        selected_model = model or self.DEFAULT_MODEL

        payload: dict[str, Any] = {
            "model": selected_model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
            },
        }

        response = requests.post(
            f"{self.BASE_URL}/api/generate",
            json=payload,
            timeout=120,
        )

        response.raise_for_status()

        data = response.json()

        result = data.get(
            "response",
            "",
        ).strip()

        logger.info("Ollama response generated")

        return result
