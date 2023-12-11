FROM python:3.12-slim

COPY ./pyproject.toml \
     ./poetry.lock \
     ./scripts \
     ./alembic.ini \
     alembic/ \
     ./

COPY ./homedigger /app
COPY ./html /tmp/html

RUN  ./python-image.sh
