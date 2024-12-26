import cv2
import numpy as np
import torch
from loguru import logger

def read_image(file_bytes):
    logger.info("Reading image from bytes")
    np_arr = np.frombuffer(file_bytes, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return image 

def preprocess_image(image):
    logger.info("Preprocessing image")
    image = cv2.resize(image, (640, 640))
    image = image / 255.0
    image = torch.from_numpy(image).float()
    image = image.permute(2, 0, 1)
    image = image.unsqueeze(0)
    return image 