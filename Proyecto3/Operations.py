from Products import obtener_producto

def calcular_total(lista_productos):
    total = 0
    for producto in lista_productos:
        total += producto['precio']
    return total

def agregar_producto(id_producto, cantidad, lista_productos):
    producto = obtener_producto(id_producto)
    if producto:
        lista_productos.append({"nombre": producto["nombre"], "precio": producto["precio"] * cantidad})
    else:
        raise ValueError(f"Producto con ID {id_producto} no encontrado.")