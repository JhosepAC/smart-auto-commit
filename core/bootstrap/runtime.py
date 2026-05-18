from core.logging.logger import logger


class RuntimePreparation:
    """
    Prepare application runtime.
    """

    @staticmethod
    def prepare_runtime() -> None:
        """
        Prepare runtime environment.
        """

        logger.info("Preparing runtime environment")

        logger.info("Runtime environment prepared")
