from core.ai.services.ai_commit_generator import (
    AICommitGenerator,
)


def main() -> None:
    generator = AICommitGenerator(".")

    commit = generator.generate_commit()

    print()

    print("AI Commit Generator")

    print("-------------------")

    print()

    print(commit)

    print()


if __name__ == "__main__":
    main()
