import os
from dotenv import load_dotenv


environment = os.getenv("ENVIRONMENT", "development")
dotenv_file = f"../../.env.{environment}"

load_dotenv(dotenv_file)

API_BASE_URL = os.getenv("API_BASE_URL")
IMAGE_PATH = os.getenv("IMAGE_PATH")
TRAINING_PROGRESS_PATH = os.getenv("TRAINING_PROGRESS_PATH")
MODEL_PATH = os.getenv("MODEL_PATH")
