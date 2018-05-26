from json import dumps

from flask import Flask, jsonify, url_for, request

from .repository import retrieve_all, get_entity, search

from .csv_processor import process_csv

from Helpers.decorators import treat_none_as_404, run_in_thread

from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.route("/")
def get_all():
    if request.args:
        search(request.args)
    return retrieve_all()


@app.route("/<string:id>")
@treat_none_as_404
def get(id):
    return get_entity(id)


@app.route("/import/", methods=["POST"])
def import_crimes():
    if request.headers["Content-Type"] == "application/json":
        filename = request.get_json()["filename"]
        if filename is None:
            raise BadRequest("filename must be provided")
        _importFromCsv(filename)
        return "Import started", 201


@run_in_thread
def _importFromCsv(filename):
    process_csv(filename)
