import os
from dotenv import load_dotenv
from loguru import logger


environment = os.getenv("ENVIRONMENT", "development")
dotenv_file = f"../../.env.{environment}"

load_dotenv(dotenv_file)

MODEL_PATH = os.getenv("MODEL_PATH")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL")
