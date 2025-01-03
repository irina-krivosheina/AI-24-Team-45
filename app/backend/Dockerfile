FROM python:3.9-slim

WORKDIR /backend
COPY app/backend/requirements.txt .
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 git
RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/ultralytics/yolov5 /yolov5 \
    && pip install --no-cache-dir -r /yolov5/requirements.txt \
    && rm -rf /yolov5/.git

COPY app/backend .

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${API_PORT}"]
