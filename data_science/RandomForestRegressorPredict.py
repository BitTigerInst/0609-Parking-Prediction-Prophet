'''Random Forest Regressor'''
from sklearn.ensemble import RandomForestRegressor
import helper

(X,y) = helper.readTrain()

clf = RandomForestRegressor(random_state=0)

clf = clf.fit(X,y)

helper.predict(clf, 'predict_RF.csv')

#cannot import MLPRegressor : http://scikit-learn.org/stable/developers/contributing.html#retrieving-the-latest-code