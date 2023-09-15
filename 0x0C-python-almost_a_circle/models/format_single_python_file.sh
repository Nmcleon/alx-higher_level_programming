#!/bin/bash

# Check if a file was provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <python_file>"
    exit 1
fi

python_file="$1"

# Check if the provided file has a .py extension
if [[ ! "$python_file" =~ \.py$ ]]; then
    echo "Error: The provided file is not a Python (.py) file."
    exit 1
fi

# Run autopep8 to automatically format the provided Python file
autopep8 --in-place "$python_file"

echo "Formatting completed for $python_file."

