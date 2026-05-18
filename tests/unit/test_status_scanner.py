from core.git.status_scanner import (
    GitStatusScanner,
)


def test_scan_status():
    scanner = GitStatusScanner(".")

    status = scanner.scan_status()

    assert status is not None


def test_status_has_attributes():
    scanner = GitStatusScanner(".")

    status = scanner.scan_status()

    assert hasattr(
        status,
        "modified_files",
    )

    assert hasattr(
        status,
        "staged_files",
    )

    assert hasattr(
        status,
        "untracked_files",
    )
