FROM python:3.9-buster
ENV BOT_NAME=$BOT_NAME

WORKDIR /usr/src/app/"${BOT_NAME:-tg_bot}"

COPY requirements.txt /usr/src/app/"${BOT_NAME:-tg_bot}"

RUN apt-get update && \
    apt-get install -y build-essential apt-utils cmake git libgtk2.0-dev pkg-config libavcodec-dev \
    libavformat-dev libswscale-dev python-dev python-numpy \
    libtbb2 libtbb-dev \
    libjpeg-dev libjasper-dev libdc1394-22-dev \
    python-opencv libopencv-dev libav-tools python-pycurl \
    libatlas-base-dev gfortran webp qt5-default libvtk6-dev zlib1g-dev unzip && \
    rm -rf /var/lib/apt/lists/*


RUN pip install -r /usr/src/app/"${BOT_NAME:-tg_bot}"/requirements.txt
RUN pip install --upgrade pip && \
    pip install tensorflow \

COPY . /usr/src/app/"${BOT_NAME:-tg_bot}"
