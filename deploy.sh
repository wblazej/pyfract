#!/bin/bash

rm=$(which rm)
python3=$(which python3)
$rm -rf $PWD/dist/ $PWD/build/
$python3 setup.py bdist_wheel
$python3 -m pip install twine
twine=$(which twine)
$twine upload $PWD/dist/*
$rm -rf $PWD/dist/ $PWD/build/