from loguru import logger
from fastapi import FastAPI, Depends
from routers import detection, models
from app_utils.model_manager import ModelManager

logger.add("logs/app.log", rotation="5 MB", level="INFO")

app = FastAPI()


model_manager = ModelManager()

app.include_router(detection.router, tags=["detection"], dependencies=[Depends(lambda: model_manager)])
app.include_router(models.router, tags=["models"], dependencies=[Depends(lambda: model_manager)])


@app.get("/")
async def root():
    """Root endpoint for the Transport Detection API."""
    logger.info("Root endpoint accessed")
    return {"message": "Transport Detection API"}
