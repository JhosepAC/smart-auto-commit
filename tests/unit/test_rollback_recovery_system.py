from core.git.rollback_recovery_system import (
    RollbackRecoverySystem,
)


def test_create_checkpoint():
    system = RollbackRecoverySystem(".")

    checkpoint = system.create_checkpoint()

    assert checkpoint is not None


def test_checkpoint_branch():
    system = RollbackRecoverySystem(".")

    checkpoint = system.create_checkpoint()

    assert isinstance(
        checkpoint.branch,
        str,
    )


def test_checkpoint_commit():
    system = RollbackRecoverySystem(".")

    checkpoint = system.create_checkpoint()

    assert isinstance(
        checkpoint.head_commit,
        str,
    )
