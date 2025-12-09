from tabulate import tabulate
import numpy as np

K = 2


def getTransposed(matr):
    transposed_iterator = zip(*matr)
    transposed_matrix = [list(row) for row in transposed_iterator]
    return transposed_matrix

def getRounded(vec):
    return [round(vi, K) if isinstance(vi, float) else vi for vi in vec]
def getRounded2(matr):
    return [getRounded(vi) for vi in matr]

def printPoints(ps, func, arg):
    transposed_matrix = getTransposed(ps)
    transposed_matrix = getRounded2(transposed_matrix)
    transposed_matrix[0].insert(0, " " * len(func) + f"{arg}:")
    transposed_matrix[1].insert(0, f"{func}:")
    print(tabulate(transposed_matrix, tablefmt="fancy_outline"))  # psql


def printAb(Ab):
    Ab_ = []
    for i in range(n):
        Ab_.append(Ab[i].copy())
        for j in range(len(Ab_[-1])):
            Ab_[i][j] = round(Ab_[i][j], K)
        Ab_[i][n] = f"│ {Ab_[i][n]}"
    print(tabulate(Ab_, tablefmt="simple_outline"))


########################################################################################################################
# считаем, что заданная матрица имеет решения и послед сходится.
########################################################################################################################
# print("Введите матрицу A: ")
# A = [list(map(float, input().split()))]
# n = len(A[0])
# for _ in range(n - 1):
#     A.append(list(map(float, input().split())))
# A = np.array(A)
# print("Введите значения для b (в строку): ", end='')
# b = np.array([bi for bi in map(float, input().split())])
# print("Введите значения решений (в строку): ", end='')
# xxx = list(map(float, input().split()))


print("Введите размерность: ")
n = int(input())
print("Введите вариант: ")
v = float(input())
# print("Введите начальное значение для x0: ")
# x0i = float(input())

A = [[(v + i) if (i == j) else 0.01 * (v + i) for j in range(n)] for i in range(n)]
A = np.array(A)

xxx = [v+i for i in range(n)]

b = np.matmul(A, xxx)
########################################################################################################################
print("1) Матрица a:")
n = len(A)
aa = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            aa[i][j] = -A[i][j] / A[i][i]
aa = np.array(aa)
bb = np.array([b[i] / A[i][i] for i in range(n)])
########################################################################################################################
print("2) Значения x0:")
i = 0
xi = np.array([12345] * n)
print(f"x{i}: ", *xi)
########################################################################################################################
print("2) Значения xi:")
x = np.polyadd(np.matmul(aa, xi), bb)
i += 1
e = 0.1**30
while max(list(np.polysub(x, xi)), key=abs) > e:
    xi = x
    x = np.polyadd(np.matmul(aa, xi), bb)
    print(f"x{i}: ", *xi)
    i += 1
########################################################################################################################
print("3) Предел сходимости x*:")
print("x*: ", *getRounded(x))
print("достигнуто на x", i, sep='')
########################################################################################################################
