from core.git.repository_detector import (
    GitRepositoryDetector,
)


def main() -> None:
    detector = GitRepositoryDetector(".")

    detector.validate_repository()

    detector.ensure_repository_structure()

    print()

    print("Repository detected successfully")

    print(f"Repository path: " f"{detector.get_repository_path()}")

    print(f".git directory: " f"{detector.get_git_directory()}")

    print()


if __name__ == "__main__":
    main()
