from core.container.app_container import AppContainer


def test_container_creation():
    container = AppContainer()

    assert container is not None


def test_health_service_resolution():
    container = AppContainer()

    health_service = container.services.health_service()

    assert health_service is not None
