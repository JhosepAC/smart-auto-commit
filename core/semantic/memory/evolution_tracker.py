class EvolutionTracker:
    """
    Track architectural evolution.
    """

    def architectural_trends(
        self,
        history: dict,
    ) -> list[str]:
        """
        Determine repository trends.
        """

        trends = []

        components = history.get(
            "components",
            {},
        )

        if (
            components.get(
                "service",
                0,
            )
            >= 3
        ):
            trends.append(("Service layer " "expansion"))

        if (
            components.get(
                "parser",
                0,
            )
            >= 2
        ):
            trends.append(("Semantic parsing " "growth"))

        if not trends:
            trends.append(("Stable architectural " "evolution"))

        return trends
