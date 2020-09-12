FROM python:3.8.0
USER root
WORKDIR /home/lyric_utils

# install heroku cli
RUN curl https://cli-assets.heroku.com/install.sh | sh

COPY requirements.txt /home
RUN pip install -r /home/requirements.txt
ENV FLASK_APP '/home/lyric_utils/main.py'
ENV FLASK_DEBUG 1
