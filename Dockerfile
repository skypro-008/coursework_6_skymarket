FROM python:3.11-alpine

WORKDIR /opt/app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./skymarket/. .

COPY . .