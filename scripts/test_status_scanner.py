from core.git.status_scanner import (
    GitStatusScanner,
)


def main() -> None:
    scanner = GitStatusScanner(".")

    status = scanner.scan_status()

    print()

    print("Git Status Scanner")

    print("------------------")

    print(f"Modified files: " f"{len(status.modified_files)}")

    print(f"Staged files: " f"{len(status.staged_files)}")

    print(f"Untracked files: " f"{len(status.untracked_files)}")

    print(f"Deleted files: " f"{len(status.deleted_files)}")

    print()

    for file in status.modified_files:
        print(f"[MODIFIED] {file.path}")

    print()


if __name__ == "__main__":
    main()
