import streamlit as st
import requests
from PIL import Image
import io
from loguru import logger
import os

API_URL = "http://localhost:8000"

logger.add("../logs/streamlit_app.log", rotation="5 MB", level="ERROR")

st.title("Get Coordinates from Image")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_container_width=True)
    logger.info("Image uploaded for coordinates")

    if st.button("Get Coordinates"):
        logger.info("Get Coordinates button clicked")
        try:
            files = {"file": uploaded_file.getvalue()}
            response = requests.post(f"{API_URL}/detect/", files=files)
            logger.info(f"Request sent to {API_URL}/detect/")

            if response.status_code == 200:
                coordinates = response.json()
                logger.info("Coordinates successfully retrieved and displayed")
                
                # Отображение координат
                for coord in coordinates:
                    st.write(f"Class: {coord['name']}, Confidence: {coord['confidence']:.2f}")
                    st.write(f"Coordinates: ({coord['xmin']}, {coord['ymin']}) to ({coord['xmax']}, {coord['ymax']})")
                    st.write("---")
            else:
                logger.error(f"Failed to retrieve coordinates with status code: {response.status_code}")
                st.error("Error in retrieving coordinates")
        except Exception as e:
            logger.error(f"Exception during coordinates retrieval: {e}")
            st.error("An error occurred while retrieving coordinates")
