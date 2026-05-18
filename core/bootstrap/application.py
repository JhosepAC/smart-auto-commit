from core.bootstrap.environment import EnvironmentValidator
from core.bootstrap.lifecycle import ApplicationStatus
from core.bootstrap.runtime import RuntimePreparation
from core.bootstrap.validators import StartupValidator
from core.container.app_container import AppContainer
from core.exceptions.base import ApplicationError
from core.logging.logger import logger


class Application:
    """
    Main application bootstrap system.
    """

    def __init__(self) -> None:
        self.status = ApplicationStatus.CREATED

        self.container = AppContainer()

    def bootstrap(self) -> None:
        """
        Bootstrap application lifecycle.
        """

        try:
            self.status = ApplicationStatus.INITIALIZING

            logger.info("Starting application bootstrap")

            self._validate_environment()

            self._validate_startup_requirements()

            self._prepare_runtime()

            self._initialize_services()

            self.status = ApplicationStatus.RUNNING

            logger.info("Application bootstrap completed successfully")

        except Exception as error:
            self.status = ApplicationStatus.FAILED

            logger.exception(f"Application bootstrap failed: {error}")

            raise ApplicationError("Application startup failed") from error

    def _validate_environment(self) -> None:
        """
        Validate runtime environment.
        """

        logger.info("Validating environment")

        EnvironmentValidator.validate_python_version()

        EnvironmentValidator.validate_operating_system()

    def _validate_startup_requirements(self) -> None:
        """
        Validate startup requirements.
        """

        logger.info("Validating startup requirements")

        StartupValidator.validate_directories()

        StartupValidator.validate_required_files()

    def _prepare_runtime(self) -> None:
        """
        Prepare runtime environment.
        """

        RuntimePreparation.prepare_runtime()

    def _initialize_services(self) -> None:
        """
        Initialize application services.
        """

        logger.info("Initializing services")

        health_service = self.container.services.health_service()

        health = health_service.check_health()

        logger.info(f"Health check completed: {health}")
