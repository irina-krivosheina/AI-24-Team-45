FROM python:3.9-slim

WORKDIR /frontend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/frontend .

COPY app/frontend/public/training_progress.csv ./public/training_progress.csv

CMD ["sh", "-c", "streamlit run streamlit_app.py --server.port=${STREAMLIT_PORT} --server.address=0.0.0.0"]