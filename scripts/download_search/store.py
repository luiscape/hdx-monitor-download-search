#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import random
import unicodecsv as csv

dir = os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]

def _random_file_name():
  '''Creates a random file name.'''
  hash = random.getrandbits(128)
  file_name = 'output_' + str(hash)[0:4] + '.csv'
  return file_name

def StoreCSV(data=None, file_name=_random_file_name()):
  '''Function to store data in a CSV file.'''

  print 'Storing CSV file.'

  if data == None:
    print 'Data not provided. Storage failed.'
    return False

  #
  # Writing CSV to directory root.
  #
  path = os.path.join(dir, 'data', file_name)

  #
  # Write CSV file.
  #
  try:
    writer = csv.writer(open(path, 'wb'))
    writer.writerow(data[0].keys())
    i = 0
    for row in data:
      try:
        writer.writerow(row.values())

      except Exception as e:
        i += 1
        print row
        print e

    if i > 0:
      return { 'path': '%s records failed to be stored.' % i, 'success': False }

    else:
      return {
        'success': True,
        'message':
        'File downloaded successfully. {records} records in file.'.format(records=len(data)),
        'file_name': file_name }

  except Exception as e:
    print e
    print 'Could not store CSV file.'
    return { 'success': False, 'message': e }
