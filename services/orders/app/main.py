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
# Middleware to limit multipart/form-data payload size
# ---------------------------
class PayloadSizeLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_size: int = 2 * 1024 * 1024):  # 2MB
        super().__init__(app)
        self.max_size = max_size

    async def dispatch(self, request: Request, call_next):
        content_type = request.headers.get("content-type", "")
        content_length = request.headers.get("content-length")

        # Limit only multipart/form-data requests
        if "multipart/form-data" in content_type.lower():
            if content_length and int(content_length) > self.max_size:
                raise HTTPException(
                    status_code=413,
                    detail="Multipart/form-data payload too large"
                )

        return await call_next(request)

# ---------------------------
# Create FastAPI app instance
# ---------------------------
app = FastAPI(
    title="Orders Microservice",
    description="Handles customer orders for the e-commerce platform",
    version="1.0.0"
)

# Apply the secure middleware
app.add_middleware(PayloadSizeLimitMiddleware)

# Setup CORS (adjust allow_origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register application routes
app.include_router(orders_router, prefix="/api/orders", tags=["Orders"])

# Health check route
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}
