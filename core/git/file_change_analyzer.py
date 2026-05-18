from pathlib import Path

from core.git.models import (
    FileAnalysis,
)
from core.logging.logger import logger


class FileChangeAnalyzer:
    """
    Analyze semantic information
    about changed files.
    """

    LANGUAGE_MAPPING = {
        ".py": "Python",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".tsx": "TypeScript React",
        ".jsx": "JavaScript React",
        ".json": "JSON",
        ".yml": "YAML",
        ".yaml": "YAML",
        ".md": "Markdown",
        ".html": "HTML",
        ".css": "CSS",
        ".scss": "SCSS",
        ".sql": "SQL",
        ".sh": "Shell",
    }

    CONFIGURATION_EXTENSIONS = {
        ".json",
        ".yml",
        ".yaml",
        ".toml",
        ".ini",
        ".env",
    }

    DOCUMENTATION_EXTENSIONS = {
        ".md",
        ".txt",
        ".rst",
    }

    CRITICAL_FILES = {
        "pyproject.toml",
        "requirements.txt",
        ".env",
        "docker-compose.yml",
    }

    def analyze_file(
        self,
        file_path: str,
    ) -> FileAnalysis:
        """
        Analyze changed file.
        """

        logger.info(f"Analyzing file: {file_path}")

        path = Path(file_path)

        extension = path.suffix.lower()

        language = self.LANGUAGE_MAPPING.get(
            extension,
            "Unknown",
        )

        is_configuration_file = extension in self.CONFIGURATION_EXTENSIONS

        is_documentation_file = extension in self.DOCUMENTATION_EXTENSIONS

        is_code_file = not is_configuration_file and not is_documentation_file

        category = self._detect_category(
            is_code_file,
            is_configuration_file,
            is_documentation_file,
        )

        importance_score = self._calculate_importance(path)

        analysis = FileAnalysis(
            file_path=file_path,
            extension=extension,
            language=language,
            category=category,
            importance_score=(importance_score),
            is_code_file=is_code_file,
            is_configuration_file=(is_configuration_file),
            is_documentation_file=(is_documentation_file),
        )

        logger.info(("File analyzed successfully: " f"{file_path}"))

        return analysis

    def _detect_category(
        self,
        is_code_file: bool,
        is_configuration_file: bool,
        is_documentation_file: bool,
    ) -> str:
        """
        Detect semantic file category.
        """

        if is_configuration_file:
            return "configuration"

        if is_documentation_file:
            return "documentation"

        if is_code_file:
            return "source_code"

        return "unknown"

    def _calculate_importance(
        self,
        path: Path,
    ) -> int:
        """
        Calculate file importance score.
        """

        score = 1

        if path.name in self.CRITICAL_FILES:
            score += 5

        if "core" in path.parts:
            score += 3

        if "security" in path.parts:
            score += 5

        if path.suffix == ".py":
            score += 2

        return score
