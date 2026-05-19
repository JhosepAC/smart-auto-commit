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
class ASTEndpoint:
    """
    Represent API endpoint.
    """

    path: str

    method: str

    function_name: str

    is_async: bool

    line_number: int


@dataclass(slots=True)
class ArchitecturalComponent:
    """
    Represent architectural component.
    """

    name: str

    component_type: str

    framework: str | None

    line_number: int


@dataclass(slots=True)
class SemanticDependency:
    """
    Represent semantic dependency.
    """

    source_module: str

    target_module: str

    dependency_type: str

    line_number: int


@dataclass(slots=True)
class SemanticRelationship:
    """
    Represent semantic relationship.
    """

    source: str

    target: str

    relationship_type: str


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

    endpoints: list[ASTEndpoint]

    architectural_components: list[ArchitecturalComponent]

    semantic_dependencies: list[SemanticDependency]

    semantic_relationships: list[SemanticRelationship]
