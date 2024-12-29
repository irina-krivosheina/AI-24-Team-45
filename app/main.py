from fastapi import FastAPI
from app.routers import detection
from loguru import logger

logger.add("logs/app.log", rotation="5 MB", level="ERROR")

app = FastAPI()

app.include_router(detection.router)

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Transport Detection API"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 