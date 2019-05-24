import pandas as pd
from hyperopt import Trials, hp, fmin, tpe, STATUS_OK
import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor
from time import time
from sklearn.model_selection import GridSearchCV

X_train = pd.read_csv('X.csv', sep=';')
y_train = pd.read_csv('y.csv', header=None)

def score(params):
	params['max_depth'] = int(params['max_depth'])
	print ("Training with params:")
	print (params)
	
	dtrain = xgb.DMatrix(X_train, label=y_train)
	r = open('hyperopt.txt','a')
	t = time()

	cvresult = xgb.cv(params, dtrain, num_boost_round=10000, nfold=3, stratified = True,
		metrics='mae', early_stopping_rounds=50, verbose_eval=100, seed=12345, shuffle=True)

	delta_t = time()-t
	print ("Time: {0}\n".format(delta_t))
	# print ("Score:\n{0}".format(avg_result.iloc[-1]))
	r.write(str(params) + ';' + \
			str(cvresult['test-mae-mean'].iloc[-1]) + ';' + \
			str(cvresult['test-mae-std'].iloc[-1]) + ';' + \
			str(cvresult['train-mae-mean'].iloc[-1]) + ';' + \
			str(cvresult['train-mae-std'].iloc[-1]) + ';' + \
			str(cvresult.shape[0]) + ';' + \
			str(delta_t) + '\n')
	r.close()
	return {'loss': cvresult['test-mae-mean'].iloc[-1], 'status': STATUS_OK}

def optimize():
	space = {
		'n_estimators' : 10000,
		'eta' : 0.01,

		# Model complexity
		'max_depth' : hp.quniform('max_depth', 1, 15, 1),
		'min_child_weight': hp.quniform('min_child_weight', 1, 100, 1),

		# Robust to noise
		'subsample' : hp.quniform('subsample', 0.1, 1.0, 0.05),
		'colsample_bytree' : hp.quniform('colsample_bytree', 0.1, 1.0, 0.05),
		'colsample_bylevel' : hp.quniform('colsample_bylevel', 0.1, 1.0, 0.05),

		# 'gamma' : hp.uniform('gamma', 0.0, 1000.0),
		# 'alpha' : hp.uniform('alpha', 0.0, 1000.0),
		# 'lambda' : hp.uniform('lambda', 0.001, 1000.0),
		'eval_metric': 'mae',
		'objective': 'reg:linear',
		'silent' : 1,
		'seed' : 12345
	}
	trials = Trials()
	best_parameters = fmin(fn=score, space=space, algo=tpe.suggest, trials=trials, max_evals=500)
	print ("Best parameters:")
	print (best_parameters)
	print ("Best result: {0}\n".format(min(trials.losses())))

optimize()