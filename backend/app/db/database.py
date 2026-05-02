import logging
from typing import cast

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pymongo.asynchronous.database import AsyncDatabase
from pymongo.errors import ConnectionFailure

from app.core.config import settings

logger = logging.getLogger(__name__)

_client: AsyncIOMotorClient | None = None
_db: AsyncIOMotorDatabase | None = None


async def init_db() -> AsyncIOMotorClient:
    """Initialize the shared Mongo client and Beanie ODM at startup."""
    global _client, _db
    try:
        _client = AsyncIOMotorClient(settings.MONGO_URI)
        _db = _client[settings.MONGO_DB_NAME]
        # TODO: register Beanie document models here as they are added.
        await init_beanie(database=cast(AsyncDatabase, _db), document_models=[])
        logger.info("Database connection established successfully.")
        return _client
    except ConnectionFailure as e:
        logger.critical(f"Failed to connect to MongoDB: {e}")
        raise


def get_db() -> AsyncIOMotorDatabase:
    """FastAPI dependency that returns the shared Mongo database handle."""
    if _db is None:
        raise RuntimeError("Database not initialized. init_db() must run at startup.")
    return _db


async def close_mongo_connection(client: AsyncIOMotorClient) -> None:
    if client:
        logger.info("Closing MongoDB connection...")
        client.close()
        logger.info("MongoDB connection closed.")
