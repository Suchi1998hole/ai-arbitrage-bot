# AI-Powered Arbitrage Trading with Reinforcement Learning

## Overview
This project implements a *Reinforcement Learning-based Arbitrage Trading Model, designed to exploit price differences between Binance and Coinbase. Using **Deep Q-Learning*, the model learns an optimal trading strategy to maximize profits while managing risks.

## Features
- ✅ *Deep Q-Learning for trade decision-making*  
- ✅ *Rolling spread & volatility features for better state representation*  
- ✅ *Adaptive Epsilon decay for optimized exploration vs. exploitation*  
- ✅ *Reward smoothing with EMA to prevent high variance*  
- ✅ *Stop-loss mechanism to reduce excessive drawdowns*  
- ✅ *Backtesting with 1000 trades for performance evaluation*  
 

## Installation & Setup
### 1. Clone the repository:
bash
git clone https://github.com/your-username/arbitrage-trading-rl.git
cd arbitrage-trading-rl


### 2. Install dependencies:
bash
pip install -r requirements.txt


### 3. Set up API keys for Binance and Coinbase in a .env file:
ini
BINANCE_API_KEY=your_binance_api_key
BINANCE_SECRET_KEY=your_binance_secret_key
COINBASE_API_KEY=your_coinbase_api_key
COINBASE_SECRET_KEY=your_coinbase_secret_key


### 4. Run backtesting:
bash
python backtest.py


## File Structure

📂 arbitrage-trading-rl
├── 📄 backtest.py       # Runs backtesting on historical data
├── 📄 rl_trading_agent.py  # Deep Q-learning agent
├── 📄 data_fetcher.py   # Fetches real-time crypto prices from Binance & Coinbase
├── 📄 trading_executor.py  # Executes trades
├── 📄 requirements.txt  # Python dependencies
├── 📄 README.md         # Project documentation


## Next Steps
- 🔹 Fine-tune hyperparameters for improved stability  
- 🔹 Test on real-time price data instead of historical simulations  
- 🔹 Deploy as an API-based trading bot  

## Contributing
Feel free to submit issues or open a pull request to contribute!

## License
This project is licensed under the MIT License.

---
## 📩 Connect
If you're interested in AI-driven trading, let's connect on [LinkedIn](https://linkedin.com/suchitra-hole) or collaborate on this project!

#MachineLearning #ReinforcementLearning #AITrading #CryptoTrading #QuantFinance #AlgorithmicTrading
