def format_time(time):
    year = time.tm_year
    mon = time.tm_mon
    day = time.tm_mday
    hr = time.tm_hour
    mnt = time.tm_min
    time = f'{day:02d}-{mon:02d}-{year:d} {hr:02d}:{mnt:02d}'
    return time
