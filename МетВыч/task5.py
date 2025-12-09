from tabulate import tabulate
import numpy as np

K = 2

def getTransposed(matr):
    transposed_iterator = zip(*matr)
    transposed_matrix = [list(row) for row in transposed_iterator]
    return transposed_matrix

def printPoints(ps, func):
    transposed_matrix = getTransposed(ps)
    transposed_matrix[0].insert(0, " " * len(func) + "  x:")
    transposed_matrix[1].insert(0, f"{func}(x):")
    print(tabulate(transposed_matrix, tablefmt="fancy_outline")) #psql

def printAb(Ab):
    Ab_ = []
    for i in range(n):
        Ab_.append(Ab[i].copy())
        for j in range(len(Ab_[-1])):
            Ab_[i][j] = round(Ab_[i][j], K)
        Ab_[i][n] = f"│ {Ab_[i][n]}"
    print(tabulate(Ab_, tablefmt="simple_outline"))

########################################################################################################################
print(f"=Тест вариант №{(v := 2)}=")
n = 5
A = np.array([ [(v + i) * (1 if i == j else 0.01) for j in range(n)] for i in range(n) ])
b = np.matmul(A, [2, 3, 4, 5, 6]) # [4.36, 9.51, 16.64, 25.75, 36.84]
#
# print("Введите матрицу A: ")
# A = [list(map(float, input().split()))]
# n = len(A[0])
# for _ in range(n - 1):
#     A.append(list(map(float, input().split())))
# A = np.array(A)
# print("Введите значения для b (в строку): ", end='')
# b = np.array([ai for ai in map(float, input().split())])
########################################################################################################################
# Предполагаем, что на главной диагональ нет нулей
########################################################################################################################
print("1) Матрица (A|b):")
Ab = getTransposed(A)
Ab.append(b)
Ab = getTransposed(Ab)
printAb(Ab)
########################################################################################################################
print("2) Матрица (A|b) после прямого хода МГ:")
for i in range(n):
    for j in range(i + 1, n + 1):
        Ab[i][j] /= Ab[i][i]
    Ab[i][i] = 1
    for ii in range(i + 1, n):
        for j in range(i + 1, n + 1):
            Ab[ii][j] -= Ab[i][j] * Ab[ii][i]
        Ab[ii][i] = 0
printAb(Ab)
########################################################################################################################
print("3) Матрица (A|b) после обратного хода МГ:")
for i in range(n - 1, -1, -1):
    for ii in range(i - 1, -1, -1):
        Ab[ii][n] -= Ab[i][n] * Ab[ii][i]
        Ab[ii][i] = 0
printAb(Ab)
########################################################################################################################
# done
