import os
from loguru import logger
from app.models.yolo_model import YOLOModel

class ModelManager:
    def __init__(self, model_path: str):
        self.model = YOLOModel(model_path)

    def set_model(self, model_path: str):
        if not os.path.exists(model_path):
            raise ValueError("Model path does not exist")
        self.model = YOLOModel(model_path)
        logger.info(f"Model set to {model_path}")

    def detect(self, image):
        return self.model.detect(image) 