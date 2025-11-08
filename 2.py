stock_prices={
        "APPLE":3800,
        "GOOGLE":1450,
        "HDFC":1650,
        "TCS":1550
    }

num_stocks=int(input("Enter the no of stocks you own:"))

portfolio={}
total_val=0

for i in range(num_stocks):
    stock= input(f"Enter the stock name(options:{list(stock_prices.keys())})").upper()
    quantity=int(input(f"Enter the quantity of {stock}:"))

    if stock in stock_prices:
        investment = stock_prices[stock]* quantity
        portfolio[stock]=investment
        total_val+=investment
    else:
         print(f"{stock} is not found in stock price list!!!")

print("\n-----Portfolio Summary--------")
for stock,value in portfolio.items():
    print(f"{stock}:{value}")

print(f"\n💰Total Investment Value:{total_val}")

save=input("\nDo you want to save the investment details?").lower().strip()

if save=="yes":
    try:
        with open("investment_details.txt","w",encoding="utf-8") as file:
            file.write("Stock Portfolio Summary (in Rs.)\n")
            file.write("---------------------------------\n")
            for stock,value in portfolio.items():
                file.write(f"{stock}:Rs.{value}\n")
            file.write(f"\nTotal Investment Value:Rs.{total_val}\n")
        print("✅Portfolio saved successfully to 'investment_details'")
    except Exception as e:
        print("⚠Error while saving file",e)
else:
    print("❎File is not saved")
