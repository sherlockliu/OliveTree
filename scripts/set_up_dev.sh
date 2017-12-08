#!/usr/bin/env bash

## Python 3 ##
echo "-> Installing python3 ..."
#brew install python3

## Pip Installs ##
echo "-> Installing virtualenv..."
pip3 install virtualenv

echo "-> Creating virtualenv..."
virtualenv --setuptools --no-site-packages --prompt="(${PWD##*/}) " -p python3 .venv

echo "-> Activating virtualenv"
source .venv/bin/activate

echo "Upgrading and installing pip dependencies"
pip3 install --upgrade pip
pip3 install --upgrade setuptools
pip3 install -r requirements.txt
deactivate
echo "-> Pip dependencies install complete!"