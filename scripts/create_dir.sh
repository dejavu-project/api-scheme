#!/bin/bash

# Check if the directory name is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory_name>"
    exit 1
fi

# Extract the directory name from the first argument
directory="$1"

# Check if the directory does not exist
if [ ! -d "$directory" ]; then
    # Create the directory
    mkdir -p "$directory"
    echo "Directory '$directory' created successfully."
else
    echo "Directory '$directory' already exists."
fi