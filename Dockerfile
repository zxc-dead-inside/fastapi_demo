FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install uvicorn

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--ssl-keyfile", "cert.key", "--ssl-certfile", "cert.crt"]