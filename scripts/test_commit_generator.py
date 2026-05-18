from core.git.conventional_commit_generator import (
    ConventionalCommitGenerator,
)


def main() -> None:
    generator = ConventionalCommitGenerator(".")

    generated_commit = generator.generate_commit()

    print()

    print("Conventional Commit Generator")

    print("-----------------------------")

    print()

    print(f"Type: " f"{generated_commit.commit_type}")

    print(f"Scope: " f"{generated_commit.scope}")

    print(f"Title: " f"{generated_commit.title}")

    print()

    print("Generated Commit:")

    print(generated_commit.full_message)

    print()


if __name__ == "__main__":
    main()
