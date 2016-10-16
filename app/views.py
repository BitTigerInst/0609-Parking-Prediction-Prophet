from app import app
from app import callPredict
from flask import render_template
from flask import request
import models
import os
import json
from flask import jsonify
from datetime import datetime as dt

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/date",methods = ['GET'])
def get_date():
    beg = request.args.get('from')
    end = request.args.get('to')
    data = callPredict.getPredict(beg,end)
    print data
    '''
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data","predict.json")
    with open(json_url) as json_file:
    	data = json.load(json_file)
    '''
    return jsonify(data)

@app.route("/:month",methods=['GET'])
def pass_predict():
	predict = models.get_local_json()
	return render_template('index.html',s_data = predict);