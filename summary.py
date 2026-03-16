def show_summary(sales, total):
    print("╔═════════════════════╗")
    print("║ DAILY SALES SUMMARY ║")
    print("╚═════════════════════╝")
    for sale in sales:
        print("\nproduct:", sale["product"])
        print("amount total sold:", sale["amount"])
    print("\nTotal raised:", total)