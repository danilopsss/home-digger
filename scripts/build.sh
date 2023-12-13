#!/bin/bash

function wait_for() {
  until ping -c 1 $1 > /dev/null; do
    echo "Waiting for postgres container..."
    sleep 3
  done
}

function install_system_packages() {
  apt-get update -y
  apt-get install iputils-ping -y
}

function install_python_packages() {
  pip install --upgrade pip
  pip install poetry
  poetry config virtualenvs.create false

  if [ "$ENV" = "DEV" ]; then
    poetry install
  else
    poetry install --no-dev
  fi

  rm -rf *.toml *.lock
}

case $APP in
  "COLLECTOR")
      install_system_packages
      install_python_packages
    ;;
esac