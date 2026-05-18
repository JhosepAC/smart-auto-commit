from dependency_injector import containers, providers

from core.services.health_service import HealthService


class ServiceProviders(containers.DeclarativeContainer):
    """
    Centralized service providers container.
    """

    health_service = providers.Singleton(HealthService)
