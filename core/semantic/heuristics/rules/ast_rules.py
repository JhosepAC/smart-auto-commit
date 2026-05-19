from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
    HeuristicMatch,
)


class ASTRules:
    """
    AST-based heuristic rules.
    """

    def analyze(
        self,
        analysis: ASTAnalysisResult,
    ) -> list[HeuristicMatch]:
        """
        Analyze AST semantics.
        """

        matches = []

        if analysis.endpoints:
            matches.append(
                HeuristicMatch(
                    rule_name="endpoint_detected",
                    commit_type="feat",
                    confidence=0.88,
                    reason=("API endpoints detected"),
                )
            )

        async_functions = [
            function for function in (analysis.functions) if function.is_async
        ]

        if async_functions:
            matches.append(
                HeuristicMatch(
                    rule_name="async_processing",
                    commit_type="perf",
                    confidence=0.70,
                    reason=("Async processing detected"),
                )
            )

        return matches
