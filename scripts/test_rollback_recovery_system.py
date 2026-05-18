from core.git.rollback_recovery_system import (
    RollbackRecoverySystem,
)


def main() -> None:
    system = RollbackRecoverySystem(".")

    checkpoint = system.create_checkpoint()

    print()

    print("Rollback Recovery System")

    print("------------------------")

    print()

    print(f"Branch: " f"{checkpoint.branch}")

    print(f"HEAD Commit: " f"{checkpoint.head_commit}")

    print()

    print("Staged Files:")

    for file_path in checkpoint.staged_files:
        print(f"- {file_path}")

    print()

    print("Modified Files:")

    for file_path in checkpoint.modified_files:
        print(f"- {file_path}")

    print()


if __name__ == "__main__":
    main()
