def calcular_total(ventas):
    total= 0
    for venta in ventas:
        total = total + (venta["precio"] * venta["cantidad"])
        return total