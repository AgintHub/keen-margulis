# set_market_environment PRD

## Description
Set up the market environment for the trading workflow, including setting up trading accounts, setting up APIs, and configuring exchange links.


## Conceptual Info

The set_market_environment node is responsible for setting up the market environment for the trading workflow. This includes configuring trading accounts, APIs, and exchange links.

## Docstring

### Summary
Sets up the market environment for the trading workflow.

### Parameters

- **trading_accounts** (List[str]): List of trading accounts to set up
- **api_credentials** (dict): API credentials for configuration
- **exchanges** (List[str]): List of exchanges to configure

### Returns

dict: A dictionary containing the setup status of trading accounts, APIs, and exchange links

### Raises

- Exception: If there is an error setting up the market environment

### Examples

```python
>>> set_market_environment(trading_accounts=['account1', 'account2'], api_credentials={'api_key': 'key', 'api_secret': 'secret'}, exchanges=['exchange1', 'exchange2'])
{'trading_accounts_setup_status': True, 'api_configuration_status': True, 'exchange_links_configuration_status': True, 'configured_exchanges': ['exchange1', 'exchange2']}
```
