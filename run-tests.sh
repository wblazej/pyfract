#!/bin/bash

rm=$(which rm)
python3=$(which python3)
$rm -rf $PWD/dist/ $PWD/build/
$python3 setup.py bdist_wheel
$python3 -m pip install dist/pyfract-*.whl --force-reinstall
$rm -rf $PWD/dist/ $PWD/build/
$python3 $PWD/tests/tests.py