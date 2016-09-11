import unicodecsv
from datetime import datetime as dt
with open('train.csv','rb') as f:
	reader = unicodecsv.DictReader(f)
	rawTrain = list(reader)

X = []
y = []
for row in rawTrain:
	curDate = dt.strptime(row['time'], '%Y-%m-%d %H:%M:%S')
	temp = [curDate.year, curDate.month, curDate.day, curDate.hour]
	X.append(temp)
	occupancy = int(row['occupancy'])
	y.append(occupancy)


#print X
#raw_input('break')
#print y


'''
train part
'''
from sklearn.tree import DecisionTreeRegressor
clf = DecisionTreeRegressor(random_state = 0)
clf = clf.fit(X,y)


'''
predict part
'''
with open('test.csv','rb') as f:
	reader = unicodecsv.DictReader(f)
	rawTest = list(reader)
X = []
for row in rawTest:
	curDate = dt.strptime(row['time'],'%Y-%m-%d %H:%M:%S')
	temp = [curDate.year, curDate.month, curDate.day, curDate.hour]
	X.append(temp)
ans = clf.predict(X)

predictAns =[]
for i in range(len(rawTest)):
	#curDate = dt.strptime(rawTest[i]['time'],'%Y-%m-%d %H:%M:%S')
	temp = {'time':rawTest[i]['time'], 'occupancy':int(ans[i])}
	predictAns.append(temp)
#print predictAns

import json
with open('predict.json','w') as f:
	json.dump(predictAns, f, indent=4, sort_keys=True, default=lambda x:str(x))