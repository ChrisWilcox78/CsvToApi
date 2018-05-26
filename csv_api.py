from Templates.csv_processor import process_csv
from Templates.rest_template import app


def import_file(filename):
    process_csv(filename)


def run_server():
    app.run(debug=True, threaded=True)
