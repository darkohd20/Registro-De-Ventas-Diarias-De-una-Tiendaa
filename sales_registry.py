print("╔══════════════════════════════════╗")
print("║   Welcome to store registration  ║")
print("╚══════════════════════════════════╝")
def register_sales():
    product = input("\nEnter the product name: ")
    price = float(input("Enter the unit price of the product: "))
    amount = int(input("enter the amount sold: "))
    return product, price, amount