from datetime import datetime, UTC


class TimeUtils:
    """
    Shared time utilities.
    """

    @staticmethod
    def current_timestamp() -> str:
        """
        Return formatted timestamp.
        """

        return datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def current_datetime() -> datetime:
        """
        Return current UTC datetime.
        """

        return datetime.now(UTC)

    @staticmethod
    def current_date() -> str:
        """
        Return current date.
        """

        return datetime.now(UTC).strftime("%Y-%m-%d")
