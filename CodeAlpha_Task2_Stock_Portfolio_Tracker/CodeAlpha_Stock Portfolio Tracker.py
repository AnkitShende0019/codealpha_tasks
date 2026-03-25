import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

portfolio = {}
total_value = 0

print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()
    
    if stock == "DONE":
        break
    
    if stock == "":
        print("Please enter a stock symbol.")
        continue
    
    if stock not in stock_prices:
        print("Stock not found.")
        continue
    
    try:
        qty = int(input("Enter quantity: ").strip())
        if qty <= 0:
            print("Quantity must be positive.")
            continue
        portfolio[stock] = qty
    except ValueError:
        print("Enter a valid number.")

print("\nPortfolio Summary")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock} — Qty: {qty}, Price: ${price}, Value: ${value}")

print(f"\nTotal Investment Value: ${total_value}")

with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Price", "Value"])
    
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        writer.writerow([stock, qty, price, value])
    
    writer.writerow(["", "", "Total", total_value])

print("Saved to portfolio.csv")