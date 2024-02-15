#!/bin/bash

working_dir=$(pwd)
proto_dirs=($(pwd)/protos)

for dir in $proto_dirs
do
    srcdir=$dir/protos  #./protos
    destdir=$dir/src    #./src
    echo Building $dir protos...

    python -m grpc_tools.protoc\
        -I $working_dir\
        --proto_path=$srcdir\
        --python_out=$destdir\
        --grpc_python_out=$destdir\
        $srcdir/*.proto #./protos/*.proto

done