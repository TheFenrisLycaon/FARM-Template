import logging

from fastapi import APIRouter, Request
from pymongo.errors import ConnectionFailure

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/health/db", tags=["Health"])
async def check_db_connection(request: Request):
    """Check if the database is connected properly."""
    try:
        client = request.app.state.mongo_client
        await client.admin.command("ping")
        return {"status": "ok", "message": "Database connection successful."}
    except ConnectionFailure as e:
        logger.warning(f"Database connection failed: {e}")
        return {"status": "error", "message": f"Database connection failed: {str(e)}"}
