from typing import Optional


class ApplicationError(Exception):
    """
    Base exception for the entire application.
    """

    def __init__(
        self,
        message: str,
        details: Optional[str] = None,
    ) -> None:
        self.message = message
        self.details = details

        super().__init__(self.message)

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} | Details: {self.details}"

        return self.message


# =========================================================
# CONFIGURATION
# =========================================================


class ConfigurationError(ApplicationError):
    """
    Raised when configuration loading fails.
    """

    pass


# =========================================================
# GIT ENGINE
# =========================================================


class GitEngineError(ApplicationError):
    """
    Raised for Git engine related issues.
    """

    pass


class RepositoryNotFoundError(GitEngineError):
    """
    Raised when Git repository is not found.
    """

    pass


class InvalidGitRepositoryError(GitEngineError):
    """
    Raised when repository is invalid.
    """

    pass


# =========================================================
# AI ENGINE
# =========================================================


class AIEngineError(ApplicationError):
    """
    Raised for AI engine related issues.
    """

    pass


class OllamaConnectionError(AIEngineError):
    """
    Raised when Ollama connection fails.
    """

    pass


class ModelGenerationError(AIEngineError):
    """
    Raised when AI generation fails.
    """

    pass


# =========================================================
# SECURITY
# =========================================================


class SecurityError(ApplicationError):
    """
    Raised for security validation issues.
    """

    pass


class SecretDetectionError(SecurityError):
    """
    Raised when secrets are detected.
    """

    pass


# =========================================================
# WATCHER
# =========================================================


class WatcherError(ApplicationError):
    """
    Raised for file watcher issues.
    """

    pass
