'''
feature engineering
'''

import unicodecsv
from datetime import datetime as dt

with open('train.csv','rb') as f:
	reader = unicodecsv.DictReader(f)
	rawData = list(reader)



'''delete the data before 2014, add weekend check as a feature'''
data_new = []
for row in rawData:
	date = dt.strptime(row['time'], '%Y-%m-%d %H:%M:%S')
	flag = dt(2014,01,01,0,0,0)
	if date >= flag:
		temp = {'year':date.year, 'month':date.month, 'day':date.day, 'hour':date.hour, \
		 'weekend':dt(date.year, date.month, date.day).weekday() >= 5, \
		 'occupancy':row['occupancy']}
		data_new.append(temp)

keys = data_new[0].keys()
#print keys
#print data_new[0]

with open('train_new.csv','wb') as f:
	writer = unicodecsv.DictWriter(f,keys)
	writer.writeheader()
	writer.writerows(data_new)
	