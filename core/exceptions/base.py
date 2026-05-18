class ApplicationError(Exception):
    """
    Base application exception.
    """

    pass


class ConfigurationError(ApplicationError):
    """
    Raised when configuration loading fails.
    """

    pass


class GitEngineError(ApplicationError):
    """
    Raised for Git engine related issues.
    """

    pass


class AIEngineError(ApplicationError):
    """
    Raised for AI engine related issues.
    """

    pass


class SecurityError(ApplicationError):
    """
    Raised for security validation issues.
    """

    pass
