import numpy as np
import random
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

class TradingAgent:
    def __init__(self, state_size=3, action_size=3, learning_rate=0.001):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.model = self._build_model()
    
    def _build_model(self):
        """Build a simple Deep Q-Network (DQN)"""
        model = Sequential([
            Dense(64, input_dim=self.state_size, activation='relu'),
            Dense(32, activation='relu'),
            Dense(self.action_size, activation='linear')  # 3 actions: Buy, Sell, Hold
        ])
        model.compile(loss='mse', optimizer=Adam(learning_rate=self.learning_rate))
        return model

    def get_action(self, state, sentiment):
        """Predict the best action based on current state and sentiment"""
        state = np.reshape(state, [1, self.state_size])
        q_values = self.model.predict(state, verbose=0)[0]
        if sentiment == "negative":
            q_values[0] -= 10  # Penalize buying if sentiment is bad
        elif sentiment == "positive":
            q_values[1] += 10  # Reward buying if sentiment is good
        return np.argmax(q_values)  # Return best action index

if __name__ == "__main__":
    agent = TradingAgent()
    state = [60000, 60500, 500]  # Example state (Binance price, Coinbase price, spread)
    sentiment = "positive"  # Example sentiment
    action = agent.get_action(state, sentiment)
    print(f"Predicted Action: {action}")
