import numpy as np


a = np.array([[8, 3, -3], [-2, -8, 5], [3, 5, 10]], dtype=float)

# coeficiente de la diagonal
# diagonal principal: |a_ii|
diagonal = np.diag(np.abs(a))

# suma de los elementos fuera de la diagonal en cada fila
off_diag = np.sum(np.abs(a), axis=1) - diagonal

if np.all(diagonal > off_diag):
    print('DIAGONALMENTE DOMINANTE')
else:
    print('NO ES DIAGONALMENTE DOMINANTE')

x = np.array([0.0, 0.0, 0.0], dtype=float)
epsilon = 0.01
converged = False

print('RESULTADOS DE LA ITERACION')
print(' k, x1, x2, x3 ')

for k in range(1, 25):
    x_anterior = x.copy()

    # Método de Jacobi para el sistema:
    # 8x1 + 3x2 - 3x3 = 14
    # -2x1 - 8x2 + 5x3 = 5
    # 3x1 + 5x2 + 10x3 = -8
    # variables despejadas
    x1 = (14 - 3 * x_anterior[1] + 3 * x_anterior[2]) / 8
    x2 = (-5 - 2 * x_anterior[0] + 5 * x_anterior[2]) / 8
    x3 = (-8 - 3 * x_anterior[0] - 5 * x_anterior[1]) / 10

    x = np.array([x1, x2, x3], dtype=float)
    print(f"{k:2d}, {x[0]:.4f}, {x[1]:.4f}, {x[2]:.4f}")

    if np.linalg.norm(x - x_anterior, ord=np.inf) < epsilon:
        converged = True
        print(f'Convergencia alcanzada en la iteracion {k}.')
        break

if not converged:
    print('No se alcanzó convergencia en 24 iteraciones.')
        
        

