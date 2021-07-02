import websockets
import asyncio
import json
import time
from constants import window, coins
import numpy as np
from utils.url import url_builder


current_coin_window = {}
connections = [url_builder(coin + 'usdt') for coin in coins]


def eval_ma(data, window=window):
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


async def handle_socket(url):
    async with websockets.connect(url) as websocket:
        while True:
            data = json.loads(await websocket.recv())
            coin = data['stream'].split('@')[0][:3].upper()
            data = data['data']
            event_time = time.localtime(data['E'] // 1000)
            event_time = f'{event_time.tm_hour:02d}:{event_time.tm_min:02d}:{event_time.tm_sec:02d}'
            close_price = int(float(data["c"]))
            current_coin_window.setdefault(coin, []).append(close_price)
            ma = eval_ma(current_coin_window[coin][-5:])
            if ma:
                print(f'{coin:>10s} {int(ma):>10d} {event_time:>10s}')


async def main():
    await asyncio.wait([handle_socket(url) for url in connections])


def count_window(window=window):
    if window < 60:
        return str(window) + 's'
    elif window < 3600:
        return str(window // 60) + 'm ' + str(window % 60) + 's'
    elif window < 3600 * 24:
        return str(window // 3600) + 'h ' + str(window // 60 % 60) + 'm ' + str(window % 60) + 's'


if __name__ == '__main__':
    
    headers = ('Coin', f'MA ({count_window()})', 'Time')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s}')
    dashes = ('-' * 10 + ' ') * len(headers)
    print(dashes)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
