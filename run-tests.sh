#!/bin/bash

RM_PATH=$(which rm)
PYTHON3_PATH=$(which python3)
PATH=$(pwd)
$RM_PATH -rf $PATH/dist/ $PATH/build/
$PYTHON3_PATH setup.py bdist_wheel
$PYTHON3_PATH -m pip install dist/pyfract-*.whl --force-reinstall
$PYTHON3_PATH $PATH/tests/tests.py