import logging
import os

from dotenv import load_dotenv

logger = logging.getLogger(__name__)

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

load_dotenv(dotenv_path=os.path.join(PROJECT_ROOT, ".env"))


def _required(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(
            f"Required environment variable {name!r} is not set. "
            f"Copy .env.example to .env and fill in real values."
        )
    return value


class Settings:
    """Application settings, populated from environment variables."""

    LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "logs/src.log")
    LOG_FILE_SIZE = int(os.getenv("LOG_FILE_SIZE", 10 * 1024 * 1024))

    MONGO_URI = _required("MONGO_URI")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "app")

    CLERK_SECRET_KEY = _required("CLERK_SECRET_KEY")

    BACKEND_CORS_ORIGINS = [
        origin.strip()
        for origin in _required("BACKEND_CORS_ORIGINS").split(",")
        if origin.strip()
    ]


settings = Settings()
