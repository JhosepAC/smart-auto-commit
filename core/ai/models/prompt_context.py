from dataclasses import dataclass


@dataclass(slots=True)
class PromptContext:
    """
    Represent AI prompt context.
    """

    repository_name: str

    branch_name: str

    changed_files: list[str]

    commit_summary: str

    semantic_type: str
