from core.git.commit_context_builder import (
    CommitContextBuilder,
)


def test_build_context():
    builder = CommitContextBuilder(".")

    context = builder.build_context()

    assert context is not None


def test_context_summary():
    builder = CommitContextBuilder(".")

    context = builder.build_context()

    assert isinstance(
        context.summary,
        str,
    )


def test_context_languages():
    builder = CommitContextBuilder(".")

    context = builder.build_context()

    assert isinstance(
        context.impacted_languages,
        list,
    )
