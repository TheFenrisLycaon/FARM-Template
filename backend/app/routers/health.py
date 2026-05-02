import logging

from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo.errors import ConnectionFailure

from app.core.deps import get_db

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/health/db", tags=["Health"])
async def check_db_connection(db: AsyncIOMotorDatabase = Depends(get_db)):
    """Check if the database is connected properly."""
    try:
        await db.command("ping")
        return {"status": "ok", "message": "Database connection successful."}
    except ConnectionFailure as e:
        logger.warning(f"Database connection failed: {e}")
        return {"status": "error", "message": f"Database connection failed: {str(e)}"}
