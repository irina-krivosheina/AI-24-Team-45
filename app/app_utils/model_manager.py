import os
from loguru import logger
from app_models.yolo_model import YOLOModel


class ModelManager:
    _instance = None

    def __new__(cls, model_path: str):
        if cls._instance is None:
            cls._instance = super(ModelManager, cls).__new__(cls)
            if not os.path.exists(model_path):
                logger.error(f"Model path does not exist: {model_path}")
                raise ValueError("Model path does not exist")
            cls._instance.model = YOLOModel(model_path)
        return cls._instance

    def set_model(self, model_path: str):
        """Set a new model for detection."""
        if not os.path.exists(model_path):
            logger.error(f"Model path does not exist: {model_path}")
            raise ValueError("Model path does not exist")
        self.model = YOLOModel(model_path)
        logger.info(f"Model set to {model_path}")

    def detect(self, image):
        """Run detection on the provided image."""
        return self.model.detect(image)
