class SemanticPatternAnalyzer:
    """
    Analyze semantic repository patterns.
    """

    def dominant_patterns(
        self,
        history: dict,
    ) -> list[str]:
        """
        Extract dominant repository patterns.
        """

        patterns = []

        commit_types = history.get(
            "commit_types",
            {},
        )

        if (
            commit_types.get(
                "feat",
                0,
            )
            >= 3
        ):
            patterns.append(("Feature-driven " "development"))

        if (
            commit_types.get(
                "refactor",
                0,
            )
            >= 2
        ):
            patterns.append(("Frequent architectural " "refactoring"))

        if not patterns:
            patterns.append(("General repository " "evolution"))

        return patterns
