FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3

COPY server.py /server.py

WORKDIR /

EXPOSE 8000
CMD ["python3", "/server.py" ]
