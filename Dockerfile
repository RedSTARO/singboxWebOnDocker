
FROM python:alpine

WORKDIR /app
COPY . /app

EXPOSE 5000
EXPOSE 9090
EXPOSE 2080

CMD ["python3", "start.py"]
