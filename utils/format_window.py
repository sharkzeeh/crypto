def format_window(window=5):
    if window < 60 and window > 0:
        return str(window) + 'm'
    elif window < 1439 and window >= 60:
        return str(window // 60) + 'h_' \
                + str(window % 60) + 'm'
    else:
        raise ValueError('Incorrect value for time window has been specified! Try setting window within range [1, 1439] in file constants.py')
