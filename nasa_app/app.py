from flask import flask, render_template, jsonify
import requests

app = flask(__name__)


api_url = 'https://api.nasa.gov/'
api_key = 'Qtzb35JEnpb6CnDaa8j4hjnNnVb1nnKHwc6wsTwo'

app.route('/')

def index():
    params = {

        'api key' : api_key

    }

    response = requests.get(api_url, params=params)
    data = response.json()