# Estructura anidada

edad = int(input("Digite la edad >>> "))
if edad > 0 and edad < 12:
    print("Es un niño")
    adulto = input("¿Viene acompañado de un Adulto? si/no >>> ").lower() #Coloca todoen minusculas
    if adulto == "si":
        print("Por acompañante puede usar las atracciones.")
    else:
        print("No puede usar las atracciones")
else:
    print("Puede usar las atracciones")
