# Trading System MVP

## Overview
This is the MVP version of the trading system.

## Project Structure
- `config/`: Configuration files
- `data/`: Data storage
- `logs/`: Application logs
- `components/`: Main application modules
- `tests/`: Test suite
- `venv/`: Python virtual environment

## Setup
1. Create virtual environment: `python -m venv venv`
2. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`

## Components
- UI Module
- Data Management Module
- Strategy Management Module
- Backtesting Module
- Trading Execution Engine
- Portfolio Management Module
- Risk Management Module
- Reporting and Analytics Module
- Integration and Communication Module
- Logging and Monitoring Module

# Backtesting Module Documentation

## Overview
The backtesting module allows you to test trading strategies using historical market data. It provides functionality for:
- Running individual backtests
- Optimizing strategy parameters
- Comparing strategy performance against benchmarks
- Viewing and analyzing results

## Quick Start

1. **Running a Backtest:**
   - Navigate to the Backtest page
   - Select a strategy (e.g., Moving Average Crossover)
   - Enter ticker symbol and date range
   - Configure strategy parameters
   - Click "Run Backtest"

2. **Parameter Optimization:**
   - Check the "Optimize Parameters" option
   - The system will test multiple parameter combinations
   - Best performing parameters will be automatically selected

3. **Viewing Results:**
   - Performance metrics including returns, Sharpe ratio, and drawdown
   - Comparison against benchmark (S&P 500 by default)
   - Historical results available in the Results tab

## Default Settings
- Initial capital: $100,000
- Simulated commission rate: 0.001 (0.1%) for more realistic backtesting
- Data frequency: Daily
- Optimization limit: 100 combinations

## Notes
- Backtests use daily data for MVP version
- Resource monitoring prevents system overload
- Results are saved automatically for future reference
- The commission rate is simulated for backtesting purposes only and does not reflect actual trading costs
- Actual trading costs will vary based on your broker and trading volume

For technical documentation and API details, see the developer documentation.
