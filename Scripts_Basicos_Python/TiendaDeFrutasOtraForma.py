#Operadores aritmetico: +suma,-resta,*multiplicacion,/division,//DivEntera,**potenciacion,%residuo
#Venta de Productos

fresa = 5500
mango = 4800
manzana = 2500
#\n representa un salto linea dentro del print
print(f"Lista de Precios\nFresa ${fresa} Libra\nMango ${mango} Unidad\nManzana ${manzana} unidad")

#Cantidad por producto
cant_fresa=float(input("Digite cantidad de fresa a comprar (Libras) >>> "))
cant_mango=int(input("Digite cantidad de mango a comprar (Unidades) >>> "))
cant_manzana=int(input("Digite cantidad de manzana a comprar (Unidades) >>> "))

#Total por producto - multiplicacion

total_fresa= fresa * cant_fresa
total_mango= mango * cant_mango
total_manzana= manzana * cant_manzana
total= total_fresa + total_mango + total_manzana
print(total)

#Calcular descuento 0 - 100

pctDesc=float(input("Digite el porcentaje de descuento(0% - 100%) >>> "))
descuento= (pctDesc/100)*total
total_descuento = total - descuento

#Creación de la Factura

print("------ Factura --------")
print("Producto  Precio unit   Cant.    Total")
print(f"Fresa     ${fresa}     {cant_fresa}Lib      ${total_fresa}")
print(f"Mango     ${mango}     {cant_mango}Unid     ${total_mango}")
print(f"Manzana   ${manzana}   {cant_manzana}Unid   ${total_manzana}")
print(f"Subtotal  ${total}")
print(f"Descuento del {pctDesc}% es ${descuento}")
print(f"Total a pagar ${round(total_descuento)}")