import subprocess
from pathlib import Path

from core.git.models import GitDiff
from core.git.repository_validator import (
    GitRepositoryValidator,
)
from core.logging.logger import logger


class GitDiffEngine:
    """
    Extract and analyze Git diffs.
    """

    def __init__(
        self,
        repository_path: str | Path,
    ) -> None:
        self.repository_path = Path(repository_path).resolve()

        self.validator = GitRepositoryValidator(self.repository_path)

        self.validator.validate_repository_state()

    def get_repository_diff(
        self,
    ) -> list[GitDiff]:
        """
        Return repository diff information.
        """

        logger.info("Extracting repository diff")

        command = [
            "git",
            "diff",
            "--numstat",
        ]

        result = subprocess.run(
            command,
            cwd=self.repository_path,
            capture_output=True,
            text=True,
            check=False,
        )

        output = result.stdout.strip()

        if not output:
            logger.info("No diffs detected")

            return []

        diffs = []

        for line in output.splitlines():
            parts = line.split("\t")

            if len(parts) != 3:
                continue

            additions = 0 if parts[0] == "-" else int(parts[0])

            deletions = 0 if parts[1] == "-" else int(parts[1])

            file_path = parts[2]

            diff_content = self.get_file_diff(file_path)

            diffs.append(
                GitDiff(
                    file_path=file_path,
                    diff_content=diff_content,
                    additions=additions,
                    deletions=deletions,
                )
            )

        logger.info(("Repository diff extracted: " f"{len(diffs)} file diffs"))

        return diffs

    def get_file_diff(
        self,
        file_path: str,
    ) -> str:
        """
        Return diff content for file.
        """

        logger.debug(f"Extracting diff for: {file_path}")

        command = [
            "git",
            "diff",
            "--",
            file_path,
        ]

        result = subprocess.run(
            command,
            cwd=self.repository_path,
            capture_output=True,
            text=True,
            check=False,
        )

        return result.stdout.strip()
