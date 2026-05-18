from core.git.repository_detector import (
    GitRepositoryDetector,
)


def test_repository_exists():
    detector = GitRepositoryDetector(".")

    assert detector.repository_exists()


def test_is_git_repository():
    detector = GitRepositoryDetector(".")

    assert detector.is_git_repository()


def test_repository_path():
    detector = GitRepositoryDetector(".")

    assert detector.get_repository_path() is not None
