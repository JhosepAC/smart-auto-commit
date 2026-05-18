from functools import wraps
from typing import Callable

from core.exceptions.handlers import ExceptionHandler


def safe_execution(function: Callable):
    """
    Decorator for safe function execution.
    """

    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)

        except Exception as error:
            ExceptionHandler.handle(error)

            return None

    return wrapper
