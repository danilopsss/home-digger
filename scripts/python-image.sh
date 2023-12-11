#!/bin/bash

# APT UPDATE AND BASIC INSTALLS
apt-get update -y
apt-get install iputils-ping postgresql -y

# UPDGRADE PIP
pip install --upgrade pip
pip install poetry

# INSTALL POETRY AND REMOVE TOML
poetry config virtualenvs.create false
poetry install --no-dev
# rm -rf *.toml *.lock
