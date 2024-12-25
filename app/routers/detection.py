from fastapi import APIRouter, File, UploadFile
from app.models.yolo_model import YOLOModel
from app.utils.image_processing import read_image

router = APIRouter()
model = YOLOModel('model/yolov5_weights.pt')

@router.post("/detect/")
async def detect_transport(file: UploadFile = File(...)):
    image = read_image(await file.read())
    results = model.detect(image)
    return results.pandas().xyxy[0].to_dict(orient="records") 