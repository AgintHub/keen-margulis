# make_a_trading_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'make_a_trading_workflow' module.

## Table of Contents

- [backtest_trading_system](#backtest_trading_system)

- [create_trading_interface](#create_trading_interface)



---

## backtest_trading_system

### Description
Evaluate the trading system using historical data

### Implementation Plan

#### 1. Retrieve historical market data for the trading system using the selected market data source.

| Category | Details |
| --- | --- |
| **Reason** | This data will be used for backtesting the trading system |
| **Impact** | MEDIUM |
| **Complexity** | MEDIUM |
| **Method** | Use the API provided by the market data source to fetch historical data. |

#### 2. Calculate the technical indicators for the historical market data using the formulas specified in the technical indicators node.

| Category | Details |
| --- | --- |
| **Reason** | This will provide valuable insights into the market data. |
| **Impact** | HIGH |
| **Complexity** | HIGH |
| **Method** | Use a Python library such as Pandas to calculate the technical indicators. |

#### 3. Backtest the trading system using the historical market data and calculate the backtested performance metrics such as Sharpe ratio, max drawdown, and return on investment.

| Category | Details |
| --- | --- |
| **Reason** | This will help evaluate the trading system's performance and identify potential pitfalls. |
| **Impact** | HIGH |
| **Complexity** | HIGH |
| **Method** | Use a Python library such as Backtrader to backtest the trading system. |


---

## create_trading_interface

### Description
Develop a user interface for trading

### Implementation Plan

#### 1. Get the output from the parent node set_trading_rules by using the API call get_trading_rules().

| Category | Details |
| --- | --- |
| **Reason** | This will allow us to establish the trading rules for the system. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Use the get_trading_rules() method from the set_trading_rules node |

#### 2. Extract the trading rules, stop_loss_levels, and take_profit_levels from the output and store them in a dictionary.

| Category | Details |
| --- | --- |
| **Reason** | This will allow us to use these values in subsequent steps. |
| **Impact** | MEDIUM |
| **Complexity** | LOW |
| **Method** | Use the ExtractValuesFromDict() method from the utils library |

#### 3. Create a new dictionary with keys 'trading_interface_name', 'interface_features', 'trade_management_capabilities', 'market_data_visualization', and 'performance_analysis_tool'.

| Category | Details |
| --- | --- |
| **Reason** | This will allow us to create the output structure for this node. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use the CreateOutputDict() method from the utils library |

#### 4. Populate the output dictionary with the extracted values from the parent node and the newly created values.

| Category | Details |
| --- | --- |
| **Reason** | This will allow us to create the final output for this node. |
| **Impact** | HIGH |
| **Complexity** | MEDIUM |
| **Method** | Use the PopulateOutputDict() method from the utils library |
