from loguru import logger
from fastapi import FastAPI
from app.routers import detection

logger.add("logs/app.log", rotation="5 MB", level="ERROR")

app = FastAPI()

app.include_router(detection.router)


@app.get("/")
async def root():
    """Root endpoint for the Transport Detection API."""
    logger.info("Root endpoint accessed")
    return {"message": "Transport Detection API"}
