#!/bin/bash

working_dir=$(pwd)
proto_dirs=($(pwd)/protos)  # ./protos/

# Find all files with `pb2` and delete them
find "$proto_dirs" -type f -name "*pb2*" -delete
