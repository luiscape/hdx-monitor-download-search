#!/usr/bin/python
# -*- coding: utf-8 -*-

def ParseHDXQuery(data=None, fields=None):
  '''Parses data from an HDX query.'''

  if data == None or fields == None:
    print 'Data not provided. Parsing failed.'
    return False

  print 'Parsing %s results.' % len(data['result']['results'])

  #
  # Parsing the fields
  # of interest.
  #
  out = []
  for result in data['result']['results']:
    r = {}
    for field in fields:
      r[field] = result.get(field)

    #
    # When done add it back
    # to the out list.
    #
    out.append(r)


  return out
