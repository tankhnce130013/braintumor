# start from base

FROM ubuntu:18.04

LABEL maintainer="KIEN HA NGOC TAN tankhnce130013@fpt.edu.vn"

RUN apt-get update -y && \

    apt-get install -y python-pip python-dev
    pip3 install keras -y && \
    pip3 install tensorflow -y && \
    pip3 install Pillow==2.2.2 -y 

# We copy just the requirements.txt first to leverage Docker cache

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD [ "python", "./app.py" ]
