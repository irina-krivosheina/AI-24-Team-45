import os
from loguru import logger
from app_models.yolo_model import YOLOModel


MODEL_PATHS = "../model"
DEFAULT_MODEL = "yolov5_weights.pt"


class ModelManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelManager, cls).__new__(cls)
            cls._instance.models = {
                f: os.path.join(MODEL_PATHS, f)
                for f in os.listdir(MODEL_PATHS)
                if os.path.isfile(os.path.join(MODEL_PATHS, f))
            }
            cls._instance.model = YOLOModel(DEFAULT_MODEL, cls._instance.models[DEFAULT_MODEL])
            logger.info(f"Models loaded: {cls._instance.models}")
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'models'):
            self.models = {
                f: os.path.join(MODEL_PATHS, f)
                for f in os.listdir(MODEL_PATHS)
                if os.path.isfile(os.path.join(MODEL_PATHS, f))
            }
            self.model = YOLOModel(DEFAULT_MODEL, self.models[DEFAULT_MODEL])
            logger.info(f"Models loaded: {self.models}")

    def set_model(self, model_name: str):
        """Set a new model for detection using model name."""
        if model_name not in self.models:
            logger.error(f"Model name does not exist: {model_name}")
            raise ValueError("Model name does not exist")
        model_path = self.models[model_name]
        self.model = YOLOModel(model_name, model_path)
        logger.info(f"Model set to {model_name}")

    def detect(self, image):
        """Run detection on the provided image."""
        return self.model.detect(image)

    def get_available_models(self):
        """Return a list of available model names."""
        model_names = list(self.models.keys())
        logger.info(f"Available models: {model_names}")
        return model_names

    def get_current_model(self):
        """Return the current model path."""
        current_model_name = self.model.model_name
        logger.info(f"Current model: {current_model_name}")
        return current_model_name
