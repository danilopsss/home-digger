FROM python:3.11.7-slim AS builer

COPY ./scripts .

FROM builer AS collector

ENV APP=COLLECTOR

COPY ./collector/pyproject.toml \
     ./collector/poetry.lock \
     ./

COPY ./collector ./

RUN  ./build.sh


FROM collector AS sentinel

ENV APP=SENTINEL

RUN ./build.sh
