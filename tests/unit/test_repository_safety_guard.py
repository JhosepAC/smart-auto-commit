from core.git.repository_safety_guard import (
    RepositorySafetyGuard,
)


def test_validate_repository_safety():
    guard = RepositorySafetyGuard(".")

    report = guard.validate_repository_safety()

    assert report is not None


def test_risk_score_type():
    guard = RepositorySafetyGuard(".")

    report = guard.validate_repository_safety()

    assert isinstance(
        report.risk_score,
        int,
    )


def test_safe_flag_type():
    guard = RepositorySafetyGuard(".")

    report = guard.validate_repository_safety()

    assert isinstance(
        report.safe,
        bool,
    )
