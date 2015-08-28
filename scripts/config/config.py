#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json

dir = os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]

def Config(config_path='config/config.json'):
  '''Load configuration parameters.'''

  try:
    with open(os.path.join(dir, config_path)) as json_file:
      config = json.load(json_file)

  except Exception as e:
    print "Couldn't load configuration."
    print e
    return False

  return config
