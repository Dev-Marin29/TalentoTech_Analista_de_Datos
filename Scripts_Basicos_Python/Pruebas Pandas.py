import pandas as pd

# Crear un DataFrame sencillo
data = {
    "Nombre": ["Ana", "Luis", "María"],
    "Edad": [23, 35, 29],
    "Ciudad": ["Bogotá", "Medellín", "Cartagena"]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nPromedio de edades:", df["Edad"].mean())
