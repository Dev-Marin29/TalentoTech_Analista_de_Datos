#Operadores Relacionales - Logicos
#Parque de Diversiones - quien puede utilizar las atracciones
#R1: debe medir mas de 120cm
#R2: Si es menor de 12 años, debe acompañarlo un adulto
#Zona VIP: compro el pase VIP, o Abono es más de 50000

# Vamos a pedir estatura, la edad, si es adulto, pase vip y la recarga!

estatura = int(input("Digite su estatura >>>"))
edad = int(input("Digite su edad >>>"))
adulto = input("¿Viene acompañado de un Adulto? si/No >>> ").lower() #te muestra todo en minuscula
adulto = adulto=="si"
print(adulto)
pase_vip = input("¿Compró pase VIP? si/no >>> ").upper() #te muestra el texto en mayuscula
pase_vip = pase_vip=="SI"
print(pase_vip)
recarga = int (input("Digite el valor de su recarga >>>"))

requisito_1 = estatura>120
#print("¿Cumple con la estatura? ",requisito_1)
print(f"¿Cumple con la estatura? {requisito_1}")
requisito_2 = edad>=12 or adulto==True
print(f"¿Cumple con la edad o acompañante? {requisito_2}")
usar_atracciones = requisito_1==True and requisito_2==True #True and True -False and True
print(f"Puedes disfrutar de las atracciones: {usar_atracciones}")
zona_vip = pase_vip==True or recarga>50000
print(f"Puedes disfruta de la zona VIP {zona_vip}")