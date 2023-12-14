FROM python:3.11.7-slim AS builer

COPY ./scripts .

FROM builer AS dispatcher

ENV APP=DISPATCHER

COPY ./dispatcher/pyproject.toml \
     ./dispatcher/poetry.lock \
     ./

COPY ./dispatcher ./

RUN  ./build.sh

