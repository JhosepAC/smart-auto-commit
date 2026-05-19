class CommitResponseCleaner:
    """
    Clean AI responses.
    """

    def clean(
        self,
        response: str,
    ) -> str:
        """
        Normalize commit response.
        """

        cleaned = response.strip()

        cleaned = cleaned.replace(
            "```",
            "",
        )

        return cleaned.strip()
