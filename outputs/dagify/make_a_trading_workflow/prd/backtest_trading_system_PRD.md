# backtest_trading_system PRD

## Description
Evaluate the trading system using historical data


## Implementation Plan

### 1. Retrieve historical market data for the trading system using the selected market data source.

| Category | Details |
| --- | --- |
| **Reason** | This data will be used for backtesting the trading system |
| **Impact** | MEDIUM |
| **Complexity** | MEDIUM |
| **Method** | Use the API provided by the market data source to fetch historical data. |

### 2. Calculate the technical indicators for the historical market data using the formulas specified in the technical indicators node.

| Category | Details |
| --- | --- |
| **Reason** | This will provide valuable insights into the market data. |
| **Impact** | HIGH |
| **Complexity** | HIGH |
| **Method** | Use a Python library such as Pandas to calculate the technical indicators. |

### 3. Backtest the trading system using the historical market data and calculate the backtested performance metrics such as Sharpe ratio, max drawdown, and return on investment.

| Category | Details |
| --- | --- |
| **Reason** | This will help evaluate the trading system's performance and identify potential pitfalls. |
| **Impact** | HIGH |
| **Complexity** | HIGH |
| **Method** | Use a Python library such as Backtrader to backtest the trading system. |
