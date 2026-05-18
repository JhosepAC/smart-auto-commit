from core.git.commit_execution_engine import (
    CommitExecutionEngine,
)


def test_execute_commit():
    engine = CommitExecutionEngine(".")

    result = engine.execute_commit(dry_run=True)

    assert result.success is True


def test_dry_run_enabled():
    engine = CommitExecutionEngine(".")

    result = engine.execute_commit(dry_run=True)

    assert result.dry_run is True


def test_commit_message_generated():
    engine = CommitExecutionEngine(".")

    result = engine.execute_commit(dry_run=True)

    assert len(result.commit_message) > 0
