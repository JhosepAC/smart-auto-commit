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
