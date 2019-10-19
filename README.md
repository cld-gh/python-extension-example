# python-extension-example


## Install Notes

Install python3-dev if not already installed.
sudo apt install python3-dev
conda create --name python-extension-example python=3.6 -y
source activate python-extension-example
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -e .


# Building

```
c++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` src/main.cpp -o python_extension_example`python3-config --extension-suffix`
```
