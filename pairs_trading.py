# Statistical Arbitrage Engine
# Pairs Trading Strategy using Mean Reversion & Z-Score

import numpy as np

np.random.seed(42)

# PARAMETERS
n = 300
window = 20
entry_threshold = 1
exit_threshold = 0

# GENERATE CORRELATED ASSETS
price1 = np.cumsum(np.random.normal(0, 1, n)) + 100
price2 = price1 + np.random.normal(0, 2, n)

# COMPUTE SPREAD
spread = price1 - price2

# ROLLING MEAN
rolling_mean = np.convolve(spread, np.ones(window)/window, mode='valid')

# ROLLING STD
rolling_std = []
for i in range(len(spread) - window + 1):
    rolling_std.append(np.std(spread[i:i+window]))

rolling_std = np.array(rolling_std)

# Z-SCORE
z_score = (spread[window-1:] - rolling_mean) / rolling_std

# TRADING SIGNALS
positions = []

for z in z_score:
    if z > entry_threshold:
        positions.append(-1)   # Short spread
    elif z < -entry_threshold:
        positions.append(1)    # Long spread
    else:
        positions.append(0)    # No position

positions = np.array(positions)

# RETURNS
returns = np.diff(spread[window-1:])
strategy_returns = returns * positions[:-1]

# PERFORMANCE
cum_returns = np.cumprod(1 + strategy_returns)

# OUTPUT METRICS
print("Final Return:", cum_returns[-1])
print("Max Return:", np.max(cum_returns))
print("Min Return:", np.min(cum_returns))

