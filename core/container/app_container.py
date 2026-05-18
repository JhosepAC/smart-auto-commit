from dependency_injector import containers, providers

from core.container.providers import ServiceProviders


class AppContainer(containers.DeclarativeContainer):
    """
    Main dependency injection container.
    """

    services = providers.Container(ServiceProviders)
