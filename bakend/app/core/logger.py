import logging
import sys
from logging.handlers import RotatingFileHandler


def setup_logger():

    logger = logging.getLogger("job_system")

    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
    )

    # Console logs
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # File logs
    file_handler = RotatingFileHandler(
        "job_system.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


logger = setup_logger()