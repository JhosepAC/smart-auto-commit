from core.git.repository_safety_guard import (
    RepositorySafetyGuard,
)


def main() -> None:
    guard = RepositorySafetyGuard(".")

    report = guard.validate_repository_safety()

    print()

    print("Repository Safety Guard")

    print("-----------------------")

    print()

    print(f"Safe: " f"{report.safe}")

    print(f"Risk Score: " f"{report.risk_score}")

    print(f"Current Branch: " f"{report.current_branch}")

    print(f"Changed Files: " f"{report.total_changed_files}")

    print()

    print("Blocked Reasons:")

    for reason in report.blocked_reasons:
        print(f"- {reason}")

    print()

    print("Warnings:")

    for warning in report.warnings:
        print(f"- {warning}")

    print()


if __name__ == "__main__":
    main()
