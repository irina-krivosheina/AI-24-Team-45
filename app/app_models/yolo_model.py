import torch
from loguru import logger


class YOLOModel:
    """A class representing a YOLO model for object detection."""

    def __init__(self, model_path: str):
        """Initialize the YOLO model with the given model path."""
        logger.info(f"Loading YOLO model from {model_path}")
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, trust_repo=True)

    def detect(self, image):
        """Run detection on the provided image."""
        logger.info("Running detection on image")
        results = self.model(image)
        return results

    def get_model_info(self):
        """Return information about the loaded model."""
        return self.model.yaml
