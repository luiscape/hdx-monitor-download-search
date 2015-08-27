#!/usr/bin/python
# -*- coding: utf-8 -*-

import query
import parse
import store

def Main():
  '''Wrapper.'''

  data = query.QueryHDX('cod')
  result = parse.ParseHDXQuery(data=data, fields = ['id', 'name', 'metadata_created', 'metadata_modified'])
  store.StoreCSV(result)


if __name__ == '__main__':
  Main()
