import pandas as pd

df = pd.read_excel(
    r"C:\Users\DELL\OneDrive\Documentos\alineación.xlsx"
)


df.insert(
    0,
    "FID",
    range(1, 12)
)


print(df)


df.to_excel(
    r"C:\Users\DELL\OneDrive\Documentos\alineación_FID.xlsx",
    index=False
)

print("\nArchivo alineación_FID.xlsx guardado correctamente.")





df = pd.read_excel(
    r"C:\Users\DELL\OneDrive\Documentos\alineación_FID.xlsx"
)


grupos = df.groupby("FID")


for fid, grupo in grupos:

    numero = grupo.iloc[0]["NUMERO"]
    nombre = grupo.iloc[0]["NOMBRE"]

    print(
        "FID:", fid,
        "Número:", numero,
        "Nombre:", nombre
    )