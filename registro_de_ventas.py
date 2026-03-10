def registrar_ventas():
    producto = input("ingrese el nombre del producto: ")
    precio = float(input("ingrese el precio unitario del producto: "))
    cantidad = float(input("ingrese la cantidad vendida: "))
    return producto, precio, cantidad