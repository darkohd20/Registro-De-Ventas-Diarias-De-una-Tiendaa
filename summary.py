def show_summary(sales, total):
    print("/nDAILY SALES SUMMARY")
    for sale in sales:
        print("product:", sale["product"])
        print("amount total sold:", sale["amount"])
        print("Total raised:", total)