product_name = input("Produk name: ").title()
purchase_price = float(input("Purchase Prices: "))
order_quantity = int(input("Order Quantity: "))
total_cost = purchase_price * order_quantity

percent = input("Percent: ").split("%")
profit = (purchase_price * float(percent[0])/100 )

selling_price = purchase_price + profit
item_sold = int(input("Item sold: "))

income = item_sold * selling_price
total_profit = income - total_cost

print("="*60)

print(f"Product Name: {product_name}\nPurchase Price: {purchase_price}\nOrder Quantity: {order_quantity}\n\
Total Cost: {total_cost}\nPercent: {percent[0]}%\nProfit: {profit}\nSelling Price: {selling_price}\n\
Item sold: {item_sold}\nIncome: {income}\nTotal Profit: {total_profit}")