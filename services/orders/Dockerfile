# Stage 1 - Builder
FROM python:3.11.9-slim@sha256:59a7878e7e8702177b603137ec6b34d78097d4de7f79070b030fbab1d3cc93c8 AS builder

WORKDIR /app

# Set up build environment
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Stage 2 - Final
FROM python:3.11.9-slim@sha256:59a7878e7e8702177b603137ec6b34d78097d4de7f79070b030fbab1d3cc93c8

WORKDIR /app

RUN useradd -m appuser

# Copy from builder
COPY --from=builder /usr/local /usr/local
COPY . .

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
CMD ["python", "app/main.py"]
