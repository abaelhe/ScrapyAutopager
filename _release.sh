#!/bin/sh

python -m autopager train autopager/data autopager/autopager.crf
./setup.py sdist
./setup.py bdist_wheel
