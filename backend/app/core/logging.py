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

    if logger.hasHandlers():
        logger.handlers.clear()

    # --- Formatter ---
    # The JSON formatter will be used by both handlers.
    formatter = JsonFormatter("%(asctime)s %(name)s %(levelname)s %(message)s")

    # --- Console Handler ---
    # This handler logger.infos logs to the console. Great for development.
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # --- File Handler ---
    # This handler writes logs to a file, with rotation.
    log_file_path = settings.LOG_FILE_PATH

    # Ensure the directory for the log file exists
    log_dir = os.path.dirname(log_file_path)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    # Create a rotating file handler.
    # maxBytes: The max size of a log file before it rotates. 10MB here.
    # backupCount: The number of old log files to keep.
    file_handler = RotatingFileHandler(
        filename=log_file_path,
        maxBytes=settings.LOG_FILE_SIZE,  # 10 MB
        backupCount=5,
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info(
        f"Logging configured successfully. Outputting to console and {log_file_path}"
    )
