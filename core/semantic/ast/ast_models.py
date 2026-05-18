from dataclasses import (
    dataclass,
)


@dataclass(slots=True)
class ASTFunction:
    """
    Represent function node.
    """

    name: str

    is_async: bool

    decorators: list[str]

    arguments: list[str]

    line_number: int


@dataclass(slots=True)
class ASTClass:
    """
    Represent class node.
    """

    name: str

    base_classes: list[str]

    methods: list[str]

    decorators: list[str]

    line_number: int


@dataclass(slots=True)
class ASTImport:
    """
    Represent import node.
    """

    module: str

    imported_names: list[str]

    line_number: int


@dataclass(slots=True)
class ASTAnalysisResult:
    """
    Represent AST analysis result.
    """

    file_path: str

    language: str

    functions: list[ASTFunction]

    classes: list[ASTClass]

    imports: list[ASTImport]

    detected_frameworks: list[str]
