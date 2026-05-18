from core.git.commit_execution_engine import (
    CommitExecutionEngine,
)


def main() -> None:
    engine = CommitExecutionEngine(".")

    result = engine.execute_commit(dry_run=True)

    print()

    print("Commit Execution Engine")

    print("-----------------------")

    print()

    print(f"Success: " f"{result.success}")

    print(f"Dry Run: " f"{result.dry_run}")

    print()

    print("Commit Message:")

    print(result.commit_message)

    print()

    print(f"Stdout: " f"{result.stdout}")

    print()

    print(f"Stderr: " f"{result.stderr}")

    print()


if __name__ == "__main__":
    main()
