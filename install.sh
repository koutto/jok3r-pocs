#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y tcpdump
python3 -m pip install -r requirements-py3.txt
python2 -m pip install -r requirements-py2.txt
