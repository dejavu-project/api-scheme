#!/bin/bash

working_dir=$(pwd)
proto_dirs=($(pwd)/protos)  # ./protos/
python_dir=($(pwd)/src)     # ./src/

# Add execute permission to `create_dir.sh`
chmod +x ./scripts/create_dir.sh

# Create ./src/ directory
./scripts/create_dir.sh src


# Build *.proto files within the ./protos/ directory
python3 -m grpc_tools.protoc\
    --proto_path=$proto_dirs\
    --python_out=$python_dir\
    --grpc_python_out=$python_dir\
    $proto_dirs/*.proto     # ./protos/*.proto


# Find subdirectories under ./protos/
subdirectories=$(find "$proto_dirs" -mindepth 1 -maxdepth 1 -type d)

# .*proto files within subdirectories
for proto_dir in $subdirectories
do  
    src_dir="${proto_dir/protos/src}"

    # Check if the directory is empty
    if [ -z "$(ls -A "$proto_dir")" ]; then
        echo "Directory $proto_dir is empty. Skipping..."
        continue
    fi

    # Create corresponding subdirectories under ./src/
    dir="${src_dir##*/}"
    ./scripts/create_dir.sh "src/$dir"

    python3 -m grpc_tools.protoc\
        --proto_path=$proto_dir\
        --python_out=$src_dir\
        --grpc_python_out=$src_dir\
        $proto_dir/*.proto  # ./protos/<subdir>/*.proto
done