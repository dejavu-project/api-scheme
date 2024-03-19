#!/bin/bash

working_dir=$(pwd)
proto_dirs=($(pwd)/protos)  # ./protos/

# Build *.proto files within the ./protobufs/ directory
for file in $(find "$proto_dirs" -type f); do
    filename=$(basename "$file")
    if echo "$filename" | grep -q "struct"; then
        # Only RPC for structs
        python3 -m grpc_tools.protoc\
            --proto_path=$proto_dirs\
            --python_out=$proto_dirs\
            $file
    else
        # RPC and gRPC for non structs
        python3 -m grpc_tools.protoc\
            --proto_path=$proto_dirs\
            --python_out=$proto_dirs\
            --grpc_python_out=$proto_dirs\
            $file
    fi
done
