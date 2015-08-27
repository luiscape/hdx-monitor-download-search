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


class TestQuery(unittest.TestCase):
  '''Unit tests for testing the query to HDX.'''

  def test_query_without_parameter_returns_false(self):
    assert Query.QueryHDX(query=None, test=True) == False

  def test_query_with_parameter_returns_dict(self):
    data = Query.QueryHDX(query='ebola', test=True)
    assert type(data) is dict

