import logging
import os

from dotenv import load_dotenv

logger = logging.getLogger(__name__)

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

# Load the .env file from the project root
load_dotenv(dotenv_path=os.path.join(PROJECT_ROOT, ".env"))


class Settings:
    """
    Application settings class. Reads values from environment variables.

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

    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "test")

    CLERK_SECRET_KEY = os.getenv("CLERK_SECRET_KEY", "")

    BACKEND_CORS_ORIGINS = os.getenv("BACKEND_CORS_ORIGINS", "localhost:3000").split(
        ","
    )

    def __init__(self):
        if not self.CLERK_SECRET_KEY:
            raise ValueError("CLERK_SECRET_KEY environment variable must be set")


# Create a single, importable instance of the settings
settings = Settings()
