#!/bin/bash

# WAIT FOR DATABASE GOES UP
until ping -c 1 database > /dev/null; do
    echo "Waiting for postgres container..."
    sleep 1
done

# RUN ALEMBIC UPGRADE HEAD
# pushd / > /dev/null
# alembic upgrade head

# popd  > /dev/null

tail -f /dev/null