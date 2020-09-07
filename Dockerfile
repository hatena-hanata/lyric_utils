FROM python:3.8.0
USER root
WORKDIR /home/project

COPY requirements.txt /home
RUN pip install -r /home/requirements.txt
ENV FLASK_APP '/home/project/main.py'
ENV FLASK_DEBUG 1
