import websockets
import asyncio
import json
import time
from constants import window, coins
import numpy as np
from utils.url import url_builder
from utils.eval_ma import eval_ma
from utils.format_window import format_window
from utils.format_time import format_time
import csv
import aiofiles

current_coin_window = {}
connections = [url_builder(coin + 'usdt') for coin in coins]


async def handle_socket(url, csv_writer=None):
    async with websockets.connect(url) as websocket:
        while True:
            data = json.loads(await websocket.recv())
            coin = data['stream'].split('@')[0][:3].upper()
            data = data['data']
            event_time = time.localtime(data['E'] // 1000)
            event_time = format_time(event_time)
            close_price = float(data["c"])
            current_coin_window.setdefault(coin, []).append(close_price)
            ma = eval_ma(data=current_coin_window[coin][-5:], window=window)
            if ma:
                print(f'{coin:>10s} {ma:>10.2f} {event_time:>25s}')
                current_coin_window[coin] = current_coin_window[coin][1:]
                row = (coin, str(int(ma)), event_time)
                await csv_writer.writerow(row)


async def main():
    headers = ('Coin', f'MA_{format_window(window=window)}', 'Time')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>25s}')
    dashes = ('-' * 10 + ' ') * (len(headers) - 1) + '-' * 25
    print(dashes)
    async with aiofiles.open('log.csv', 'wt') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        await writer.writerow(headers)
        await asyncio.wait([handle_socket(url, writer) for url in connections])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
