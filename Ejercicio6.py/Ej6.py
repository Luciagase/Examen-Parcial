import numpy as np

"Iterativa"
def determinant(mat):#toma una matriz mat como argumento y devuelve su determinante calculado con el método de eliminación de Gauss.
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

