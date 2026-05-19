class AIResponseValidator:
    """
    Validate AI responses.
    """

    INVALID_PATTERNS = {
        "```",
        "#",
        "markdown",
    }

    def validate(
        self,
        response: str,
    ) -> bool:
        """
        Validate AI response.
        """

        if not response.strip():
            return False

        for pattern in self.INVALID_PATTERNS:
            if pattern in response:
                return False

        return True
