# ---------------------
# Stage 1 - Builder
# ---------------------
FROM python:3.11.9-slim AS builder

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install Python packages
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# ---------------------
# Stage 2 - Final Image
# ---------------------
FROM python:3.11.9-slim

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Create non-root user
RUN useradd -m appuser

# Copy runtime dependencies from builder
COPY --from=builder /usr/local /usr/local
COPY . .

# Permissions
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["python", "app/main.py"]
