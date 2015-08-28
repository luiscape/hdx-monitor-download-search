#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import requests

def QueryHDX(query=None, ckan='https://data.hdx.rwlabs.org', field='title', test=False):
  '''Makes search query to HDX.'''

  if query == None:
    print 'Please provide search query.'
    return False

  #
  # Builds query string.
  #
  print 'Making query: %s' % query

  if query == '':
    print 'Fetching all datasets.'
    search = ckan + '/api/3/action/package_search?&fq='

  else:
    search = ckan + '/api/3/action/package_search?&fq=' + field + ':' + query


  #
  # Adding limit to search.
  #
  if test:
    search += '&rows=1'

  else:
    search += '&rows=1000'

  #
  # Makes query.
  #
  r = requests.get(search)
  data = r.json()

  #
  # Making recurring requests
  # if what's requested is larger
  # than 1000 results.
  #
  if data['result']['count'] > 1000:
    total = math.ceil(data['result']['count']/float(1000))
    for i in range(0, int(total)):
      i += 1
      print 'Making request %s / %s' % (i, int(total))
      r = requests.get(search + '&start=%s' % (i * 1000))
      data['result']['results'] += r.json()['result']['results']

  return data
