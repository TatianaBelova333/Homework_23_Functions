import os

from flask import Flask, request, abort
from utils import process_request


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST', 'GET'])
def perform_query():
    cm_1 = request.values.get('cm_1')
    val_1 = request.values.get('val_1')
    cm_2 = request.values.get('cm_2')
    val_2 = request.values.get('val_2')
    file_name = request.values.get('file', ' ')
    file_path = os.path.join(DATA_DIR, file_name)
    if os.path.exists(file_path):
        data = process_request(file_path=file_path, cm_1=cm_1, val_1=val_1, cm_2=cm_2, val_2=val_2)
        return app.response_class(data, content_type="text/plain")
    else:
        abort(404, 'Requested file not found')


if __name__ == "__main__":
    app.run(debug=True)
