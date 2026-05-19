from dataclasses import (
    dataclass,
    field,
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
class ImpactAnalysis:
    """
    Represent impact analysis.
    """

    impact_score: int

    coupling_score: int

    blast_radius: int

    criticality_level: str


@dataclass(slots=True)
class CriticalModule:
    """
    Represent critical module.
    """

    module_name: str

    reason: str

    severity: str


@dataclass(slots=True)
class HeuristicMatch:
    """
    Represent heuristic match.
    """

    rule_name: str

    commit_type: str

    confidence: float

    reason: str


@dataclass(slots=True)
class HeuristicAnalysis:
    """
    Represent heuristic analysis.
    """

    matches: list[HeuristicMatch]

    dominant_commit_type: str

    confidence_score: float


@dataclass(slots=True)
class SemanticContext:
    """
    Represent semantic context.
    """

    technical_summary: str

    architectural_summary: str

    impact_summary: str

    reasoning_chain: list[str]

    ai_context: str


@dataclass(slots=True)
class RepositorySemanticContext:
    """
    Represent repository semantic context.
    """

    total_files: int

    dominant_commit_type: str

    architectural_summary: str

    repository_summary: str

    impacted_components: list[str]

    reasoning_chain: list[str]

    global_risk_level: str

    ai_repository_context: str


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

    semantic_dependencies: list[SemanticDependency] = field(default_factory=list)

    semantic_relationships: list[SemanticRelationship] = field(default_factory=list)

    impact_analysis: ImpactAnalysis | None = None

    critical_modules: list[CriticalModule] = field(default_factory=list)

    heuristic_analysis: HeuristicAnalysis | None = None

    semantic_context: SemanticContext | None = None
