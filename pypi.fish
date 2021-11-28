#!/usr/bin/fish

source venv/bin/activate
rm -rf build
rm -rf dist
rm -rf *.egg-info
python3 setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/* $* 
