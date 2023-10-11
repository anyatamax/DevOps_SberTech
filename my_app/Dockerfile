FROM ubuntu:latest
MAINTAINER Anna Maksimova
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /my_app
WORKDIR /my_app 
RUN pip3 install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python3"]
CMD ["app.py"]