#!/bin/bash

# Ensure Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Loading..."
    apk add python3 py3-pip
fi

# Run the Python script
python3 reaper.py
