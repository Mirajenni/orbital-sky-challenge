from flask import Flask
import satelliteLocation as sl
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Página Login'

@app.route('/getSatelitesFile')
def prepare_sat():
    fname = "test_list.txt"
    data = sl.get_all(fname, debug=True)
    return json.dumps(data)

@app.route('/getSatelitesNear')
def prepare_near():
    data = sl.get_near(debug = True);
    return json.dumps(data)