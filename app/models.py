#models.py
#deal with data
import os
from app import app
from flask import Flask
from flask import jsonify
import json


@app.route("/test",methods=['GET'])
def get_local_json():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "static/data","predict.json")
	#console.log("url is all right")
	#data = json.load(open(json_url,"rb"))
	#return app.response_class(data, content_type='application/json')
	with open(json_url) as json_file:
		data = json.load(json_file)
	return jsonify(data)