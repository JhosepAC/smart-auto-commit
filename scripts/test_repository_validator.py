from core.git.repository_validator import (
    GitRepositoryValidator,
)


def main() -> None:
    validator = GitRepositoryValidator(".")

    validator.validate_repository_state()

    branch = validator.get_current_branch()

    print()

    print("Repository validation successful")

    print(f"Current branch: {branch}")

    print()


if __name__ == "__main__":
    main()
