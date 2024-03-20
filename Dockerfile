
FROM python:alpine

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/ 

EXPOSE 5000
EXPOSE 9090
EXPOSE 2080

CMD ["python3", "start.py"]
