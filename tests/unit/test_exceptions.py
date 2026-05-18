from core.exceptions.base import ApplicationError


def test_application_error():
    error = ApplicationError("Test error")

    assert str(error) == "Test error"
