FROM ubuntu:latest
MAINTAINER Anna Maksimova
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /my_app
WORKDIR /my_app 
RUN python3 app.py && python3 -m unittest test_main