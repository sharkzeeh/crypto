import numpy as np


def eval_ma(data, window=5):
    '''
    input:
        data -- coin price list
        window -- number of points to compute average
    returns:
        mean of the latest k (window size) coin prices
            or None if there are not enough data points
    '''
    if len(data) < window:
        ...
    else:
        return np.mean(data[-5:])
