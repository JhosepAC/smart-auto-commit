from core.git.diff_engine import (
    GitDiffEngine,
)


def test_get_repository_diff():
    engine = GitDiffEngine(".")

    diffs = engine.get_repository_diff()

    assert diffs is not None


def test_diff_engine_returns_list():
    engine = GitDiffEngine(".")

    diffs = engine.get_repository_diff()

    assert isinstance(diffs, list)
