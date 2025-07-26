from fastapi import APIRouter
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
from pymongo.errors import ConnectionFailure

router = APIRouter()

@router.get("/health/db", tags=["Health"])
async def check_db_connection():
    """Check if the database is connected properly."""
    try:
        client = AsyncIOMotorClient(settings.MONGO_URI, serverSelectionTimeoutMS=2000)
        # The ismaster command is cheap and does not require auth.
        await client.admin.command('ping')
        client.close()
        return {"status": "ok", "message": "Database connection successful."}
    except ConnectionFailure as e:
        return {"status": "error", "message": f"Database connection failed: {str(e)}"}
