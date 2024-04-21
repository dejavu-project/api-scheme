#!/bin/bash

working_dir=$(pwd)
python_out=($working_dir/protos/src)

find "$python_out" -type f -name "*pb2*" -delete
