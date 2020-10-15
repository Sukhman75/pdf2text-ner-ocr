FROM ubuntu:18.04

RUN apt-get update
RUN apt-get -y install curl gnupg
#RUN curl -sL https://deb.nodesource.com/setup_11.x  | bash -
#RUN apt-get -y install nodejs
RUN mkdir -p /app
RUN apt-get update
RUN apt-get install -y python3.6
# # RUN apt install update
RUN apt install -y python3-pip

RUN apt install -y tesseract-ocr
#RUN apt-get install tesseract-ocr-eng
RUN apt-get install -y tesseract-ocr-all 
#RUN apt-get install python3.7



#USER root
#RUN npm install
#EXPOSE 5000/udp
RUN pip3 install --upgrade pip
RUN pip install pytesseract
# RUN pip install tensorflow==1.13.1

# RUN sudo install --upgrade
RUN apt-get update
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libgtk-3-dev -y
RUN pip install opencv-python
Run pip install pdf2image
RUN apt-get install -y poppler-utils

#RUN pip install websocket-client
#RUN pip install matplotlib
#RUN pip install pillow
#RUN pip install requests
#RUN pip install socketio

# RUN apt-get install -y net-tools

# RUN pip install tflearn

# RUN pip install python-socketio
# RUN pip install flask-socketio
# RUN pip install gevent
# RUN pip install gevent-websocket
# #RUN pip install pafy
# #RUN pip install youtube-dl
# RUN pip install pymongo[srv]

COPY . /app
WORKDIR /app
#RUN apt-get install -y vim

#RUN cd Image_Classification

#RUN pip install -r requirements.txt

#ENTRYPOINT ["python3", "init.py"]
ENTRYPOINT ["python3", "pdf-img-txt-pipeline.py"]




