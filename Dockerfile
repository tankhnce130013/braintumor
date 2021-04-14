# start from base

FROM ubuntu:18.04

LABEL maintainer="KIEN HA NGOC TAN tankhnce130013@fpt.edu.vn"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev &&\
    apt-get install virtualenv &&\
    virtualenv --python=python3 env  &&\
    source env/bin/activate &&\
    pip install -U pip &&\
    pip install -U setuptools &&\
    pip install keras && \
    pip install tensorflow  && \
    pip install Pillow==2.2.2  

# We copy just the requirements.txt first to leverage Docker cache

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD [ "python", "./app.py" ]
