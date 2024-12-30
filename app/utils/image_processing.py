import cv2
import numpy as np
from loguru import logger


def read_image(file_bytes):
    """Decode image from bytes using OpenCV."""
    logger.info("Reading image from bytes")
    np_arr = np.frombuffer(file_bytes, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return image
