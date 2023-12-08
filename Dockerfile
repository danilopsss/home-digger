FROM python:3.12-slim

COPY ./{*.toml, *.lock} ./scripts/ ./

RUN bash /python-image.sh

COPY ./homedigger /app/homedigger
COPY ./html /tmp/html

WORKDIR /app
