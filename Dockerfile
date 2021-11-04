FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3
COPY . /app
WORKDIR /app
