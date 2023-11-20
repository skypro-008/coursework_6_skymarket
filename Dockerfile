FROM python:3.11-slim

WORKDIR /opt/app

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./skymarket/. .

COPY . .