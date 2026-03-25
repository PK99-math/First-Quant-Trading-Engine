# Quant Risk Engine
# Monte Carlo Simulation + Value at Risk (VaR) + Expected Shortfall (ES)

import numpy as np

np.random.seed(42)

# PARAMETERS
initial_price = 100
mu = 0.0005          # expected daily return
sigma = 0.02         # volatility
days = 252           # trading days (1 year)
simulations = 1000

# MONTE CARLO SIMULATION
def simulate_prices():
    prices = np.zeros((days, simulations))
    prices[0] = initial_price

    for t in range(1, days):
        random_shock = np.random.normal(0, 1, simulations)
        prices[t] = prices[t-1] * (1 + mu + sigma * random_shock)

    return prices

# RUN SIMULATION
price_paths = simulate_prices()

# FINAL RETURNS
final_prices = price_paths[-1]
returns = (final_prices - initial_price) / initial_price

# VALUE AT RISK (VaR)
confidence_level = 0.95
VaR = np.percentile(returns, (1 - confidence_level) * 100)

# EXPECTED SHORTFALL (ES)
ES = returns[returns <= VaR].mean()

# OUTPUT
print("Monte Carlo Simulations:", simulations)
print("Mean Return:", np.mean(returns))
print("Value at Risk (95%):", VaR)
print("Expected Shortfall:", ES)
