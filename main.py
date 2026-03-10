from registro_de_ventas import registrar_ventas
from calcular_total import calcular_total
ventas = []
continuar = "yes"

while continuar == "yes":
    producto, precio, cantidad = registrar_ventas()

    venta = {
        "producto":producto,
        "precio": precio,
        "cantidad": cantidad,
        }
    ventas.append(venta)
    continuar = input("desea registrar otra venta? (yes/not): ")
total = calcular_total(ventas)
print("Total recaudado:",  total)
