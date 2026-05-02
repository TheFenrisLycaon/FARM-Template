# Contributing

Thanks for taking the time to contribute to FARM Template.

## Before You Start

- Check existing [issues](../../issues) and [pull requests](../../pulls) to avoid duplicate work.
- For significant changes, open an issue first to discuss the approach.
- Read the [Code of Conduct](CODE_OF_CONDUCT.md).

## Development Setup

**Prerequisites:** Docker + Docker Compose, or Python 3.13 + [`uv`](https://docs.astral.sh/uv/) + [Bun](https://bun.sh).

```sh
git clone <your-fork-url>
cd FARM-template
cp .env.example .env   # fill in required values
```

**With Docker:**
```sh
docker compose up --build
```

**Natively:**
```sh
# Backend
cd backend && uv sync && uv run uvicorn app.main:app --reload

# Frontend (separate terminal)
cd frontend && bun install && bun run dev
```

## Making Changes

1. Fork the repo and create a branch from `main`:
   ```sh
   git checkout -b feat/your-feature-name
   ```
2. Make your changes.
3. Run the test suite before opening a PR.
4. Push and open a pull request against `main`.

## Running Tests

**Backend:**
```sh
cd backend && uv run pytest
```

**Frontend:**
```sh
cd frontend && bun run lint && bun run build
```

All CI checks must pass before a PR can be merged.

## Pull Request Guidelines

- Keep PRs focused — one logical change per PR.
- Fill in the PR template completely.
- Reference any related issues with `Closes #<number>`.
- Add or update tests for any behaviour you change.
- Do not commit `.env` or any secrets.

## Commit Style

Use conventional commits:

```
feat: add rate limiting to API routes
fix: correct CORS header for preflight requests
docs: update setup instructions for uv
chore: bump next.js to 15.x
```

Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`.

## Project Structure

```
backend/    FastAPI app (app/main.py, routers, db, core)
frontend/   Next.js App Router (src/app/, src/components/)
docker-compose.yml          base services
docker-compose.override.yml dev overrides (bind mounts, reload)
.env.example                copy to .env before starting
```

## Questions

Open a [GitHub Discussion](../../discussions) or file an issue with the `question` label.
