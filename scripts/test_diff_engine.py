from core.git.diff_engine import (
    GitDiffEngine,
)


def main() -> None:
    engine = GitDiffEngine(".")

    diffs = engine.get_repository_diff()

    print()

    print("Git Diff Engine")

    print("----------------")

    print(f"Detected diffs: {len(diffs)}")

    print()

    for diff in diffs:
        print(f"File: {diff.file_path}")

        print(f"Additions: {diff.additions}")

        print(f"Deletions: {diff.deletions}")

        print()

    print()


if __name__ == "__main__":
    main()
