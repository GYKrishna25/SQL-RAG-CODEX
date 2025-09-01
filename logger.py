import logging
import sys

class Logger:
    _logger = None

    @staticmethod
    def get_logger(name: str = "app"):
        if Logger._logger is None:
            Logger._logger = logging.getLogger(name)
            Logger._logger.setLevel(logging.DEBUG)

            # Console handler
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(logging.DEBUG)

            # Formatter
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
                "%Y-%m-%d %H:%M:%S"
            )
            console_handler.setFormatter(formatter)

            Logger._logger.addHandler(console_handler)
            Logger._logger.propagate = False

        return Logger._logger
