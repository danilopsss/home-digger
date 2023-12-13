#!/bin/bash

fswatch -drxt --event-flag-separator="|" . | while read file; do
    echo "File changed: $file"
    # do something here
done