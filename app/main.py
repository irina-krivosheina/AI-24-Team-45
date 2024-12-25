from fastapi import FastAPI
from app.routers import detection
import uvicorn

app = FastAPI()

app.include_router(detection.router)

@app.get("/")
async def root():
    return {"message": "Transport Detection API"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 