from core.utils.filesystem import FileSystemUtils


def test_file_exists():
    result = FileSystemUtils.file_exists("main.py")

    assert result is True
