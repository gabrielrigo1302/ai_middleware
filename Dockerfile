# Stage 1: Builder stage
FROM python:3.13-slim as builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-editable --no-dev

# Stage 2: Final stage
FROM python:3.13-slim

WORKDIR /app

# Copy only the virtual environment
COPY --from=builder /app/.venv /app/.venv

# Copy application code
COPY . .

# Use virtual environment
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]