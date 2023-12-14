#!/bin/bash

function wait_for() {
  until ping -c 1 $1 > /dev/null; do
    echo "Waiting for postgres container..."
    sleep 3
  done
}

case $APP in
  "COLLECTOR")
      wait_for sentinel
      gunicorn -w 1 collector:app -b 0.0.0.0:8001
    ;;
  "SENTINEL")
      bash /sentinel.sh
    ;;
esac