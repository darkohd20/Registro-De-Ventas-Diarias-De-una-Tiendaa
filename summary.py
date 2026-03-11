def show_summary(sales, total):
    print("/nDAILY SALES SUMMARY")
    for sale in sales:
        print("product:", sale["product"])
        print("amount total vendida:", sale["amount"])
        print("Total recaudado:", total)