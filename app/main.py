from fastapi import FastAPI
from app.routers import detection
import uvicorn
from loguru import logger
from app.models.yolo_model import YOLOModel

logger.add("logs/app.log", rotation="5 MB", retention=2, level="INFO")

app = FastAPI()

# Загрузка модели при старте приложения
model = YOLOModel('model/yolov5_weights.pt')

app.include_router(detection.router)

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Transport Detection API"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 