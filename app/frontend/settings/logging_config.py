from loguru import logger

logger.add("logs/streamlit_app.log", rotation="5 MB", level="INFO")
