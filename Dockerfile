FROM python:3.9-buster
ENV BOT_NAME=$BOT_NAME

WORKDIR /usr/src/app/"${BOT_NAME:-tg_bot}"

COPY requirements.txt /usr/src/app/"${BOT_NAME:-tg_bot}"

RUN apt-get update -y && \
    apt-get install build-essential libssl-dev cmake -y && \
    apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -r /usr/src/app/"${BOT_NAME:-tg_bot}"/requirements.txt

RUN pip install --upgrade pip && \
    pip install tensorflow \

COPY . /usr/src/app/"${BOT_NAME:-tg_bot}"
