FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
MAINTAINER Akhil <akhilrajns@gmail.com>

COPY . /cryptomarkets
WORKDIR /cryptomarkets

RUN python3 -m pip install -r requirements.txt

EXPOSE 8000
CMD ["python3", "main.py"]
