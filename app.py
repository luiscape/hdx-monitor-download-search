#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from flask import *
from scripts.download_search import *

__version__ = 'v.0.1.1'

app = Flask(__name__)

with open('config/config.json') as json_file:
  config = json.load(json_file)

@app.route('/status', methods=['GET'])
def ServerStatus():
  '''Serves the status of the service in JSON.'''

  status = {
    'online': True,
    'message': config['description'],
    'CKAN_instance': config['CkanInstance'],
    'version': config['version'],
    'repository': config['repository']
  }
  return jsonify(**status)

@app.route('/', methods=['POST'])
def QueryParseAndProvideLink():
  '''
  Makes a query to the CKAN instance, parses the output,
  and creates a CSV file. It returns a status message,
  together with a download link directly to the file system.
  '''

  #
  # The following is a method
  # to convert a form payload
  # into a dictionary object.
  #
  # request_data = dict(
  #   (key, request.form.getlist(key)
  #     if len(request.form.getlist(key)) > 1
  #     else request.form.getlist(key)[0]) for key in request.form.keys()
  #   )

  request_data = request.get_json()

  if 'fields' in request_data.keys():
    query_fields = request_data['fields']

  else:
    query_fields=['id', 'title']

  #
  # Query CKAN, parse results,
  # and store output.
  #
  ckan_payload = query.QueryHDX(query=request_data['query'])
  results = parse.ParseHDXQuery(data=ckan_payload, fields=query_fields)
  out = store.StoreCSV(data=results)

  return jsonify(**out)


if __name__ == '__main__':
    app.run(
      host='0.0.0.0',
      port=config['port']
      )
