import ccxt
import os
import logging

# Load API keys from environment variables
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")
COINBASE_API_KEY = os.getenv("COINBASE_API_KEY")
COINBASE_SECRET_KEY = os.getenv("COINBASE_SECRET_KEY")

# Initialize Exchange Clients
binance = ccxt.binance({
    'apiKey': BINANCE_API_KEY,
    'secret': BINANCE_SECRET_KEY,
    'enableRateLimit': True
})

coinbase = ccxt.coinbasepro({
    'apiKey': COINBASE_API_KEY,
    'secret': COINBASE_SECRET_KEY,
    'enableRateLimit': True
})

# Configure logging
logging.basicConfig(filename='trade_logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def execute_trade(action, trade_amount=0.01, paper_trading=True):
    """Executes a trade action (Buy on Binance, Sell on Coinbase, or vice versa)."""
    try:
        if action == 0:  # Buy on Binance, Sell on Coinbase
            if paper_trading:
                logging.info("Paper Trade: Buy on Binance, Sell on Coinbase")
            else:
                binance.create_market_buy_order('BTC/USDT', trade_amount)
                coinbase.create_market_sell_order('BTC/USDT', trade_amount)
                logging.info("Executed Trade: Buy on Binance, Sell on Coinbase")

        elif action == 1:  # Buy on Coinbase, Sell on Binance
            if paper_trading:
                logging.info("Paper Trade: Buy on Coinbase, Sell on Binance")
            else:
                coinbase.create_market_buy_order('BTC/USDT', trade_amount)
                binance.create_market_sell_order('BTC/USDT', trade_amount)
                logging.info("Executed Trade: Buy on Coinbase, Sell on Binance")

        else:
            logging.info("No trade executed (Hold)")
    except Exception as e:
        logging.error(f"Trade execution error: {e}")
        print(f"Trade execution error: {e}")

if __name__ == "__main__":
    execute_trade(0, paper_trading=True)  # Test trade in paper trading mode
