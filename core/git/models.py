from dataclasses import dataclass


@dataclass(slots=True)
class GitFileStatus:
    """
    Represent Git file status.
    """

    path: str

    index_status: str

    working_tree_status: str


@dataclass(slots=True)
class GitRepositoryStatus:
    """
    Represent repository Git status.
    """

    modified_files: list[GitFileStatus]

    staged_files: list[GitFileStatus]

    untracked_files: list[GitFileStatus]

    deleted_files: list[GitFileStatus]


@dataclass(slots=True)
class GitDiff:
    """
    Represent Git diff information.
    """

    file_path: str

    diff_content: str

    additions: int

    deletions: int


@dataclass(slots=True)
class FileAnalysis:
    """
    Represent semantic file analysis.
    """

    file_path: str

    extension: str

    language: str

    category: str

    importance_score: int

    is_code_file: bool

    is_configuration_file: bool

    is_documentation_file: bool


@dataclass(slots=True)
class CommitContext:
    """
    Represent aggregated commit context.
    """

    total_files_changed: int

    total_additions: int

    total_deletions: int

    impacted_languages: list[str]

    impacted_categories: list[str]

    critical_files: list[str]

    high_importance_files: list[str]

    summary: str


@dataclass(slots=True)
class SemanticClassification:
    """
    Represent semantic change classification.
    """

    commit_type: str

    confidence_score: float

    detected_patterns: list[str]

    reasoning: str


@dataclass(slots=True)
class GeneratedCommit:
    """
    Represent generated commit message.
    """

    commit_type: str

    scope: str

    title: str

    full_message: str


@dataclass(slots=True)
class CommitQualityReport:
    """
    Represent commit quality validation.
    """

    is_valid: bool

    quality_score: int

    warnings: list[str]

    suggestions: list[str]


@dataclass(slots=True)
class CommitExecutionResult:
    """
    Represent commit execution result.
    """

    success: bool

    commit_message: str

    commit_hash: str | None

    stdout: str

    stderr: str

    dry_run: bool


@dataclass(slots=True)
class StagingCandidate:
    """
    Represent staging candidate file.
    """

    path: str

    allowed: bool

    reason: str


@dataclass(slots=True)
class SmartStagingResult:
    """
    Represent smart staging analysis.
    """

    allowed_files: list[StagingCandidate]

    blocked_files: list[StagingCandidate]

    total_allowed: int

    total_blocked: int


@dataclass(slots=True)
class RepositorySafetyReport:
    """
    Represent repository safety validation.
    """

    safe: bool

    risk_score: int

    blocked_reasons: list[str]

    warnings: list[str]

    current_branch: str

    total_changed_files: int


@dataclass(slots=True)
class RepositoryCheckpoint:
    """
    Represent repository recovery checkpoint.
    """

    branch: str

    head_commit: str

    staged_files: list[str]

    modified_files: list[str]


@dataclass(slots=True)
class RecoveryResult:
    """
    Represent rollback recovery result.
    """

    success: bool

    restored_branch: str

    restored_commit: str

    stdout: str

    stderr: str
