FROM ubuntu:18.04

RUN apt-get update
RUN apt-get -y install curl gnupg

RUN mkdir -p /app
RUN apt-get update
RUN apt-get install -y python3.6
RUN apt install -y python3-pip

RUN apt install -y tesseract-ocr
RUN apt-get install -y tesseract-ocr-all

RUN pip3 install --upgrade pip
RUN pip install pytesseract

RUN apt-get update
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libgtk-3-dev -y
RUN pip install opencv-python
Run pip install pdf2image
RUN apt-get install -y poppler-utils

COPY . /app
WORKDIR /app

ENTRYPOINT ["python3", "pdf-img-txt-pipeline.py"]




