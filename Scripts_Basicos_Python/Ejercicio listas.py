#Ejercicio Propuesto Listas
# Lista base
Productos = ["Manzana", "Platano", "Tomate"]
Eliminados = []

print("Lista inicial:", Productos)
print("Eliminados:", Eliminados)

# 1) Insertar un nuevo producto
Nuevo_producto = input("Escribe el nuevo producto de la lista: ")

if Nuevo_producto in Productos:
    print("El producto ya está registrado")
else:
    Productos.insert(0, Nuevo_producto)   # lo meto al inicio como en tu ejemplo
    print("Producto agregado:", Nuevo_producto)

print("Lista de productos:", Productos)

# 2) Eliminar producto si existe
Eliminar = input("Escribe el producto a eliminar de la lista: ")

if Eliminar in Productos:
    Productos.remove(Eliminar)
    Eliminados.insert(0, Eliminar)   # guardo en eliminados
    print("Producto eliminado:", Eliminar)
else:
    print("Producto no disponible")

print("Lista de productos:", Productos)
print("Lista de eliminados:", Eliminados)

# 3) Buscar producto y ponerlo en MAYÚSCULAS
Busca_producto = input("Producto a buscar: ")

if Busca_producto in Productos:
    indice = Productos.index(Busca_producto)   # posición
    Productos[indice] = Productos[indice].upper()
    print("Producto modificado a MAYÚSCULAS:", Productos[indice])
    print("Posición del producto:", indice)
else:
    print("Producto no disponible")

print("Lista de productos:", Productos)

# 4) Concatenar nueva lista
entrada = input("Ingresa productos adicionales separados por coma: ")
Nuevos_productos = entrada.split(",")   # separo por comas

Productos = Productos + Nuevos_productos
print("Lista concatenada:", Productos)

# 5) Repetir MANZANA 4 veces
Productos = Productos + ["MANZANA", "MANZANA", "MANZANA", "MANZANA"]
print("Lista con manzanas repetidas:", Productos)

# 6) Contar cuántas veces aparece manzana
conteo = Productos.count("Manzana") + Productos.count("MANZANA")
print("El producto 'manzana' aparece", conteo, "veces en la lista.")
