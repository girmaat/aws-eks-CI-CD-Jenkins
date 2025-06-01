# Stage 1 - Builder
FROM python:3.11-slim AS builder

# Set non-root user early for best practice
RUN useradd -m appuser

# Set workdir and install build deps
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Stage 2 - Runtime
FROM python:3.11-slim

WORKDIR /app

# Create non-root user again in final stage
RUN useradd -m appuser

# Copy app code and dependencies from builder
COPY --from=builder /usr/local /usr/local
COPY . .

# Set ownership and switch to non-root
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
CMD ["python", "app/main.py"]
