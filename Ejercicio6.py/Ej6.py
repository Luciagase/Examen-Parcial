import numpy as np

"Iterativa"
def determinante(mat):#toma una matriz mat como argumento y devuelve su determinante calculado con el método de eliminación de Gauss.
    n = len(mat)#tamaño de la matriz
    sign = 1 #signo del determinante
    det = 1 #valor absoluto del determinante
    for i in range(n):# ecorre la diagonal principal de la matriz mat y se realiza el pivoteo parcial para obtener una matriz triangular superior
        if mat[i][i] == 0:#Si en algún momento el elemento diagonal es cero, se retorna un determinante de 0.
            return 0
        for j in range(i+1, n):#Se actualiza el valor de det en cada iteración multiplicándolo por el valor del elemento diagonal actual.
            while mat[j][i] != 0:
                ratio = mat[i][i] / mat[j][i]
                for k in range(i, n):
                    mat[i][k] -= ratio * mat[j][k]
                    mat[i][k], mat[j][k] = mat[j][k], mat[i][k]
                sign *= -1#El signo del determinante se actualiza en cada iteración multiplicándolo por -1 si se realizó un intercambio de filas.
            det *= mat[i][i]#devuelve el determinante como el producto del signo y el valor absoluto del determinante.
    return sign * det

matriz = np.array([[4, 2, 3, 4, 5], [6, 7, 8, 6, 10], [11, 12, 6, 14, 15], [16, 17, 6, 9, 2], [1, 2, 2, 4, 5]])
det = determinante(matriz)
print(det)

"Recursiva"


def determinant(mat):
    n = len(mat)
    if n == 1:  # Si la matriz es de tamaño 1, su determinante es el único elemento
        return mat[0][0]
    elif n == 2:  # Si la matriz es de tamaño 2, se calcula el determinante directamente
        return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
    else:  # Si la matriz es de tamaño mayor que 2
        sign = 1  # Inicializa el signo del determinante en 1
        det = 0  # Inicializa el determinante en 0
        for j in range(n):  # Recorre cada columna de la primera fila de la matriz original
            sub_mat = np.delete(np.delete(mat, 0, axis=0), j, axis=1)  # Elimina la primera fila y la columna actual para obtener la submatriz
            sub_det = determinant(sub_mat)  # Calcula el determinante de la submatriz de forma recursiva
            det += sign * mat[0][j] * sub_det  # Calcula el determinante total sumando los determinantes parciales multiplicados por el elemento correspondiente de la primera fila, alternando su signo con cada iteración
            sign *= -1  # Alterna el signo para la siguiente iteración
        return det  # Retorna el determinante total
    
matriz = np.array([[4, 2, 3, 4, 5], [6, 7, 8, 6, 10], [11, 12, 6, 14, 15], [0, 17, 6, 9, 2], [1, 0, 0, 0, 0]])
det2 = determinant(matriz)
print(det2)