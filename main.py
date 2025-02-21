import time
from scripts.data_fetcher import get_prices
from scripts.news_scraper import fetch_news
from scripts.rl_trading_agent import TradingAgent
from scripts.trading_executor import execute_trade

# RL Agent
agent = TradingAgent()

def main():
    print("Starting BOT")
    
    while True:
        # real-time market data
        binance_price, coinbase_price = get_prices()
        
        # financial news
        news_sentiment = fetch_news()
        
        # current state for RL agent
        state = [binance_price, coinbase_price, binance_price - coinbase_price]
        
        # action prediction
        action = agent.get_action(state, news_sentiment)
        
        # execute trade
        execute_trade(action)
        
        # fetch new data every 10 seconds
        time.sleep(10)

if __name__ == "__main__":
    main()
