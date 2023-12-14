#!/bin/bash

fswatch /tmp/html --event=Created | while read file; do
    echo "File created...$file"
done
