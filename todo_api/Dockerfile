FROM ubuntu:18.04

RUN apt update -y && \
    apt install -y python3-pip python3-dev libpq-dev python-dev

WORKDIR /api

RUN pip3 install flask flask-restful

COPY . .

ENTRYPOINT ["python3"]
CMD ["api.py"]
