def url_builder(coin):
    return f'wss://stream.binance.com:9443/stream?streams={coin:s}@kline_1m'
