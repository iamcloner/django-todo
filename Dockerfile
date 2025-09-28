FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY todo/. /app/

CMD ["gunicorn", "todo.wsgi:application", "--bind", "0.0.0.0:8000"]
