from motor.motor_asyncio import AsyncIOMotorDatabase

from app.db import database as _database


def get_db() -> AsyncIOMotorDatabase:
    """FastAPI dependency that returns the shared Mongo database handle."""
    if _database._db is None:
        raise RuntimeError("Database not initialized. init_db() must run at startup.")
    return _database._db
