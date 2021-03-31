FROM ubuntu:18.04
WORKDIR /code
# Upgrade installed packages
RUN apt-get update && apt-get upgrade -y && apt-get clean
RUN apt-get install -y curl
# (...)
RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  rm -rf /var/lib/apt/lists/*
# Register the version in alternatives
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1
# Set python 3 as the default python
RUN update-alternatives --set python /usr/bin/python3.6
WORKDIR /data
COPY . /data
