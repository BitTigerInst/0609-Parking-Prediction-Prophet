from app import app
from flask import render_template
from flask import request
import models

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/date",methods = ['POST'])
def get_date():
	form_data = request.form
	print form_data['from']
	print form_data['to']
	return "All OK"


@app.route("/:month",methods=['GET'])
def pass_predict():
	predict = models.get_local_json()
	return render_template('index.html',s_data = predict);