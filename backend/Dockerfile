FROM python:3.13-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app


# Install the application dependencies.
WORKDIR /app
RUN uv sync --frozen --no-cache

# Add venv to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Run the application.
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]