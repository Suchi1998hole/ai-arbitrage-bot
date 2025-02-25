import time
from scripts.data_fetcher import get_prices
from scripts.news_scraper import fetch_news
from scripts.rl_trading_agent import TradingAgent
from scripts.trading_executor import execute_trade

agent = TradingAgent()

def main():
    print("Starting BOT")    
    while True:
        binance_price, coinbase_price = get_prices()        
        news_sentiment = fetch_news()        
        state = [binance_price, coinbase_price, binance_price - coinbase_price]        
        action = agent.get_action(state, news_sentiment)        
        execute_trade(action)        
        time.sleep(10)
        
if __name__ == "__main__":
    main()
