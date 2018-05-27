from json import dumps
from flask import Flask, jsonify, url_for, request
from werkzeug.exceptions import BadRequest

from Helpers.decorators import treat_none_as_404
from .repository import retrieve_all, get_entity, search
from .csv_processor import process_csv


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
