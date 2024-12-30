import os
from loguru import logger
from app.models.yolo_model import YOLOModel


class ModelManager:
    """Class to manage YOLO model operations."""

    def __init__(self, model_path: str):
        """Initialize the model manager with a model path."""
        self.model = YOLOModel(model_path)

    def set_model(self, model_path: str):
        """Set a new model for detection."""
        if not os.path.exists(model_path):
            raise ValueError("Model path does not exist")
        self.model = YOLOModel(model_path)
        logger.info(f"Model set to {model_path}")

    def detect(self, image):
        """Run detection on the provided image."""
        return self.model.detect(image)
