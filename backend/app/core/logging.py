import logging
import os
import sys
from logging.handlers import RotatingFileHandler

from pythonjsonlogger.json import JsonFormatter

from app.core.config import settings


def setup_logging():
    """
    Configures logging to output to both console and a rotating file.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = JsonFormatter("%(asctime)s %(name)s %(levelname)s %(message)s")

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    log_file_path = settings.LOG_FILE_PATH
    log_dir = os.path.dirname(log_file_path)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    file_handler = RotatingFileHandler(
        filename=log_file_path,
        maxBytes=settings.LOG_FILE_SIZE,
        backupCount=5,
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info(
        f"Logging configured successfully. Outputting to console and {log_file_path}"
    )
