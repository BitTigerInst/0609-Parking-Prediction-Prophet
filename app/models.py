#models.py
#deal with data
import os
from app import app


@app.route("/test",methods=['GET'])
def get_local_json():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "static/data","redict.json")
	#console.log("url is all right")
	data = json.load(open(json_url))
	return data
