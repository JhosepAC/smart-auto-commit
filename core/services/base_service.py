from core.config.settings import settings
from core.logging.logger import logger


class BaseService:
    """
    Base service class for all application services.
    """

    service_name = "base_service"

    def __init__(self) -> None:
        self.settings = settings

        self.logger = logger

        self.logger.debug(f"Initializing service: {self.service_name}")

    def initialize(self) -> None:
        """
        Initialize service resources.
        """

        self.logger.debug(f"Initializing resources for: {self.service_name}")

    def shutdown(self) -> None:
        """
        Shutdown service resources.
        """

        self.logger.debug(f"Shutting down service: {self.service_name}")
