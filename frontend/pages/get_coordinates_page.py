import streamlit as st
import requests
from PIL import Image
import io
from loguru import logger

API_URL = "http://localhost:8000"

st.title("Get coordinates with YOLOv5")