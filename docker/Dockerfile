FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY docker/requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

RUN adduser -D mariana
USER mariana

CMD ["make migrate"]