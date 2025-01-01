import os
import streamlit as st
from loguru import logger
import requests
import logging_config  # pylint: disable=unused-import


API_URL = "http://localhost:8000"

model_dir = os.path.abspath("../model")
model_files = os.listdir(model_dir)
selected_model = st.sidebar.selectbox("Choose a model", model_files)

if st.sidebar.button("Set Model"):
    model_path = os.path.join(model_dir, selected_model)
    if not os.path.exists(model_path):
        st.sidebar.error(f"Model file not found: {model_path}")
        logger.error(f"Model file not found: {model_path}")
    else:
        response = requests.post(f"{API_URL}/set_model/", json={"model_path": model_path}, timeout=10)
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

eda_page = st.Page(
    "pages/eda_page.py", title="EDA", icon="📈"
)

training_progress_page = st.Page(
    "pages/training_progress_page.py", title="Training Progress", icon="🏁"
)

pg = st.navigation(
    {
        "Analyze": [eda_page, training_progress_page],
        "Inference": [detect_image_page, get_coordinates_page],
    }
)

pg.run()
