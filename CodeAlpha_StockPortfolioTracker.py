# 📈 CodeAlpha Internship Project - Stock Portfolio Tracker

# Hardcoded stock prices (in USD)
stock_prices = {
    "APPLE": 180,
    "TSLA": 250,
    "MICROSOFT": 330,
    "GOOGLE": 140,
    "AMAZON": 125
}

print("📊 Welcome to the CodeAlpha Stock Portfolio Tracker!")
print("Available Stocks:", ", ".join(stock_prices.keys()))

portfolio = {}

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Invalid stock symbol! Please choose from available ones.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
total_investment = 0
for stock, qty in portfolio.items():
    total_investment += stock_prices[stock] * qty

print("\n🧾 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${stock_prices[stock] * qty}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Optional — save results to file
save = input("\nDo you want to save your portfolio to a file? (y/n): ").lower()
if save == "y":
    with open("portfolio_summary.txt", "w") as f:
        f.write("Your Stock Portfolio Summary\n\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
        f.write(f"\nTotal Investment Value: ${total_investment}")
    print("✅ Portfolio saved to 'portfolio_summary.txt'!")
else:
    print("✅ Portfolio not saved. Program finished.")
