FROM python:3.8.0
USER root
WORKDIR /home/project/

COPY requirements.txt ${PWD}
RUN pip install -r requirements.txt \
    && echo "PS1='\[\e[31m\][\u@\h:\w] \[\e[0m\] \$ '" >> ~/.bashrc \
    && echo "source ~/.bashrc" >> ~/.bash_profile

