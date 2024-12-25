from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse
from app.models.yolo_model import YOLOModel
from app.utils.image_processing import read_image
import cv2
import numpy as np
import io

router = APIRouter()
model = YOLOModel('model/yolov5_weights.pt')

@router.post("/detect/")
async def detect_transport_coordinates(file: UploadFile = File(...)):
    image = read_image(await file.read())
    results = model.detect(image)
    return results.pandas().xyxy[0].to_dict(orient="records")


@router.post("/detect/image/")
async def detect_transport_image(file: UploadFile = File(...)):
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