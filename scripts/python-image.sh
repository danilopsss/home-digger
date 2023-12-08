#!/bin/bash

# UPDGRADE PIP
pip install --upgrade pip
pip install poetry
# INSTALL POETRY AND REMOVE TOML
poetry config virtualenvs.create false
poetry install --no-dev
rm -rf *.toml *.lock
