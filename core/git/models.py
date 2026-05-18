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
