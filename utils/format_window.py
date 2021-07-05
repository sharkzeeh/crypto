def format_window(window=5):
    if window < 60 and window > 0:
        return str(window) + 's'
    elif window < 3600 and window >= 60:
        return str(window // 60) + 'm_' + str(window % 60) + 's'
    elif window < 3600 * 24 and window >= 3600:
        return \
            str(window // 3600) + 'h_' \
            + str(window // 60 % 60) + 'm_' \
            + str(window % 60) + 's'
    else:
        raise ValueError('Incorrect value for time window has been specified! Try setting window within range [1, 86399] in file constants.py')
