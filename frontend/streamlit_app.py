import streamlit as st
from loguru import logger
import os
import requests

API_URL = "http://localhost:8000"

logger.add("../logs/streamlit_app.log", rotation="5 MB", retention=2, level="INFO")

model_dir = os.path.abspath("model")
model_files = os.listdir(model_dir)
selected_model = st.sidebar.selectbox("Choose a model", model_files)

if st.sidebar.button("Set Model"):
    model_path = os.path.join(model_dir, selected_model)
    if not os.path.exists(model_path):
        st.sidebar.error(f"Model file not found: {model_path}")
        logger.error(f"Model file not found: {model_path}")
    else:
        response = requests.post(f"{API_URL}/set_model/", json={"model_path": model_path})
        if response.status_code == 200:
            st.sidebar.success(f"Model set to {selected_model}")
            logger.info(f"Model set to {selected_model}")
        else:
            st.sidebar.error("Failed to set model")
            logger.error("Failed to set model")

detect_image_page = st.Page(
    "pages/detect_image_page.py", title="Detect Image", icon="🚗", default=True
)

get_coordinates_page = st.Page(
    "pages/get_coordinates_page.py", title="Get Coordinates", icon="📐"
)

pg = st.navigation(
    {
        "Inference": [detect_image_page, get_coordinates_page],
    }
)

pg.run()