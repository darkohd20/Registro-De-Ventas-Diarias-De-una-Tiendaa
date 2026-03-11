def calculate_total(sales):
    total= 0
    for sale in sales:
        total = total + (sale["price"] * sale["cantidad"])
        return total