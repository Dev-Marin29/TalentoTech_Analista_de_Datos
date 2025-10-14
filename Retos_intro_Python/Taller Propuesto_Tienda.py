#Calculadora Tienda de Barrio
# Inicializamos el total de la compra en 0
TOTAL = 0  

while True:
    # Pedir datos al tendero
    VALOR_UNITARIO = float(input("Ingrese el valor unitario del producto (sin IVA): "))
    TIENE_IVA = input("¿El producto tiene IVA? (S/N): ").upper()
    CANTIDAD = int(input("Ingrese la cantidad de productos: "))

    # Calcular subtotal según tenga o no IVA
    if TIENE_IVA == "S":
        SUBTOTAL = VALOR_UNITARIO * CANTIDAD * 1.19
        print("IVA incluido")
    else:
        SUBTOTAL = VALOR_UNITARIO * CANTIDAD
        print("PRODUCTO SIN IVA")

    # Mostrar subtotal
    print(f"SUBTOTAL: {SUBTOTAL}")

    # Acumular el total
    TOTAL = TOTAL + SUBTOTAL

    # Preguntar si faltan productos
    MAS_PRODUCTOS = input("¿Faltan productos por cobrar? (S/N): ").upper()
    if MAS_PRODUCTOS == "N":
        break  # salir del ciclo

# Mostrar el total final
print(f"TOTAL A COBRAR: {TOTAL}")

