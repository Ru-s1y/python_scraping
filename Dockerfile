FROM python:3.11-slim

RUN apt-get update
RUN apt-get install -y sudo less vim

RUN pip install --upgrade pip
WORKDIR /var/docker-python

COPY requirements.txt /var/docker-python
RUN pip install -r requirements.txt
