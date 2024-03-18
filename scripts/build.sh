#!/bin/bash

working_dir=$(pwd)
proto_dirs=($(pwd)/protos)  # ./protos/
python_dir=($(pwd)/src)     # ./src/

# Create ./src/ dirctory
directory="src"
if [ ! -d "$directory" ]; then
    # Create the directory
    mkdir -p "$directory"
    echo "Directory '$directory' created successfully."
else
    echo "Directory '$directory' already exists."
fi

# Build *.proto files within the ./protos/ directory
for file in $proto_dirs/*.proto; do
    filename=$(basename "$file")
    if echo "$filename" | grep -q "struct"; then
        # Only RPC for structs
        python3 -m grpc_tools.protoc\
            --proto_path=$proto_dirs\
            --python_out=$python_dir\
            $file
    else
        # RPC and gRPC for non structs
        python3 -m grpc_tools.protoc\
            --proto_path=$proto_dirs\
            --python_out=$python_dir\
            --grpc_python_out=$python_dir\
            $file
    fi
done