# DockerFile, Image, Container
FROM python:3.10

ADD koza0021-assignement4.py .

RUN pip install random

CMD ["python", "./koza0021-assignment4.py"]