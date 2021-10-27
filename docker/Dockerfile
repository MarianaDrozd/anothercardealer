FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY docker/requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

CMD ["make migrate"]