#!/usr/bin/python
# -*- coding: utf-8 -*-

# system
import os
import sys

dir = os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]
sys.path.append(os.path.join(dir, 'scripts'))

# testing
import mock
import unittest
from mock import patch

# program
import download_search.query as Query
import download_search.parse as Parse
import download_search.store as Store

class TestStore(unittest.TestCase):
  '''Unit tests for storing HDX queried data in CSV.'''

  def test_store_without_fields_and_data_returns_false(self):
    assert Store.StoreCSV(data=None) == False

  def test_store_with_right_data_works(self):
    data = Query.QueryHDX(query='ebola', test=True)
    result = Parse.ParseHDXQuery(data=data, fields=['name', 'title'])
    assert Store.StoreCSV(data=result) == True

  def test_store_with_wrong_path_fails(self):
    data = Query.QueryHDX(query='ebola', test=True)
    result = Parse.ParseHDXQuery(data=data, fields=['name', 'title'])
    assert Store.StoreCSV(data=result, path='foo/bar.csv') == False


