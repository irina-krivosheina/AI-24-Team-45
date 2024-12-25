from fastapi import FastAPI
from app.routers import detection

app = FastAPI()

app.include_router(detection.router)

@app.get("/")
async def root():
    return {"message": "Transport Detection API"} 