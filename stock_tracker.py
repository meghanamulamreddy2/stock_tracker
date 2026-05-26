"""
Filename: stock_tracker.py
Description: A console-based Stock Portfolio Tracker that allows users to track their investments.
Author: [Your Name]
Date: 2026-05-12
"""

import csv

def display_available_stocks(prices):
    """
    Displays the available stocks and their current prices in a formatted table.
    Args:
        prices (dict): A dictionary mapping ticker symbols to prices.
    """
    print("\n--- Available Stocks ---")
    print(f"{'Ticker':<10} | {'Price':>10}")
    print("-" * 23)
    for ticker, price in prices.items():
        print(f"{ticker:<10} | ${price:>9.2f}")
    print("-" * 23)

def get_user_portfolio(prices):
    """
    Handles the user input loop to build a portfolio.
    Args:
        prices (dict): A dictionary of available stock prices.
    Returns:
        dict: A dictionary where keys are tickers and values are quantities.
    """
    portfolio = {}
    print("\nEnter your stocks. Type 'done' when you are finished.")
    
    while True:
        ticker = input("Enter Stock Ticker (or 'done'): ").strip().upper()
        
        if ticker == 'DONE':
            break
            
        if ticker not in prices:
            print(f"Error: '{ticker}' is not available. Please choose from the list.")
            continue
            
        try:
            qty_input = input(f"Enter quantity for {ticker}: ").strip()
            qty = int(qty_input)
            if qty <= 0:
                print("Error: Quantity must be a positive integer.")
                continue
            
            # If ticker already exists, add to existing quantity
            portfolio[ticker] = portfolio.get(ticker, 0) + qty
        except ValueError:
            print("Error: Invalid input. Please enter a whole number for quantity.")
            
    return portfolio

def calculate_portfolio(portfolio, prices):
    """
    Computes the total value for each stock and returns data for the summary.
    Args:
        portfolio (dict): User's portfolio {ticker: qty}.
        prices (dict): Price dictionary.
    Returns:
        tuple: (list of dicts with stock details, grand total value)
    """
    portfolio_data = []
    grand_total = 0.0
    
    for ticker, qty in portfolio.items():
        price = prices[ticker]
        total_value = qty * price
        grand_total += total_value
        
        portfolio_data.append({
            "ticker": ticker,
            "qty": qty,
            "price": price,
            "total": total_value
        })
        
    return portfolio_data, grand_total

def display_summary(portfolio_data, grand_total):
    """
    Prints a formatted Portfolio Summary table to the console.
    Args:
        portfolio_data (list): List of dicts containing stock details.
        grand_total (float): The total value of all stocks.
    """
    print("\n  ╔" + "═" * 38 + "╗")
    print("  ║" + "STOCK PORTFOLIO SUMMARY".center(38) + "║")
    print("  ╠" + "═" * 38 + "╣")
    print(f"  ║  {'Stock':<7} {'Qty':<5} {'Price':<10} {'Total':<11} ║")
    
    for item in portfolio_data:
        ticker = item['ticker']
        qty = item['qty']
        price = f"${item['price']:,.2f}"
        total = f"${item['total']:,.2f}"
        print(f"  ║  {ticker:<7} {qty:<5} {price:<10} {total:<11} ║")
        
    print("  ╠" + "═" * 38 + "╣")
    print(f"  ║  GRAND TOTAL:           ${grand_total:>13,.2f} ║")
    print("  ╚" + "═" * 38 + "╝")

def save_to_txt(portfolio_data, grand_total, filename):
    """
    Saves the portfolio summary to a text file.
    Args:
        portfolio_data (list): Portfolio details.
        grand_total (float): Total value.
        filename (str): Name of the file.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("STOCK PORTFOLIO SUMMARY\n")
            f.write("=" * 40 + "\n")
            f.write(f"{'Stock':<10} {'Qty':<10} {'Price':<10} {'Total':<10}\n")
            for item in portfolio_data:
                f.write(f"{item['ticker']:<10} {item['qty']:<10} ${item['price']:<9.2f} ${item['total']:<9.2f}\n")
            f.write("=" * 40 + "\n")
            f.write(f"GRAND TOTAL: ${grand_total:,.2f}\n")
        print(f"Successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving to txt: {e}")

def save_to_csv(portfolio_data, filename):
    """
    Saves the portfolio summary to a CSV file.
    Args:
        portfolio_data (list): Portfolio details.
        filename (str): Name of the file.
    """
    try:
        keys = ["ticker", "qty", "price", "total"]
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(portfolio_data)
        print(f"Successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving to csv: {e}")

def main():
    """
    Main entry point for the Stock Portfolio Tracker.
    Orchestrates the workflow.
    """
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 320,
        "AMZN": 175,
        "NFLX": 480,
        "META": 300
    }
    
    print("Welcome to the Stock Portfolio Tracker!")
    display_available_stocks(stock_prices)
    
    portfolio = get_user_portfolio(stock_prices)
    
    if not portfolio:
        print("\nYour portfolio is empty. Goodbye!")
        return
        
    portfolio_data, grand_total = calculate_portfolio(portfolio, stock_prices)
    display_summary(portfolio_data, grand_total)
    
    save_choice = input("\nWould you like to save this summary? (y/n): ").strip().lower()
    if save_choice == 'y':
        save_to_txt(portfolio_data, grand_total, "portfolio_summary.txt")
        save_to_csv(portfolio_data, "portfolio_summary.csv")
    
    print("\nThank you for using the Stock Portfolio Tracker!")

if __name__ == "__main__":
    main()
