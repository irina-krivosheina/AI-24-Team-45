from fastapi import APIRouter, File, UploadFile, Query, HTTPException
from fastapi.responses import StreamingResponse

from app.models.yolo_model import YOLOModel
from app.utils.image_processing import read_image

from app.models.model_path import ModelPath

import cv2
import numpy as np
from typing import Annotated, List, Dict
from loguru import logger
import os
import io

router = APIRouter()

DEFAULT_MODEL_PATH = 'model/yolov5_weights.pt'
current_model_path = DEFAULT_MODEL_PATH
model = YOLOModel(current_model_path)


@router.post("/set_model/")
async def set_model(data: ModelPath):
    global model
    try:
        if not os.path.exists(data.model_path):
            raise ValueError("Model path does not exist")
        model = YOLOModel(data.model_path)
        logger.info(f"Model set to {data.model_path}")
        return {"message": f"Model set to {data.model_path}"}
    except Exception as e:
        logger.error(f"Error setting model: {e}")
        raise HTTPException(status_code=400, detail="Invalid model path")

@router.post("/detect/", response_model=List[Dict[str, float]])
async def detect_transport_coordinates(file: Annotated[UploadFile, File(...)]) -> List[Dict[str, float]]:
    logger.info("Received request for /detect/")
    try:
        image = read_image(await file.read())
        results = model.detect(image)
        return results.pandas().xyxy[0].to_dict(orient="records")
    except Exception as e:
        logger.error(f"Error in detect_transport_coordinates: {e}")
        raise

@router.post("/detect/image/")
async def detect_transport_image(file: Annotated[UploadFile, File(...)]) -> StreamingResponse:
    logger.info("Received request for /detect/image/")
    try:
        image = read_image(await file.read())
        results = model.detect(image)
        detections = results.pandas().xyxy[0].to_dict(orient="records")

        for detection in detections:
            x1, y1, x2, y2 = int(detection['xmin']), int(detection['ymin']), int(detection['xmax']), int(detection['ymax'])
            label = detection['name']
            confidence = detection['confidence']
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, f"{label} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        _, img_encoded = cv2.imencode('.jpg', image)
        return StreamingResponse(io.BytesIO(img_encoded.tobytes()), media_type="image/jpeg")
    except Exception as e:
        logger.error(f"Error in detect_transport_image: {e}")
        raise 