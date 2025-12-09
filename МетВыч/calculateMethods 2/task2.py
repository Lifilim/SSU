from tabulate import tabulate
import numpy as np

K = 1

def getTransposed(matr):
    transposed_iterator = zip(*matr)
    transposed_matrix = [list(row) for row in transposed_iterator]
    return transposed_matrix

def printPoints(ps, func):
    transposed_matrix = getTransposed(ps)
    transposed_matrix[0].insert(0, " " * len(func) + "  x:")
    transposed_matrix[1].insert(0, f"{func}(x):")
    print(tabulate(transposed_matrix, tablefmt="fancy_outline")) #psql

def calcF(f, x):
    res = 0
    xx = 1
    for i in range(len(f) - 1, -1, -1):
        res += xx * f[i]
        xx *= x
    return res

########################################################################################################################
print("Введите количество точек: ", end='')
n = int(input())
print("Введите точки и значения в них функции f в формате \"x f(x)\" каждую пару с новой строки:")
pointsF = []
for _ in range(n):
    pointsF.append(list(map(float, input().split())))  #[x, f]
########################################################################################################################
print("1) Таблица для f(x):")
printPoints(pointsF, "f")
########################################################################################################################
print(f"2) L{n}(x):")
L_n = np.array([])
for i in range(n):
    denominator = 1
    numerator = np.array([1])
    for j in range(n):
        if j != i:
            denominator *= pointsF[i][0] - pointsF[j][0]
            numerator = np.polymul(numerator, np.array([1, pointsF[i][0]]))
    coefL_i = pointsF[i][1] / denominator

    L_n = np.polyadd(L_n, np.polymul(coefL_i, numerator))
n_ = len(L_n)
print(tabulate([[f"l{n_ - i - 1}" for i in range(n_)], [round(L_n[i], K) for i in range(n_)]], tablefmt="double_outline"))
########################################################################################################################
print(f"4) Заполнение таблицы для L{n}(x):")
pointsL = [pointsF[0]]
for i in range(1, n):
    x = (pointsF[i - 1][0] + pointsF[i][0]) / 2
    pointsL.append([x, round(calcF(L_n, x), K)])
    pointsL.append(pointsF[i])
printPoints(pointsL, f"L_{n}")
########################################################################################################################
# done
