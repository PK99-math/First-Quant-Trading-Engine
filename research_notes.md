# Quant Research Notes

## 1. Objective
Develop quantitative trading strategies and risk models using statistical and probabilistic techniques.

---

## 2. Strategy: Pairs Trading (Statistical Arbitrage)

### Concept
Pairs trading exploits temporary deviations between two correlated assets. The assumption is that the spread between the assets is mean-reverting.

### Implementation
- Generate two correlated price series
- Compute spread = price1 - price2
- Normalize using Z-score

### Signal Logic
- Z-score > 1 → Short spread
- Z-score < -1 → Long spread
- Otherwise → No position

### Observations
- Strategy performance depends heavily on window size
- Threshold selection impacts trade frequency and profitability

---

## 3. Risk Modeling

### Monte Carlo Simulation
Used to simulate multiple future price paths under uncertainty.

### Value at Risk (VaR)
Estimates the maximum expected loss at a given confidence level.

### Expected Shortfall (ES)
Measures the average loss in the worst-case scenarios.

---

## 4. Key Insights
- Markets exhibit stochastic behavior
- Risk management is as important as strategy design
- Parameter tuning significantly affects outcomes

---

## 5. Future Improvements
- Use real market data instead of simulated data
- Implement portfolio-level strategies
- Introduce transaction costs and slippage
- Optimize strategy parameters using data-driven methods
