class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity, purchase_price):
        if symbol in self.portfolio:
            self.portfolio[symbol]['quantity'] += quantity
        else:
            self.portfolio[symbol] = {'quantity': quantity, 'purchase_price': purchase_price, 'current_price': purchase_price}
        print(f"Added {quantity} shares of {symbol} at ${purchase_price} each.")

    def update_price(self, symbol, new_price):
        if symbol in self.portfolio:
            self.portfolio[symbol]['current_price'] = new_price
            print(f"Updated {symbol} price to ${new_price}")
        else:
            print("Stock not found in portfolio.")

    def view_portfolio(self):
        print("\nStock Portfolio:")
        total_value = 0
        for symbol, data in self.portfolio.items():
            stock_value = data['quantity'] * data['current_price']
            total_value += stock_value
            print(f"{symbol}: {data['quantity']} shares | Purchase Price: ${data['purchase_price']} | Current Price: ${data['current_price']} | Value: ${stock_value}")
        print(f"Total Portfolio Value: ${total_value}\n")

if __name__ == "__main__":
    portfolio = StockPortfolio()
    
    while True:
        print("\nOptions: 1) Add Stock  2) Update Price  3) View Portfolio  4) Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            purchase_price = float(input("Enter purchase price: "))
            portfolio.add_stock(symbol, quantity, purchase_price)
        elif choice == "2":
            symbol = input("Enter stock symbol: ").upper()
            new_price = float(input("Enter new price: "))
            portfolio.update_price(symbol, new_price)
        elif choice == "3":
            portfolio.view_portfolio()
        elif choice == "4":
            print("Exiting Portfolio Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")
