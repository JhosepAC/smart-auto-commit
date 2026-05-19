class TrendAnalyzer:
    """
    Analyze repository semantic trends.
    """

    def calculate_activity_score(
        self,
        history: dict,
    ) -> int:
        """
        Calculate repository activity.
        """

        commit_types = history.get(
            "commit_types",
            {},
        )

        return sum(commit_types.values())
