# Stock Portfolio Tracker - CodeAlpha Python Internship

## Project Overview
A console-based application that allows users to track their stock investments. Users can select from a list of available stocks, specify quantities, and view a detailed summary of their portfolio's value.

## Features
- **Hardcoded Stock Prices**: Uses a predefined list of stocks (AAPL, TSLA, etc.) and their prices.
- **Dynamic Portfolio Building**: Add multiple stocks and quantities in a loop.
- **Input Validation**: Ensures valid ticker symbols and positive integer quantities.
- **Formatted Summary**: Displays a clean, aligned table with individual stock totals and a grand total.
- **File Export**: Options to save the portfolio summary to both `.txt` and `.csv` files.

## How to Run
Run the script using Python:

```bash
python stock_tracker.py
```

## Python Concepts Covered
- Dictionaries for data mapping.
- Input loops and error handling (`try/except`).
- String formatting for professional console output.
- File I/O using context managers.
- Using the `csv` module for data export.
