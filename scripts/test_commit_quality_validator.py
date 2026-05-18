from core.git.commit_quality_validator import (
    CommitQualityValidator,
)


def main() -> None:
    validator = CommitQualityValidator(".")

    report = validator.validate_commit()

    print()

    print("Commit Quality Validator")

    print("------------------------")

    print()

    print(f"Valid: " f"{report.is_valid}")

    print(f"Quality Score: " f"{report.quality_score}")

    print()

    print("Warnings:")

    for warning in report.warnings:
        print(f"- {warning}")

    print()

    print("Suggestions:")

    for suggestion in report.suggestions:
        print(f"- {suggestion}")

    print()


if __name__ == "__main__":
    main()
