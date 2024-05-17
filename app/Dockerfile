FROM python:3

WORKDIR /app

RUN pip install minio

COPY . .

CMD [ "python", "main.py" ]