import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import exceptions
from app.core.config import settings
from app.core.exception_handlers import base_exception_handler
from app.core.logging import setup_logging
from app.db.database import close_mongo_connection, init_db
from app.routers.health import router as health_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    client = await init_db()
    app.state.mongo_client = client
    yield
    await close_mongo_connection(client)


app = FastAPI(
    title="Template FastAPI with Clerk and MongoDB",
    description="The backend API template in FastAPI with Clerk and MongoDB",
    version="0.1.0",
    lifespan=lifespan,
    exception_handlers={exceptions.BaseException: base_exception_handler},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include health check router
app.include_router(health_router)


@app.get("/")
async def read_root():
    return {"message": "Hello World !"}
