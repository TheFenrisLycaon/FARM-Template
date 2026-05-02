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
    """
    Application settings, populated from environment variables

    Attributes:
        SECRET_KEY (str): Secret key for JWT authentication.
        ALGORITHM (str): Algorithm used for JWT.
        ACCESS_TOKEN_EXPIRE_MINUTES (int): JWT token expiration in minutes.
        ADMIN_USERNAME (str): Username for the initial admin user.
        MONGO_URL (str): MongoDB connection URL.
        MONGO_DB_NAME (str): MongoDB database name.
        LOG_FILE_PATH (str): Path to the log file.
        LOG_FILE_SIZE (int): Maximum log file size in bytes.
    """

    LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "logs/src.log")
    LOG_FILE_SIZE = int(os.getenv("LOG_FILE_SIZE", 10 * 1024 * 1024))

    MONGO_URI = _required("MONGO_URI")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "app")

    CLERK_SECRET_KEY = os.getenv("CLERK_SECRET_KEY", "")

    BACKEND_CORS_ORIGINS = os.getenv("BACKEND_CORS_ORIGINS", "localhost:3000").split(
        ","
    )

    def __init__(self):
        if not self.CLERK_SECRET_KEY:
            raise ValueError("CLERK_SECRET_KEY environment variable must be set")


settings = Settings()
