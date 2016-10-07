from flask import Flask
from flask_restplus import Api 
from flask_restplus import fields 
from sklearn.externals import joblib

app = Flask(__name__)

'''
set up the flask app
'''
api = Api(
	app,
	version='1.0',
	title = 'Parking Prediction API',
	description = 'an API for prediction')

ns = api.namespace('occupancy',
	description = 'maximum number of car in the hour')




'''
set up the request parameters for this web service
'''
parser = api.parser()
parser.add_argument(
	'Year',
	type = int,
	required = True,
	help = 'year to predict',
	location = 'form')
parser.add_argument(
	'Month',
	type = int,
	required = True,
	help = 'month to predict',
	location = 'form')
parser.add_argument(
	'Day',
	type = int,
	required = True,
	help = 'day to predict',
	location = 'form')
parser.add_argument(
	'Hour',
	type = int,
	required = True,
	help = 'hour to predict',
	location = 'form')




'''
feed the requested parameters into the model, and predict the occupancy
'''
resource_fields = api.model('Resource', {
		'result': fields.Integer,
	})

from flask.ext.restplus import Resource
@ns.route('/')
class ParkingApi(Resource):
	@api.doc(parser=parser)
	@api.marshal_with(resource_fields)
	def post(self):
		args = parser.parse_args()
		result = self.get_result(args)
		return result,201

	def get_result(self,args):
		year = args["Year"]
		month = args["Month"]
		day = args["Day"]
		hour = args["Hour"]

		from pandas import DataFrame
		df = DataFrame([[year,month,day,hour]])

		clf = joblib.load('model/nb.pkl')

		result = clf.predict(df)
		result = result[0]

		return {
			"result": result
		}


if __name__ == '__main__':
	app.run(debug=True)
