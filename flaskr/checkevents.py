from flask import request, jsonify, Flask, abort
import requests
import json
from pprint import pprint
import os
import time

# SECRET_KEY = os.environ.get("SECRET_KEY")
# if not SECRET_KEY:
#     raise ValueError("No SECRET_KEY set for Flask application")

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/db_test.yml/', methods=['GET'])
def getevents():
    response= \
"""
db_test1:
    resource_group: db_1
    tags: 
        - runner
    script:
        - sleep 30
        - echo 1
        - echo 2
"""
    return response

@app.route('/', methods=['POST'])
def postevents():
    try:
        record = json.loads(request.data)
        # pprint (record)
        # r = requests.post("http://192.168.0.73/api/v4/projects/1/trigger/pipeline",data={'token':'188372ead06795298ace49d0448aaf','ref':'master','variables[test]':'true'})
        # pprint(r,"output of requests")
        return jsonify(record)
    except:
        abort(400)

app.run(host="0.0.0.0")