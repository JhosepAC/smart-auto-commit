from core.semantic.ast.ast_models import (
    IntelligentCommit,
)


class IntelligentCommitFormatter:
    """
    Format intelligent commit messages.
    """

    def format(
        self,
        commit: IntelligentCommit,
    ) -> str:
        """
        Format final commit message.
        """

        lines = []

        lines.append((f"{commit.commit_type}" f"({commit.scope}): " f"{commit.title}"))

        lines.append("")

        lines.append(commit.summary)

        lines.append("")

        lines.append("Architectural impact:")

        lines.append((f"- " f"{commit.architectural_impact}"))

        lines.append("")

        lines.append("Technical reasoning:")

        for item in commit.technical_reasoning:
            lines.append(f"- {item}")

        return "\n".join(lines)
