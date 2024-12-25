import torch

class YOLOModel:
    def __init__(self, model_path: str):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

    def detect(self, image):
        results = self.model(image)
        return results 