FROM python:3.9-slim

WORKDIR /frontend
COPY app/frontend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/frontend .

CMD ["sh", "-c", "streamlit run streamlit_app.py --server.port=${STREAMLIT_PORT} --server.address=0.0.0.0"]
