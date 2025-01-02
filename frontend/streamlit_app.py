import os
import streamlit as st
from loguru import logger
import requests
import logging_config  # pylint: disable=unused-import


API_URL = "http://localhost:8000"

response = requests.get(f"{API_URL}/models/available")
model_files = response.json() if response.status_code == 200 else []

selected_model = st.sidebar.selectbox("Choose a model", model_files)

current_model_response = requests.get(f"{API_URL}/models/current")
current_model = current_model_response.json() if current_model_response.status_code == 200 else None

if current_model:
    st.sidebar.write(f"Current model: {current_model}")

if st.sidebar.button("Set Model"):
    response = requests.post(f"{API_URL}/models/set_model?model_name={selected_model}", timeout=10)
    if response.status_code == 200:
        st.sidebar.success(f"Model set to {selected_model}")
        logger.info(f"Model set to {selected_model}")
    else:
        st.sidebar.error("Failed to set model")
        logger.error(f"Failed to set model: {selected_model}, Status Code: {response.status_code}, Response: {response.text}")

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
