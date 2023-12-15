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
    poetry install --no-root
  else
    poetry install --no-dev --no-root
  fi

  rm -rf *.toml *.lock *.Dockerfile
}

case $APP in
  "DISPATCHER")
      install_system_packages
      install_python_packages
    ;;
  "PROCESSOR")
      install_system_packages
      install_python_packages
    ;;
  "COLLECTOR")
      install_system_packages
      install_python_packages
    ;;
  "SENTINEL")
      install_system_packages
      apt-get install curl -y
      apt-get install fswatch -y
    ;;
esac