# app/db/database.py
import logging
from typing import cast

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.asynchronous.database import AsyncDatabase
from pymongo.errors import ConnectionFailure

from app.core.config import settings

logger = logging.getLogger(__name__)


async def init_db() -> AsyncIOMotorClient:
    """
    Initializes the database connection and Beanie ODM.
    This function should be called at application startup.
    """
    try:
        # Initialize the MongoDB client
        client = AsyncIOMotorClient(settings.MONGO_URI)
        db = client[settings.MONGO_DB_NAME]

        # Initialize Beanie with the database
        await init_beanie(database=cast(AsyncDatabase, db), document_models=[])

        logger.info("Database connection established successfully.")

        return client
    except ConnectionFailure as e:
        logger.critical(f"Failed to connect to MongoDB: {e}")
        raise e


async def close_mongo_connection(client: AsyncIOMotorClient):
    """Closes the MongoDB connection during application shutdown."""
    if client:
        logger.info("Closing MongoDB connection...")
        client.close()
        logger.info("MongoDB connection closed.")
