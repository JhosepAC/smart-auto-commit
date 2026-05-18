class RetryPolicy:
    """
    Manage retry execution policy.
    """

    MAX_RETRIES = 3

    def should_retry(
        self,
        attempt: int,
    ) -> bool:
        """
        Determine if retry is allowed.
        """

        return attempt < self.MAX_RETRIES
