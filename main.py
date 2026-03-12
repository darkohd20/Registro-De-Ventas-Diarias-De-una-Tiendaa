from sales_registry import register_sales
from calculate_total import calculate_total
from summary import show_summary
sales = []
continue01 = "yes"

while continue01 == "yes":
    product, price, amount = register_sales()

    sale = {
        "product":product,
        "price": price,
        "amount": amount,
        }
    sales.append(sale)
    continue01 = input("Do you want to register another sale? (yes/no): ")
total = calculate_total(sales)
show_summary(sales,total)