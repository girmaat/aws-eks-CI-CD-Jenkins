from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from .routes import router as orders_router
import logging

# ---------------------------
# Optional: Configure logging
# ---------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ---------------------------
# Middleware to limit payload size (e.g., prevent DoS from huge form-data)
# ---------------------------
class SizeLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        content_length = request.headers.get('content-length')
        if content_length and int(content_length) > 2 * 1024 * 1024:  # 2MB limit
            raise HTTPException(status_code=413, detail="Payload too large")
        return await call_next(request)

# ---------------------------
# Create the FastAPI app instance
# ---------------------------
app = FastAPI(
    title="Orders Microservice",
    description="Handles customer orders for the e-commerce platform",
    version="1.0.0"
)

# Apply the size-limiting middleware
app.add_middleware(SizeLimitMiddleware)

# Setup CORS (adjust origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Consider restricting in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(orders_router, prefix="/api/orders", tags=["Orders"])

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}
