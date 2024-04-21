#!/bin/bash

working_dir=$(pwd)
proto_dirs=($(pwd)/protos)  # ./protos/
python_out=($(pwd)/protos/src/python)  # ./protos/src/python/

# Build *.proto files within the ./protobufs/ directory
for file in $(find "$proto_dirs" -type f -name "*.proto"); do
    filename=$(basename "$file")
    if echo "$filename" | grep -q "struct"; then
        # Only RPC for structs
        python3 -m grpc_tools.protoc\
            --proto_path=$proto_dirs\
            --python_out=$python_out\
            $file
    else
        # RPC and gRPC for non structs
        python3 -m grpc_tools.protoc\
            --proto_path=$proto_dirs\
            --python_out=$python_out\
            --grpc_python_out=$python_out\
            $file
    fi
done
