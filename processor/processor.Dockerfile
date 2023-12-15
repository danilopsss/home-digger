FROM python:3.11.7-slim AS builer

COPY ./scripts .

FROM builer AS processor

ENV APP=PROCESSOR

COPY ./processor/alembic.ini \
     ./processor/pyproject.toml \
     ./processor/poetry.lock \
     /

COPY ./processor/homedigger /homedigger
COPY ./processor/alembic /alembic

RUN  ./build.sh

