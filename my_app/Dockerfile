FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
RUN pip3 install pytest allure-pytest
COPY . /my_app
WORKDIR /my_app 
RUN python3 app.py && pytest -v test_main.py --alluredir=reports/