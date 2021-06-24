FROM python:3.8

WORKDIR /bot

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./src ./src

CMD ["python", "./src/main.py"]
