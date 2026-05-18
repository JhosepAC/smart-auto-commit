from core.exceptions.base import GitEngineError


class GitRepositoryError(GitEngineError):
    """
    Base Git repository exception.
    """

    pass


class RepositoryNotFoundError(GitRepositoryError):
    """
    Raised when Git repository cannot be found.
    """

    pass


class InvalidRepositoryError(GitRepositoryError):
    """
    Raised when repository structure is invalid.
    """

    pass
