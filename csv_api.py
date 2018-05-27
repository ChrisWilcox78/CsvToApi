import argparse

from Templates.csv_processor import process_csv
from Templates.rest import app


def import_file(filename):
    process_csv(filename)


def run_test_server():
    app.run(threaded=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Turns a CSV file into an API.')
    parser.add_argument('command', metavar='Command', type=str, choices=['import', 'serve'],
                        nargs=1, help='The command to be executed (one of [import, serve])')
    parser.add_argument('-f', metavar='file', type=str, nargs=1,
                        help='The file to import from (if importing).')
    args = parser.parse_args()
    if args:
        if args.command[0] == 'import':
            if not args.f:
                parser.error('file must be provided when importing')
            import_file(args.f[0])
        elif args.command[0] == 'serve':
            run_test_server()
