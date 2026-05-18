from core.git.repository_validator import (
    GitRepositoryValidator,
)


def test_validate_repository_state():
    validator = GitRepositoryValidator(".")

    validator.validate_repository_state()


def test_get_current_branch():
    validator = GitRepositoryValidator(".")

    branch = validator.get_current_branch()

    assert branch is not None
