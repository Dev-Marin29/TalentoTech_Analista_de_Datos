#Operadores aritmetico: +suma,-resta,*multiplicacion,/division,//DivEntera,**potenciacion,%residuo
#Venta de Productos

fresa = 5500  #el \n es para que, el texto que sigue después aparecerá en una nueva línea.
mango = 4800
manzana = 2500
#\n representa un salto linea dentro del print
print(f"Lista de Precios\nFresa ${fresa} Libra\nMango ${mango} Unidad\nManzana ${manzana} unidad")

#Cantidad por Productos

Cant_Fresa= float(input("Digite la cantidad de fresa a comprar >>> "))
Cant_Mango= int(input("Digite la cantidad de Mangos a comprar >>> "))
Cant_Manzana= int(input("Digite la cantidad de Manzanas a comprar >>> "))

#Total por producto - Multiplicación

Total_Fresa= fresa * Cant_Fresa
Total_Mangos= mango * Cant_Mango
Total_Manzana= manzana * Cant_Manzana
Total = Total_Fresa + Total_Mangos + Total_Manzana
print(f"Su subtotal es: {Total}")

#Calcular descuento 0 - 100

pctDesc= float(input("Digite el porcentaje de descuento(0% - 100%)>>> "))
descuento= Total * pctDesc/100
TotalConDescuento= Total - descuento
print(f"Su valor total a pagar con el descuento es: {TotalConDescuento}")