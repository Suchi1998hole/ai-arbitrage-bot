import ccxt
#rel time prices
def get_prices():
    try:
        binance = ccxt.binance()
        coinbase = ccxt.coinbasepro()       
        binance_price = binance.fetch_ticker('BTC/USDT')['last']
        coinbase_price = coinbase.fetch_ticker('BTC/USDT')['last']       
        return binance_price, coinbase_price    
    except Exception as e:
        print(f"Error fetching prices: {e}")
        return None, None
if __name__ == "__main__":
    binance_price, coinbase_price = get_prices()
    print(f"Binance BTC Price: ${binance_price}, Coinbase BTC Price: ${coinbase_price}")
