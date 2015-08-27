#!/usr/bin/python
# -*- coding: utf-8 -*-

# system
import os
import sys
dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(os.path.join(dir, 'scripts'))

# testing
import mock
import unittest
from mock import patch

# program
import download_search.query as Query
import download_search.parse as Parse


class TestParse(unittest.TestCase):
  '''Unit tests for testing the parser for a query to HDX.'''

  def test_parser_without_fields_and_data_returns_false(self):
    assert Parse.ParseHDXQuery(data=None) == False
    assert Parse.ParseHDXQuery(fields=None) == False
    assert Parse.ParseHDXQuery(data=None, fields=['name']) == False

  def test_parser_with_data_returns_a_dict(self):
    data = Query.QueryHDX(query='ebola')
    result = Parse.ParseHDXQuery(data=data, fields=['name', 'title'])
    assert type(result) is list

