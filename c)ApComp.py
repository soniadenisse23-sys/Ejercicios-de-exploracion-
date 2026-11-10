import pandas as pd

df = pd.read_excel(
    r"C:\Users\DELL\OneDrive\Documentos\SELECCIÓN.xlsx"
)


print("Datos del archivo:")
print(df)


JUGADORES = {}

for i in range(len(df)):

    numero = df.iloc[i, 0]
    nombre = df.iloc[i, 1]

    JUGADORES[numero] = nombre


print("\nDiccionario:")
print(JUGADORES)

df_nuevo = pd.DataFrame(
    list(JUGADORES.items()),
    columns=["NUMERO", "NOMBRE"]
)


print("\nNuevo DataFrame:")
print(df_nuevo)


df_nuevo.to_excel(
    r"C:\Users\DELL\OneDrive\Documentos\alineación.xlsx",
    index=False
)

print("\nArchivo alineación.xlsx guardado correctamente.")
