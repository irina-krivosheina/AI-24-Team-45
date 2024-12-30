FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 git
RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/ultralytics/yolov5 /yolov5
RUN pip install -r /yolov5/requirements.txt

COPY app /app

CMD ["python", "main.py"]

