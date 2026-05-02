from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo.errors import PyMongoError

from app.db.database import get_db

router = APIRouter()


@router.get("/health/db", tags=["Health"])
async def check_db_connection(db: AsyncIOMotorDatabase = Depends(get_db)):
    """Check the shared MongoDB connection with a cheap ping."""
    try:
        await db.command("ping")
        return {"status": "ok", "message": "Database connection successful."}
    except PyMongoError as e:
        return {"status": "error", "message": f"Database connection failed: {e}"}
