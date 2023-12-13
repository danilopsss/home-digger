FROM python:3.11.7-slim

ENV APP=COLLECTOR

COPY ./collector/pyproject.toml \
     ./collector/poetry.lock \
     ./scripts \
     ./

COPY ./collector ./

RUN  ./build.sh
