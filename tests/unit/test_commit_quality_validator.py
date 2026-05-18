from core.git.commit_quality_validator import (
    CommitQualityValidator,
)


def test_validate_commit():
    validator = CommitQualityValidator(".")

    report = validator.validate_commit()

    assert report is not None


def test_quality_score():
    validator = CommitQualityValidator(".")

    report = validator.validate_commit()

    assert report.quality_score >= 0


def test_commit_validation_result():
    validator = CommitQualityValidator(".")

    report = validator.validate_commit()

    assert isinstance(
        report.is_valid,
        bool,
    )
