from abc import (
    ABC,
    abstractmethod,
)
from pathlib import Path

from core.semantic.ast.ast_models import (
    ASTAnalysisResult,
)


class BaseASTParser(ABC):
    """
    Base AST parser contract.
    """

    SUPPORTED_EXTENSIONS: set[str]

    @abstractmethod
    def parse(
        self,
        file_path: Path,
    ) -> ASTAnalysisResult:
        """
        Parse source file.
        """

    @classmethod
    def supports(
        cls,
        extension: str,
    ) -> bool:
        """
        Check parser support.
        """

        return extension.lower() in cls.SUPPORTED_EXTENSIONS
