# Stage 1: Builder
FROM python:3.12-slim as builder

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install --prefix=/install -r requirements.txt

# Stage 2: Final minimal image
FROM python:3.12-slim

# Non-root user for security
RUN useradd -m appuser
USER appuser

WORKDIR /app

COPY --from=builder /install /usr/local
COPY ./app ./app
COPY ./data ./data

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
