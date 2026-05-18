from core.config.settings import settings


def test_settings_loaded():
    assert settings is not None


def test_application_name_exists():
    assert settings.application.name is not None
