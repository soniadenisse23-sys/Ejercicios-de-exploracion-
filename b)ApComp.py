from openpyxl import Workbook

JUGADORES = [
    [1, "Raúl Rangel"],
    [2, "Jorge Sánchez"],
    [3, "César Montes"],
    [5, "Johan Vásquez"],
    [23, "Jesús Gallardo"],
    [6, "Érik Lira"],
    [7, "Luis Romo"],
    [19, "Gilberto Mora"],
    [25, "Roberto Alvarado"],
    [9, "Raúl Jiménez"],
    [16, "Julián Quiñones"]
]

libro = Workbook()

hoja = libro.active

hoja["A1"] = "NUMERO"
hoja["B1"] = "NOMBRE"


fila = 2

for jugador in JUGADORES:

    hoja.cell(fila, 1, jugador[0])
    hoja.cell(fila, 2, jugador[1])

    fila = fila + 1


libro.save(
    r"C:\Users\DELL\OneDrive\Documentos\SELECCIÓN.xlsx"
)

print("Archivo SELECCIÓN.xlsx guardado correctamente.")
