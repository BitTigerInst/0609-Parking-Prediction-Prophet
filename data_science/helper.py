import unicodecsv
from datetime import datetime as dt
import datetime


def readTrain():
	with open('train_new.csv','rb') as f:
		reader = unicodecsv.DictReader(f)
		rawTrain = list(reader)

	X = []
	y = []
	for row in rawTrain:
		'''
		curDate = dt.strptime(row['time'], '%Y-%m-%d %H:%M:%S')
		temp = [curDate.year, curDate.month, curDate.day, curDate.hour]
		'''
		temp = [ int(row['year']), int(row['month']), int(row['day']), int(row['hour']), bool(row['weekend']) ]
		X.append(temp)
		occupancy = int(row['occupancy'])
		y.append(occupancy)

	return (X,y)




'''
predict part
'''
def predict(clf,outFile):

	'''new input: from -> to'''
	start = dt(2015,11,1,0,0,0)
	end = dt(2016,1,31,23,0,0)
	X = []
	while start<=end:
		temp = [start.year, start.month, start.day, start.hour, start.weekday()>=5]
		start = start + datetime.timedelta(hours=1)
		X.append(temp)
		
	ans = clf.predict(X)

	predictAns =[]
	for i in range(len(X)):
		#curDate = dt.strptime(rawTest[i]['time'],'%Y-%m-%d %H:%M:%S')
		temp = {'time':dt(X[i][0],X[i][1],X[i][2],X[i][3],0,0), 'occupancy':int(ans[i])}
		predictAns.append(temp)
	#print predictAns

	''' output predict as csv file '''
	keys = predictAns[0].keys()
	with open(outFile,'wb') as f:
		writer = unicodecsv.DictWriter(f,keys)
		writer.writeheader()
		writer.writerows(predictAns)