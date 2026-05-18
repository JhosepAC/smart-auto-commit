from core.config.settings import settings
from core.logging.logger import logger


class BaseService:
    """
    Base service class for all application services.
    """

    def __init__(self) -> None:
        self.settings = settings
        self.logger = logger
