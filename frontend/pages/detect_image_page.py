import streamlit as st
import requests
from PIL import Image
import io
from loguru import logger

API_URL = "http://localhost:8000"

st.title("Transport Detection with YOLOv5")

def detect_image_page(uploaded_file, selected_model):
    col1, col2 = st.columns(2)

    with col1:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_container_width=True)
        logger.info("Image uploaded")

    if st.button("Detect"):
        logger.info("Detection button clicked")
        try:
            files = {"file": uploaded_file.getvalue()}
            response = requests.post(f"{API_URL}/detect/image/", files=files, params={"model_path": selected_model})
            logger.info(f"Request sent to {API_URL}/detect/image/ with model {selected_model}")

            if response.status_code == 200:
                with col2:
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption='Detected Image.', use_container_width=True)
                    logger.info("Detection successful, image displayed")
            else:
                st.error("Error in detection process")
                logger.error(f"Detection failed with status code: {response.status_code}")
        except Exception as e:
            st.error("An error occurred during detection")
            logger.error(f"Exception during detection: {e}")

