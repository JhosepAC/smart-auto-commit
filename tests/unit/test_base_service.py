from core.services.base_service import BaseService


def test_base_service_creation():
    service = BaseService()

    assert service is not None


def test_base_service_has_logger():
    service = BaseService()

    assert service.logger is not None


def test_base_service_has_settings():
    service = BaseService()

    assert service.settings is not None
