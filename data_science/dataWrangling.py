import unicodecsv
from datetime import datetime as dt
from datetime import timedelta

# Read Raw Data
with open('trans.csv','rb') as f:
	reader = unicodecsv.DictReader(f)
	rawData = list(reader)
#print rawData[0]

'''
Fix data type, store in separate list
'''
entryTime = []
exitTime = []
for item in rawData:
	entryTime.append(dt.strptime(item['entry_time'], '%Y-%m-%d %H:%M:%S'))
	exitTime.append(dt.strptime(item['exit_time'],'%Y-%m-%d %H:%M:%S'))
	#print item['entry_time']
entryTime.sort()
exitTime.sort()
#raw_input('break')
#print entryTime[0],entryTime[1],exitTime[0]

'''
create every hour container
'''
maxOccupancy = {}
startDate = dt(2012,12,1,5,0,0)
endDate = dt(2016,01,31,23,0,0)
date = startDate
while date <= endDate:
	maxOccupancy[date] = 0
	date += timedelta(hours=1)
	#print date
	#raw_input('break')
#print maxOccupancy.keys()

'''
create occupancy data from raw data
ocupancy is the maximum ocupancy in one hour
'''
i = 0 #idx to go through enter time
j = 0 #idx to go through exit time
curOccupancy = 0
#print len(entryTime)
#print len(exitTime)
while (i<len(entryTime) and j<len(exitTime)):
	while (i<len(entryTime) and j<len(exitTime) and entryTime[i] <= exitTime[j]):
		year = entryTime[i].year
		month = entryTime[i].month
		day = entryTime[i].day
		hour = entryTime[i].hour
		curDate = dt(year,month,day,hour,0,0) 
		curOccupancy += 1
		#print curDate
		#raw_input('break')
		if (curOccupancy > maxOccupancy[curDate]):
			maxOccupancy[curDate] = curOccupancy
		i += 1
	while (i<len(entryTime) and j<len(exitTime) and entryTime[i] > exitTime[j]):
		year = exitTime[j].year
		month = exitTime[j].month
		day = exitTime[j].day
		hour = exitTime[j].hour
		curDate = dt(year,month,day,hour,0,0)
		curOccupancy -= 1
		j += 1
#fill in the gap in maxOccupancy
temp = 0
startDate = dt(2012,12,1,5,0,0)
endDate = dt(2016,01,31,23,0,0)
date = startDate
while date <= endDate:
	if (maxOccupancy[date] != 0):
		temp = maxOccupancy[date]
	else:
		maxOccupancy[date] = temp
	date += timedelta(hours=1)

#deal with the left exit_time
while (j<len(exitTime)):
	year = exitTime[j].year
	month = exitTime[j].month
	day = exitTime[j].day
	hour = exitTime[j].hour
	curDate = dt(year,month,day,hour,0,0)
	maxOccupancy[curDate] -= 1
	j += 1

#from sortedcontainers import SortedDict
#maxOccupancy = SortedDict(maxOccupancy)

#print maxOccupancy

'''
with open('allData.csv','wb') as f:
	writer = unicodecsv.writer(f)
	for key,value in maxOccupancy.items():
		writer.writerow([key,value])
'''

'''
split data into train and test
'''
splitPoint = dt(2015,11,1,0)
train = []
test = []
startDate = dt(2012,12,1,5,0,0)
endDate = dt(2016,01,31,23,0,0)
date = startDate
while date <= endDate:
	#print date
	#print maxOccupancy
	#raw_input('break')
	item = {'time':date,'occupancy':maxOccupancy[date]}
	if date<splitPoint:
		train.append(item)
	else:
		test.append(item)
	date += timedelta(hours=1)
train = sorted(train,key=lambda k:k['time'])
test = sorted(test, key=lambda k:k['time'])

'''
transfer train/test into csv, test also into json type
'''
keys = train[0].keys()
with open('train.csv','wb') as f:
	writer = unicodecsv.DictWriter(f,keys)
	writer.writeheader()
	writer.writerows(train)

keys = test[0].keys()
with open('test.csv','wb') as f:
	writer = unicodecsv.DictWriter(f,keys)
	writer.writeheader()
	writer.writerows(test)

import json
with open('test.json','w') as f:
	json.dump(test,f,indent=4, sort_keys=True, default=lambda x:str(x))
