import numpy as np

A = np.array([[4, 3, -5],
              [-2, -4, 5],
              [8, 8, 0]], dtype=float)

b = np.array([2,5,-3], dtype=float)

print("Matriz A:")
print(A)

print("\nVector b:")
print(b)

print("\n--VALIDACION DE DOMINANCIA DIAGONAL--")
# coeficiente diagonal

dominancia = True
for i in range(A.shape[0]):
    # Valor absoluto del elemento diagonal
    diagonal = abs(A[i, i])
    suma = np.sum(np.abs(A[i, :])) - diagonal

    print(f"\nFila {i+1}: |{A[i, i]}| = {diagonal}, ")
    print(f"Suma de los elementos fuera de la diagonal: {suma}")

    if diagonal >= suma:
        print("Cumple la condicion de dominancia diagonal")
    else:
        print("No cumple la condicion de dominancia diagonal")
        dominancia = False

if dominancia:
    print("\nLa matriz A cumple la condicion de dominancia diagonal.")
else:
    print("\nLa matriz A no cumple la condicion de dominancia diagonal.")