from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router as orders_router
import logging

# Optional: Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the FastAPI app instance
app = FastAPI(
    title="Orders Microservice",
    description="Handles customer orders for the e-commerce platform",
    version="1.0.0"
)

# Setup CORS (optional; adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(orders_router, prefix="/api/orders", tags=["Orders"])

# Health check route
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}
