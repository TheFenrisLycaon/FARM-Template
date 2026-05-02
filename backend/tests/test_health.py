import os

os.environ.setdefault("MONGO_URI", "mongodb://test:test@localhost:27017/")
os.environ.setdefault("CLERK_SECRET_KEY", "sk_test_dummy")
os.environ.setdefault("BACKEND_CORS_ORIGINS", "http://localhost:3000")

from fastapi.testclient import TestClient  # noqa: E402

from app.core.deps import get_db  # noqa: E402
from app.main import app  # noqa: E402


class _FakeDB:
    async def command(self, _name: str):
        return {"ok": 1}


app.dependency_overrides[get_db] = lambda: _FakeDB()


def test_health_db_ok():
    with TestClient(app) as client:
        resp = client.get("/health/db")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_root():
    with TestClient(app) as client:
        resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Hello World !"}
