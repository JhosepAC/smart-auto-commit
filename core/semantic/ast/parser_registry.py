from pathlib import Path

from core.semantic.ast.base_parser import (
    BaseASTParser,
)
from core.semantic.ast.python_parser import (
    PythonASTParser,
)


class ParserRegistry:
    """
    Manage AST parsers.
    """

    def __init__(
        self,
    ) -> None:
        self.parsers: list[BaseASTParser] = [
            PythonASTParser(),
        ]

    def get_parser(
        self,
        file_path: Path,
    ) -> BaseASTParser | None:
        """
        Retrieve compatible parser.
        """

        extension = file_path.suffix.lower()

        for parser in self.parsers:
            if parser.supports(extension):
                return parser

        return None
