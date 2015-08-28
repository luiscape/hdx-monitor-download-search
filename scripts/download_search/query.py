#!/usr/bin/python
# -*- coding: utf-8 -*-

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
  return data
