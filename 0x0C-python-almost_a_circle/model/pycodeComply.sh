#!/bin/bash

# Script to format Python code files to comply with Pycodestyle

# Define constants
IGNORED_FILES=("file_to_ignore.py" "another_file.py")
IGNORED_DIRECTORIES=("dir_to_ignore" "another_dir")

# Function that formats Python code files in a directory
format_python_directory() {
    local directory="$1"
    echo "Formatting Python files in directory: $directory"
    find "$directory" -type f -name "*.py" | while read -r file; do
        format_python_file "$file"
    done
}

# Function that formats a single Python code file
format_python_file() {
    local file="$1"
    echo "Formatting Python file: $file"
    autopep8 --in-place --aggressive --aggressive "$file"
}

# Main script
if [ $# -eq 0 ]; then
    echo "Usage: $0 <file_or_directory>"
    exit 1
fi

for item in "${IGNORED_DIRECTORIES[@]}"; do
    exclude_dirs+=" -not -path \"*/$item/*\""
done

for item in "${IGNORED_FILES[@]}"; do
    exclude_files+=" -not -name \"$item\""
done

if [ -f "$1" ]; then
    format_python_file "$1"
elif [ -d "$1" ]; then
    format_python_directory "$1"
else
    echo "Invalid input: $1 is neither a file nor a directory."
    exit 1
fi

echo "Formatting complete."
