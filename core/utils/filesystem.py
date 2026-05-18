from pathlib import Path

from core.logging.logger import logger


class FileSystemUtils:
    """
    Shared filesystem utilities.
    """

    @staticmethod
    def ensure_directory(path: str | Path) -> Path:
        """
        Ensure directory exists.
        """

        directory = Path(path)

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        logger.debug(f"Directory ensured: {directory}")

        return directory

    @staticmethod
    def file_exists(path: str | Path) -> bool:
        """
        Check if file exists.
        """

        return Path(path).exists()

    @staticmethod
    def read_text_file(
        path: str | Path,
        encoding: str = "utf-8",
    ) -> str:
        """
        Read text file content.
        """

        return Path(path).read_text(encoding=encoding)

    @staticmethod
    def write_text_file(
        path: str | Path,
        content: str,
        encoding: str = "utf-8",
    ) -> None:
        """
        Write text file content.
        """

        Path(path).write_text(
            content,
            encoding=encoding,
        )

        logger.debug(f"File written successfully: {path}")
