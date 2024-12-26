import torch
from loguru import logger

class YOLOModel:
    def __init__(self, model_path: str):
        logger.info(f"Loading YOLO model from {model_path}")
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

    def detect(self, image):
        logger.info("Running detection on image")
        results = self.model(image)
        return results 