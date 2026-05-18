from core.bootstrap.application import Application
from core.bootstrap.lifecycle import ApplicationStatus


def test_application_creation():
    app = Application()

    assert app is not None


def test_application_initial_status():
    app = Application()

    assert app.status == ApplicationStatus.CREATED
