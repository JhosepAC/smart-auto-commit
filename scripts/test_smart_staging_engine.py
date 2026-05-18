from core.git.smart_staging_engine import (
    SmartStagingEngine,
)


def main() -> None:
    engine = SmartStagingEngine(".")

    result = engine.analyze_staging_candidates()

    print()

    print("Smart Staging Engine")

    print("---------------------")

    print()

    print(f"Allowed Files: " f"{result.total_allowed}")

    print(f"Blocked Files: " f"{result.total_blocked}")

    print()

    print("Allowed:")

    for candidate in result.allowed_files:
        print(f"- {candidate.path}")

    print()

    print("Blocked:")

    for candidate in result.blocked_files:
        print((f"- {candidate.path} " f"({candidate.reason})"))

    print()


if __name__ == "__main__":
    main()
