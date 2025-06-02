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

# Install Python packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ---------------------
# Stage 2 - Runtime
# ---------------------
FROM python:3.11-slim
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Create and switch to non-root user
RUN useradd -m appuser

# Copy only the necessary runtime files
COPY --from=builder /usr/local /usr/local
COPY . .

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
CMD ["python", "app/main.py"]