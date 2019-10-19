#!/bin/bash
echo "Building Python Extension"
c++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` src/main.cpp -o python_extension_example`python3-config --extension-suffix`

echo "Running Tests"
pytest