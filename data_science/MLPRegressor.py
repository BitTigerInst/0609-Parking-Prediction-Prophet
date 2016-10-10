''' Multi-layer Perceptron Regressor'''
#http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor
from sklearn.neural_network import MLPRegressor
import helper

helper.readTrain()
X = helper.X
y = helper.y

clf = MLPRegressor(hidden_layer_sizes=(100, ), activation='relu', solver='adam', alpha=0.0001,\
 batch_size='auto', learning_rate='constant', learning_rate_init=0.001, power_t=0.5, max_iter=200, \
 shuffle=True, random_state=None, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, \
 nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

helper.predict(clf, 'predict_NN.csv')

#cannot import MLPRegressor : http://scikit-learn.org/stable/developers/contributing.html#retrieving-the-latest-code