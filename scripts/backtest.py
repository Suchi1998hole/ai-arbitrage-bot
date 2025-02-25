import pandas as pd
import matplotlib.pyplot as plt
import random
from scripts.rl_trading_agent import TradingAgent
from scripts.news_scraper import analyze_sentiment

# Load historical data
def load_historical_data(file_path):
    """Loads historical BTC price data."""
    return pd.read_csv(file_path)

def run_backtest(data, agent, initial_balance=10000):
    """Simulates trading strategy on historical data."""
    balance = initial_balance
    trade_log = []
    
    for index, row in data.iterrows():
        state = [row['binance_price'], row['coinbase_price'], row['binance_price'] - row['coinbase_price']]
        sentiment = analyze_sentiment([row['news_headline']]) if 'news_headline' in row else "neutral"
        action = agent.get_action(state, sentiment)
        
        if action == 0:  # Buy on Binance, Sell on Coinbase
            profit = row['coinbase_price'] - row['binance_price']
            balance += profit
            trade_log.append((index, profit, balance))
        elif action == 1:  # Buy on Coinbase, Sell on Binance
            profit = row['binance_price'] - row['coinbase_price']
            balance += profit
            trade_log.append((index, profit, balance))
        
    return trade_log, balance

def plot_results(trade_log):
    """Visualizes backtest results."""
    indices, profits, balances = zip(*trade_log)
    plt.plot(indices, balances, label='Account Balance')
    plt.xlabel('Trade Number')
    plt.ylabel('Balance ($)')
    plt.title('Backtest Performance')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    historical_data = load_historical_data('historical_prices.csv')
    agent = TradingAgent()
    trade_log, final_balance = run_backtest(historical_data, agent)
    print(f"Final Balance: ${final_balance}")
    plot_results(trade_log)
