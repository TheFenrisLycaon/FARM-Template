import logging

from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import BaseException

logger = logging.getLogger(__name__)


async def base_exception_handler(request: Request, exc: BaseException):
    """
    Handles all custom BaseExceptions and converts them into a standard JSON error response.

    Args:
        request (Request): The incoming FastAPI request.
        exc (BaseException): The custom exception instance.

    Returns:
        JSONResponse: A JSON response with the error details and status code.
    """
    logger.error(
        f"BaseException caught: {exc.detail}",
        extra={
            "status_code": exc.status_code,
            "request_url": str(request.url),
            "request_method": request.method,
        },
    )

    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
