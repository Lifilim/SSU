from tabulate import tabulate
import numpy as np

def getTransposed(matr):
    transposed_iterator = zip(*matr)
    transposed_matrix = [list(row) for row in transposed_iterator]
    return transposed_matrix

def printPoints(ps, func):
    transposed_matrix = getTransposed(ps)
    transposed_matrix[0].insert(0, " " * len(func) + "  x:")
    transposed_matrix[1].insert(0, f"{func}(x):")
    print(tabulate(transposed_matrix, tablefmt="fancy_outline")) #psql

########################################################################################################################
# print("=Тест=")
# n = 4
# n = 10 ** 2
# pointsF = []
# for i in range(n):
#     pointsF.append([i, 3 * i * i - i + 100])

print("Введите количество точек: ", end='')
n = int(input())
print("Введите точки и значения в них функции f в формате \"x f(x)\" каждую пару с новой строки:")
pointsF = []
for _ in range(n):
    pointsF.append(list(map(int, input().split())))  #[x, f]
# ########################################################################################################################
print("1) Таблица для f(x):")
printPoints(pointsF, "f")
########################################################################################################################
print("2) Матрица A:")
n_ = n - 1
A = np.array([[0] * n_ * 4 for _ in range(n_ * 4)])
b = [0] * n_ * 4
h = pointsF[1][0] - pointsF[0][0]
for i in range(0, 2 * n_, 2):
    j = i * 2
    A[i][j] = 1
    b[i] = pointsF[i // 2][1]
    A[i + 1][j], A[i + 1][j + 1], A[i + 1][j + 2], A[i + 1][j + 3] = 1, h, h ** 2, h ** 3
    b[i + 1] = pointsF[i // 2 + 1][1]
for i in range(2 * n_, 2 * n_ - 2, 2):
    j = i * 2
    A[i + 1][j + 1], A[i + 1][j + 2], A[i + 1][j + 3], A[i + 1][j + 5] = 1, 2 * h, 3 * h ** 2, -1
    A[i + 1][j + 2], A[i + 1][j + 3], A[i + 1][j + 6] = 2, 6 * h, -2

A[4 * n_ - 2][2] = 2
A[4 * n_ - 1][4 * n_ - 3], A[4 * n_ - 1][4 * n_ - 2] = 2, 6 * h

Ab = getTransposed(A)
Ab.append(b)
Ab = getTransposed(Ab)
print(tabulate(Ab, tablefmt="simple_outline"))
########################################################################################################################
# done

