#!/bin/bash

#
# Installing virtualenv
# and dependencies.
#
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
