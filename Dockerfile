FROM python:3.9-buster
ENV BOT_NAME=$BOT_NAME

WORKDIR /usr/src/app/"${BOT_NAME:-tg_bot}"

COPY requirements.txt /usr/src/app/"${BOT_NAME:-tg_bot}"

RUN apt-get update && apt-get install -y --no-install-recommends \
      bzip2 \
      g++ \
      git \
      graphviz \
      libgl1-mesa-glx \
      libhdf5-dev \
      openmpi-bin \
      wget \
      python3-tk && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -r /usr/src/app/"${BOT_NAME:-tg_bot}"/requirements.txt
RUN pip install --upgrade pip && \
    pip install tensorflow \

COPY . /usr/src/app/"${BOT_NAME:-tg_bot}"
