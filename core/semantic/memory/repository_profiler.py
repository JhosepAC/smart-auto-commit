class RepositoryProfiler:
    """
    Build repository semantic profile.
    """

    def determine_maturity(
        self,
        activity_score: int,
    ) -> str:
        """
        Determine semantic maturity.
        """

        if activity_score >= 20:
            return "advanced"

        if activity_score >= 10:
            return "intermediate"

        return "early-stage"

    def build_ai_context(
        self,
        patterns: list[str],
        trends: list[str],
    ) -> str:
        """
        Build AI evolution context.
        """

        lines = []

        lines.append("Repository semantic profile:")

        lines.extend(patterns)

        lines.extend(trends)

        return "\n".join(lines)
