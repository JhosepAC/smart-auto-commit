from core.git.commit_context_builder import (
    CommitContextBuilder,
)


def main() -> None:
    builder = CommitContextBuilder(".")

    context = builder.build_context()

    print()

    print("Commit Context Builder")

    print("----------------------")

    print()

    print(f"Files changed: " f"{context.total_files_changed}")

    print(f"Additions: " f"{context.total_additions}")

    print(f"Deletions: " f"{context.total_deletions}")

    print()

    print(f"Languages: " f"{context.impacted_languages}")

    print(f"Categories: " f"{context.impacted_categories}")

    print()

    print(f"High importance files: " f"{context.high_importance_files}")

    print()

    print(f"Summary: " f"{context.summary}")

    print()


if __name__ == "__main__":
    main()
