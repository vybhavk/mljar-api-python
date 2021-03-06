import pandas as pd
import numpy as np
import hashlib
'''
MLJAR Constants
'''

MLJAR_TASKS = {
            'bin_class' : 'Binary Classification',
            'regression': 'Regression'
            }

MLJAR_METRICS = {
            'auc'    : 'Area Under Curve',
            'logloss': 'Logarithmic Loss',
            'rmse'   : 'Root Mean Square Error',
            'mse'    : 'Mean Square Error',
            'mae'    : 'Mean Absolute Error'
            }

MLJAR_DEFAULT_FOLDS = 5
MLJAR_DEFAULT_SHUFFLE = True
MLJAR_DEFAULT_STRATIFY = True
MLJAR_DEFAULT_TRAIN_SPLIT = None


MLJAR_BIN_CLASS = {
            "xgb"   :"Extreme Gradient Boosting",
            "lgb"   :"LightGBM",
            "rfc"   :"Random Forest",
            "rgfc"  :"Regularized Greedy Forest",
            "etc"   :"Extra Trees",
            "knnc"  :"k-Nearest Neighbor",
            "logreg":"Logistic Regression",
            "mlp"   :"Neural Network"
            }

MLJAR_REGRESSION = {
            "xgbr" :"Extreme Gradient Boosting",
            "lgbr" :"LightGBM",
            "rfr"  :"Random Forest",
            "rgfr" :"Regularized Greedy Forest",
            "etr"  :"Extra Trees"
            }

MLJAR_TUNING_MODES = {
            'Normal': {'random_start_cnt': 5, 'hill_climbing_cnt': 1},
            'Sport': {'random_start_cnt': 10, 'hill_climbing_cnt': 2},
            'Insane': {'random_start_cnt': 15, 'hill_climbing_cnt': 3}
            }

'''
MLJAR Defaults
'''
MLJAR_DEFAULT_METRICS = {
            'bin_class' : 'logloss',
            'regression': 'rmse'
            }

MLJAR_DEFAULT_ALGORITHMS = {
            'bin_class': ['xgb', 'lgb', 'mlp'],
            'regression': ['xgbr', 'lgbr']
            }

MLJAR_DEFAULT_ENSEMBLE        = True
MLJAR_DEFAULT_TUNING_MODE     = 'Normal'
MLJAR_DEFAULT_TIME_CONSTRAINT = '5' # minutes

MLJAR_OPT_MAXIMIZE = ['auc']

'''
Function to compute datasets hash, to not upload several times the same dataset.
'''
def make_hash(item):
    if isinstance(item, pd.DataFrame):
        index = tuple(item.index)
        columns = tuple(item.columns)
        values = tuple(tuple(x) for x in item.values)
        item = tuple([index, columns, values])
    elif isinstance(item, pd.Series):
        index = tuple(item.index)
        values = tuple(tuple(x) for x in item.values)
        item = tuple([index, values])
    elif isinstance(item, np.ndarray):
        return hashlib.sha1(item).hexdigest()
    try:
        return hash(item)
    except TypeError:
        try:
            # this might act funny if a thing is convertible to tuple but the tuple
            # is not a proper representation for the item (like for a frame :-()
            return hash(tuple(item))
        except TypeError as e:
            print("Unhashable type: %s" % (item))
            raise e
