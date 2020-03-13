FROM ubuntu:18.04

RUN apt update -y && \
    apt install -y python3-pip python3-dev libpq-dev python-dev

WORKDIR /api

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
