#!/bin/bash

function wait_for() {
  until ping -c 1 $1 > /dev/null; do
    echo "Waiting for $1 container..."
    sleep 3
  done
}

case $APP in
  "PROCESSOR")
      wait_for broker
      alembic upgrade head
      gunicorn -w 1 'homedigger:run()' -b 0.0.0.0:8000 --reload
    ;;
  "COLLECTOR")
      wait_for broker
      gunicorn -w 1 collector:app -b 0.0.0.0:8003
    ;;
  "DISPATCHER")
      wait_for broker
      gunicorn -w 1 dispatcher:app -b 0.0.0.0:8002
    ;;
  "SENTINEL")
      bash /sentinel.sh
    ;;
esac