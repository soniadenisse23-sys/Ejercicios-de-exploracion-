import numpy as np
import matplotlib.pyplot as plt



A = np.array([
    [2, 0],
    [0, 1]
])

print("======================================")
print("EJERCICIO 1")
print("======================================")

print("\nMatriz A:")
print(A)


# Calcular eigenvalores y eigenvectores
W, V = np.linalg.eig(A)

print("\nEigenvalores de A:")
print(W)

print("\nEigenvectores de A:")
print(V)


for i in range(len(W)):

    eigenvalor = W[i]

    # El eigenvector está en la columna i de V
    eigenvector = V[:, i]

    # Producto matriz-vector
    Av = np.dot(A, eigenvector)

    # Producto eigenvalor-vector
    lambda_v = eigenvalor * eigenvector

    print("\n--------------------------------")
    print("Eigenvalor:", eigenvalor)
    print("Eigenvector:", eigenvector)

    print("\nA · v =")
    print(Av)

    print("\nlambda · v =")
    print(lambda_v)

    # Verificar si son iguales
    print("\n¿A·v = lambda·v?")

    print(np.allclose(Av, lambda_v))


plt.figure(figsize=(7, 7))

origen = np.array([0, 0])


for i in range(len(W)):

    v = V[:, i]

    Av = np.dot(A, v)

    # Eigenvector
    plt.quiver(
        origen[0],
        origen[1],
        v[0],
        v[1],
        angles='xy',
        scale_units='xy',
        scale=1,
        label=f'v{i+1}'
    )

    # Vector transformado A*v
    plt.quiver(
        origen[0],
        origen[1],
        Av[0],
        Av[1],
        angles='xy',
        scale_units='xy',
        scale=1,
        linestyle='--',
        label=f'A·v{i+1}'
    )


plt.axhline(0)
plt.axvline(0)

plt.xlim(-3, 3)
plt.ylim(-3, 3)

plt.xlabel("X")
plt.ylabel("Y")

plt.title("Eigenvectores de la matriz A")

plt.grid()

plt.legend()

plt.show()



B = np.array([
    [6, 4],
    [2, 8]
])

print("\n\n======================================")
print("EJERCICIO 2")
print("======================================")

print("\nMatriz B:")
print(B)


# Calcular eigenvalores y eigenvectores

W_B, V_B = np.linalg.eig(B)


print("\nEigenvalores de B:")
print(W_B)

print("\nEigenvectores de B:")
print(V_B)



for i in range(len(W_B)):

    eigenvalor = W_B[i]

    eigenvector = V_B[:, i]

    # B*v
    Bv = np.dot(B, eigenvector)

    # lambda*v
    lambda_v = eigenvalor * eigenvector

    print("\n--------------------------------")

    print("Eigenvalor:", eigenvalor)

    print("Eigenvector:")
    print(eigenvector)

    print("\nB · v =")
    print(Bv)

    print("\nlambda · v =")
    print(lambda_v)

    print("\n¿B·v = lambda·v?")

    print(np.allclose(Bv, lambda_v))




plt.figure(figsize=(8, 8))

origen = np.array([0, 0])


for i in range(len(W_B)):

    v = V_B[:, i]

    Bv = np.dot(B, v)

    # Eigenvector
    plt.quiver(
        0,
        0,
        v[0],
        v[1],
        angles='xy',
        scale_units='xy',
        scale=1,
        label=f'v{i+1}'
    )

    # Vector transformado
    plt.quiver(
        0,
        0,
        Bv[0],
        Bv[1],
        angles='xy',
        scale_units='xy',
        scale=1,
        linestyle='--',
        label=f'B·v{i+1}'
    )


plt.axhline(0)
plt.axvline(0)

plt.xlim(-12, 12)
plt.ylim(-12, 12)

plt.xlabel("X")
plt.ylabel("Y")

plt.title("Eigenvectores de la matriz B")

plt.grid()

plt.legend()

plt.show()
    
    