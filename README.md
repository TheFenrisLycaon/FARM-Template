# FARM Template

A full-stack starter combining **FastAPI + MongoDB (Beanie)** on the backend and **Next.js + Tailwind + Clerk** on the frontend, wired together with Docker Compose.

## Features
- FastAPI backend with structured logging and a shared async MongoDB client.
- Next.js (App Router) frontend with Tailwind v4 and Clerk authentication.
- Docker Compose for local dev (with hot reload) and a separate prod-shaped base config.
- TypeScript end-to-end on the frontend; `uv` for reproducible Python installs.

## Prerequisites
- Docker + Docker Compose, OR
- Python 3.13 with [`uv`](https://docs.astral.sh/uv/) and [Bun](https://bun.com) for native dev.
- A Clerk application (https://dashboard.clerk.com) — copy your **publishable** and **secret** keys.

## Setup
1. Clone and enter the repo:
   ```sh
   git clone <your-repo-url>
   cd FARM-template
   ```
2. Copy the env template and fill in real values:
   ```sh
   cp .env.example .env
   ```
   Required keys: `MONGO_USER`, `MONGO_PASSWORD`, `MONGO_DB_NAME`, `BACKEND_CORS_ORIGINS`, `CLERK_SECRET_KEY`, `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`.

## Run with Docker (recommended)
```sh
docker compose up --build
```
- Backend: http://localhost:8000 (health: `/health/db`)
- Frontend: http://localhost:3000

`docker-compose.override.yml` is picked up automatically for dev — it adds source bind mounts and `--reload`. Run prod-shaped with `docker compose -f docker-compose.yml up`.

Mongo data is persisted in the `mongo_data` named volume across `docker compose down` / `up`.

## Run natively
**Backend:**
```sh
cd backend
uv sync
uv run uvicorn app.main:app --reload
```

**Frontend:**
```sh
cd frontend
bun install
bun run dev
```

## Tests
```sh
cd backend && uv run pytest
cd frontend && bun run lint && bun run build
```

## Folder Structure
- `backend/` — FastAPI app (`app/main.py`, routers, db, core).
- `frontend/` — Next.js App Router (`src/app/`, `src/components/`).
- `docker-compose.yml` — base services for prod-shaped runs.
- `docker-compose.override.yml` — dev overrides (bind mounts, reload).
- `.env.example` — copy to `.env` before bringing the stack up.

## Notes
- The Clerk test keys checked into a fresh clone are placeholders; rotate them in the dashboard before any real use.
- `BACKEND_CORS_ORIGINS` must be set explicitly — the backend refuses to start without it.
