'''cross validation'''
import unicodecsv

'''read the data of test'''
with open('test.csv') as f:
	reader = unicodecsv.DictReader(f)
	test = list(reader)


def compare(filename):
	with open(filename) as f:
		reader = unicodecsv.DictReader(f)
		predict = list(reader)

	ans = 0.0

	for (p,t) in zip(predict,test):
		a = float(p['occupancy'])
		b = float(t['occupancy'])
		if a>b:
			ans = ans + b/a
		else:
			ans = ans + a/b

	ans = ans / len(predict)
	print ans



'''Decision Tree Regressor with initial feature
compare('predict_old_DT.csv')
#0.521353445521
'''

'''Decision Tree Regressor with modified feature
compare('predict_DT.csv')
#0.521353445521
'''

'''Gradient Boosting Regressor with modified feature
compare('predict_GB.csv')
#0.434052402536
'''

'''Random Forest Regressor with modified feature
compare('predict_RF.csv')
#0.52851447931
'''

