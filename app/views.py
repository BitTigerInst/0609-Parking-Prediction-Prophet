from app import app
from flask import render_template
from flask import request

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/date",methods = ['POST'])
def get_start_date():
	form_data = request.form
	print form_data['from']
	print form_data['to']
	return "All OK"