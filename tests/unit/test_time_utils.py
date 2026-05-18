from core.utils.time import TimeUtils


def test_current_timestamp():
    timestamp = TimeUtils.current_timestamp()

    assert timestamp is not None
