from pathlib import Path

from core.semantic.ast.ast_models import (
    HeuristicMatch,
)


class FileRules:
    """
    File-based heuristic rules.
    """

    def analyze(
        self,
        file_path: str,
    ) -> list[HeuristicMatch]:
        """
        Analyze file heuristics.
        """

        matches = []

        path = Path(file_path)

        filename = path.name.lower()

        path_string = str(path).lower()

        if "test" in filename:
            matches.append(
                HeuristicMatch(
                    rule_name="test_file",
                    commit_type="test",
                    confidence=0.95,
                    reason=("Test file modified"),
                )
            )

        if filename == "requirements.txt" or filename == "pyproject.toml":
            matches.append(
                HeuristicMatch(
                    rule_name="dependency_file",
                    commit_type="build",
                    confidence=0.90,
                    reason=("Dependency file modified"),
                )
            )

        if "docs" in path_string:
            matches.append(
                HeuristicMatch(
                    rule_name="documentation",
                    commit_type="docs",
                    confidence=0.85,
                    reason=("Documentation modified"),
                )
            )

        if ".github" in path_string:
            matches.append(
                HeuristicMatch(
                    rule_name="ci_pipeline",
                    commit_type="ci",
                    confidence=0.90,
                    reason=("CI/CD pipeline modified"),
                )
            )

        return matches
