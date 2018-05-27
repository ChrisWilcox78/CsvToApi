# CsvToApi

Exposes the data in a CSV file via an HTTP-based API.

The aim of this project is to facilitate the interchange of data by providing an easy means by which to expose data stored in a CSV file through an API.

## How to use it

### Requirements

- A MongoDB instance
- A WSGI-compliant container to host the Flask app (a test server is built into the application)
- The Python libraries listed in `requirements.txt`

### How load a dataset

- With the appropriate Python dependencies available and a running MongoDB instance, execute `python csv_api.py import <filename>`.
- There are several environmental variables available that can be used to configure the MongoDb instance connection details:
    1. `MONGO_DB_NAME` (default is `entities`)
    2. `MONGO_HOST` (default is `localhost`)
    3. `MONGO_PORT` (default is `27017`)

### Accessing the API

- To start the test server execute `python csv_api.py serve`.
- The list of the entities loaded is available from `/`.
- Every column of the CSV is available as a query parameter using its heading (replace any spaces with `+`).
- Individual entities are available from  from `/<id>` where `<id>` is the uuid string at the heart of the object stored in the `_id` field.
