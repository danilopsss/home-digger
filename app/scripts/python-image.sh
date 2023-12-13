#!/bin/bash

# APT UPDATE AND BASIC INSTALLS
apt-get update -y
apt-get install iputils-ping postgresql -y

# UPDGRADE PIP
pip install --upgrade pip
pip install poetry

# INSTALL POETRY AND REMOVE TOML
poetry config virtualenvs.create false

# VERIFY ENVIRONMENT
case $ENV in
  "TEST")
    poetry install
    ;;
  *)
    poetry install --no-dev
    ;;
esac

# REMOVE TOML AND LOCK FILES
rm -rf *.toml *.lock
