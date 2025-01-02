import os
import streamlit as st
from loguru import logger
import requests
import logging_config  # pylint: disable=unused-import  # noqa: F401
from config import API_BASE_URL


available_models_response = requests.get(f"{API_BASE_URL}/models/available", timeout=10)
model_files = available_models_response.json() if available_models_response.status_code == 200 else []

current_model_response = requests.get(f"{API_BASE_URL}/models/current", timeout=10)
current_model = current_model_response.json() if current_model_response.status_code == 200 else None

if "selected_model" not in st.session_state:
    st.session_state.selected_model = current_model


def update_model():
    """Update the selected model on the server."""
    selected = st.session_state.selected_model
    set_model_response = requests.post(
        f"{API_BASE_URL}/models/set_model?model_name={selected}", timeout=10
    )
    if set_model_response.status_code == 200:
        st.sidebar.success(f"Model set to {selected}")
        logger.info(f"Model set to {selected}")
    else:
        st.sidebar.error("Failed to set model")
        logger.error(
            f"Failed to set model: {selected}, "
            f"Status Code: {set_model_response.status_code}, "
            f"Response: {set_model_response.text}"
        )


selected_model = st.sidebar.selectbox(
    "Choose a model",
    model_files,
    index=model_files.index(st.session_state.selected_model)
    if st.session_state.selected_model in model_files else 0,
    key="selected_model",
    on_change=update_model
)

st.sidebar.markdown(
    "[![Open in GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)]"
    "(https://github.com/irina-krivosheina/AI-24-Team-45)"
)

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
