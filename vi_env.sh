#!/bin/bash

echo "installing venv lib"
sudo apt install python3-venv

echo "creating $1 environment"
python3 -m venv $1

echo "command to activate $ environment"
echo " $ source $1/bin/activate"


