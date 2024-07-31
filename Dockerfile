FROM python:3.12.4-alpine3.20

WORKDIR /var/app

COPY . .

RUN pip3 install -r requirements.txt

CMD fastapi run main.py
