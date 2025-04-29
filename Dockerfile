FROM python:3.12-slim

WORKDIR /app

# Installing psql
RUN apt-get update && apt-get install -y postgresql-client

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD daphne -b 0.0.0.0 -p 8000 app.asgi:application