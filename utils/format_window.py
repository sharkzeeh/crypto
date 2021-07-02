def format_window(window=5):
    if window < 60:
        return str(window) + 's'
    elif window < 3600:
        return str(window // 60) + 'm_' + str(window % 60) + 's'
    elif window < 3600 * 24:
        return \
            str(window // 3600) + 'h_' \
            + str(window // 60 % 60) + 'm_' \
            + str(window % 60) + 's'
