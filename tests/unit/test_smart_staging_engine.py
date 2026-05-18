from core.git.smart_staging_engine import (
    SmartStagingEngine,
)


def test_analyze_staging_candidates():
    engine = SmartStagingEngine(".")

    result = engine.analyze_staging_candidates()

    assert result is not None


def test_allowed_files_type():
    engine = SmartStagingEngine(".")

    result = engine.analyze_staging_candidates()

    assert isinstance(
        result.allowed_files,
        list,
    )


def test_blocked_files_type():
    engine = SmartStagingEngine(".")

    result = engine.analyze_staging_candidates()

    assert isinstance(
        result.blocked_files,
        list,
    )
