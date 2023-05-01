#Soluções computacionais de sistemas lineares são necessárias, por exemplo, em aplicações ou em 
#problemas reais de grande porte, onde invariavelmente nos deparamos com matrizes de grandes dimensões.
#Sendo assim, implemente computacionalmente os algoritmos abaixo para resolver Ax=b, se A estiver 
#na forma escalonada triangular superior ou triangular inferior. Caso contrário, aplicar a fatoração LU em A 
#(Ver pág. 131 - Pulino [8]; Ver também exercício 24, pág. 70 - Anton [1]). Em seguida, resolva o sistema 
#fatorado por algum método de substituição avançada ou atrasada (ver algoritmos pág. 129 - Pulino [8])

import numpy as np


def lu_decomposition(A):
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy()
    for j in range(n-1):
        for i in range(j+1, n):
            L[i, j] = U[i, j] / U[j, j]
            U[i, j:] = U[i, j:] - L[i, j] * U[j, j:]
    return L, U

def forward_substitution(L, b):
    n = L.shape[0]
    x = np.zeros(n)
    for i in range(n):
        s = 0
        for j in range(i):
            s += L[i, j] * x[j]
        x[i] = (b[i] - s) / L[i, i]
    return x

def backward_substitution(U, y):
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        s = 0
        for j in range(i+1, n):
            s += U[i, j] * x[j]
        x[i] = (y[i] - s) / U[i, i]
    return x

def solve_lu():
    n = int(input("Digite a ordem da matriz A: "))
    A = np.zeros((n, n))
    print("Digite os elementos da matriz A:")
    for i in range(n):
        A[i, :] = input().split()
    b = np.zeros(n)
    print("Digite os elementos do vetor b:")
    b[:] = input().split()
    L, U = lu_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x

x = solve_lu()

print("Solução:")
print(f"X^(t) ={x}") #resultado é a matriz transposta
