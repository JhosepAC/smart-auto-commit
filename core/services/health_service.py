from core.services.base_service import BaseService


class HealthService(BaseService):
    """
    Application health service.
    """

    def check_health(self) -> dict:
        """
        Validate application health.
        """

        self.logger.info("Running health check")

        return {
            "status": "healthy",
            "application": self.settings.application.name,
            "version": self.settings.application.version,
            "environment": self.settings.application.environment,
        }
