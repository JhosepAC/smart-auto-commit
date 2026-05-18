from core.git.conventional_commit_generator import (
    ConventionalCommitGenerator,
)


def test_generate_commit():
    generator = ConventionalCommitGenerator(".")

    commit = generator.generate_commit()

    assert commit is not None


def test_generated_commit_message():
    generator = ConventionalCommitGenerator(".")

    commit = generator.generate_commit()

    assert ":" in commit.full_message


def test_generated_commit_scope():
    generator = ConventionalCommitGenerator(".")

    commit = generator.generate_commit()

    assert isinstance(
        commit.scope,
        str,
    )
