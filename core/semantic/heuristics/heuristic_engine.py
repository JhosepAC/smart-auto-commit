from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
    HeuristicAnalysis,
    HeuristicMatch,
)

from core.semantic.heuristics.rules.ast_rules import (
    ASTRules,
)

from core.semantic.heuristics.rules.architecture_rules import (
    ArchitectureRules,
)

from core.semantic.heuristics.rules.file_rules import (
    FileRules,
)


class HeuristicEngine:
    """
    Semantic heuristic engine.
    """

    def __init__(
        self,
    ) -> None:
        self.file_rules = FileRules()

        self.ast_rules = ASTRules()

        self.architecture_rules = ArchitectureRules()

    def analyze(
        self,
        analysis: ASTAnalysisResult,
    ) -> HeuristicAnalysis:
        """
        Run heuristic analysis.
        """

        matches = []

        matches.extend(self.file_rules.analyze(analysis.file_path))

        matches.extend(self.ast_rules.analyze(analysis))

        matches.extend(
            self.architecture_rules.analyze(analysis.architectural_components)
        )

        dominant_commit_type = self._determine_commit_type(matches)

        confidence_score = self._calculate_confidence(matches)

        return HeuristicAnalysis(
            matches=matches,
            dominant_commit_type=(dominant_commit_type),
            confidence_score=(confidence_score),
        )

    def _determine_commit_type(
        self,
        matches: list[HeuristicMatch],
    ) -> str:
        """
        Determine dominant commit type.
        """

        if not matches:
            return "chore"

        scores: dict[str, float] = {}

        for match in matches:
            scores.setdefault(
                match.commit_type,
                0.0,
            )

            scores[match.commit_type] += match.confidence

        return max(
            scores.items(),
            key=lambda item: item[1],
        )[0]

    def _calculate_confidence(
        self,
        matches: list[HeuristicMatch],
    ) -> float:
        """
        Calculate heuristic confidence.
        """

        if not matches:
            return 0.0

        total = sum(match.confidence for match in matches)

        return round(
            total / len(matches),
            2,
        )
