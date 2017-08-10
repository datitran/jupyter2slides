import os
import argparse

from flask import Flask, request, send_from_directory

parser = argparse.ArgumentParser()
parser.add_argument('--file', dest='file_name', type=str, help='Name of the slides to run.')
args = parser.parse_args()

port = int(os.getenv('PORT', 9099))

app = Flask(__name__)


@app.route('/<path:path>')
def serve_page(path):
    return send_from_directory('static', path)


@app.route('/')
def main():
    """Adjust the presentation_name if you rename the jupyter notebook."""
    presentation_name = args.file_name.split('/')[-1]
    return app.send_static_file(presentation_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
