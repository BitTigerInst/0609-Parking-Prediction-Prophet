from flask import Flask
#from flask_restplus import Api 
#from flask_restplus import fields 
from sklearn.externals import joblib
#from flask.ext.restplus import Resource
from datetime import datetime as dt
import datetime

def getDate(beg, end):
	'''input unicode of start/end date, return date type of start/end '''
	#print type(beg) => unicode
	month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	#print beg[0:3]
	for i in range(12):
		if (beg[0:3] == month[i]):
			bmonth = i+1
			break
	bday = int(beg[4:6])
	byear = int(beg[8:12])
	bhour = 0
	start = dt(byear,bmonth,bday,bhour)

	for i in range(12):
		if (end[0:3] == month[i]):
			emonth = i+1
			break
	eday = int(end[4:6])
	eyear = int(end[8:12])
	ehour = 23
	end = dt(eyear,emonth,eday,ehour)

	return [start,end]
    

def getPredict(beg,end):
	[start,end] = getDate(beg,end)
	clf = joblib.load('model/nb.pkl')

	X = []
	#print start 
	#print end
	while start<=end:
		temp = [start.year, start.month, start.day, start.hour]
		start = start + datetime.timedelta(hours=1)
		X.append(temp)

	#print X
	result = clf.predict(X)
		
	#print result
	data = []
	for i in range(len(X)):
		temp = {'time':dt(X[i][0],X[i][1],X[i][2],X[i][3]), 'occupancy':int(result[i])}
		data.append(temp)

	return data

'''
class ParkingApi(Resource):
	@api.doc(parser=parser)
	@api.marshal_with(resource_fields)

	def get_result(self,args):
		year = args["Year"]
		month = args["Month"]
		day = args["Day"]
		hour = args["Hour"]

		from pandas import DataFrame
		df = DataFrame([[year,month,day,hour]])
'''

