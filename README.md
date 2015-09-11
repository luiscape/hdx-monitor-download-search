## Download Search Results in CSV
At times an user may want to download the search results on HDX as a CSV file for post-processing somewhere else. This micro service allows you to do that.

[![Build Status](https://travis-ci.org/luiscape/hdx-monitor-download-search.svg)](https://travis-ci.org/luiscape/hdx-monitor-download-search) [![Coverage Status](https://coveralls.io/repos/luiscape/hdx-monitor-download-search/badge.svg?branch=master&service=github)](https://coveralls.io/github/luiscape/hdx-monitor-download-search?branch=master)

## Usage
The application takes two parameters: `query` and `fields`. The first is the query you want to make. The latter are the fields you would like returned in your CSV file. The search query is made on the title fields only, as it seems to produce better results.

```shell
$ curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"query":"ebola", "fields": ["id", "title", "maintainer", "creator", "metadata_created", "metadata_modified"]}' \
  localhost:3000/
```

The result will be a JSON with the path of the downloaded file:
```json
{
  "file_name": "output_2061.csv",
  "message": "File downloaded successfully. 25 records in file.",
  "records": 25,
  "success": true
}
```

## Docker Usage
When running the image, make sure you mount a volume to the data folder:

```shell
$ docker run -d \
  -v ./download_search_data:/hdx-monitor-download-search/data \
  --name download_search \
  luiscape/hdx-monitor-download-search:latest
```
