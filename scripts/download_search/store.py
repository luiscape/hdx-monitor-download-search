#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv

dir = os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]

def StoreCSV(data=None, path='data/output.csv'):
  '''Function to store data in a CSV file.'''

  print 'Storing CSV file.'

  if data == None:
    print 'Data not provided. Storage failed.'
    return False

  #
  # Writing CSV to directory root.
  #
  path = os.path.join(dir, path)

  #
  # Write CSV file.
  #
  try:
    writer = csv.writer(open(path, 'w'))
    writer.writerow(data[0].keys())
    for row in data:
      writer.writerow(row.values())

    return True

  except Exception as e:
    print e
    print 'Could not store CSV file.'
    return False
