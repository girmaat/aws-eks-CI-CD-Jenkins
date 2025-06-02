# ---------------------
# Stage 1 - Builder
# ---------------------
FROM python:3.11-slim AS builder
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Install system build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Upgrade setuptools & install Python packages
RUN pip install --upgrade pip "setuptools>=78.1.1" && \
    pip install --no-cache-dir -r requirements.txt

# ---------------------
# Stage 2 - Runtime
# ---------------------
FROM python:3.11-slim
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Create and switch to non-root user
RUN useradd -m appuser

# Copy runtime dependencies and app code
COPY --from=builder /usr/local /usr/local
COPY . .

# ✅ Reconfirm correct setuptools version in final image
RUN pip install --no-cache-dir --upgrade "setuptools>=78.1.1"

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
CMD ["python", "app/main.py"]
