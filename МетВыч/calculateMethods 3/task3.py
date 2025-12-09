from tabulate import tabulate
import numpy as np

class point:
    def __init__(self, x, f):
        self.x = x
        self.f = f
    def __init__(self, ls):
        self.x = ls[0]
        self.f = ls[1]

    def printP(self):
        print(self.x, self.f)

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
print("Введите количество точек: ", end='')
n = int(input())
print("Введите точки и значения в них функции f в формате \"x f(x)\" каждую пару с новой строки:")
pointsF = []
for _ in range(n):
    pointsF.append(list(map(int, input().split())))  #[x, f]
########################################################################################################################
print("1) Таблица для f(x):")
printPoints(pointsF, "f")
########################################################################################################################
print("2) Таблица разделенных разностей:")
TPP = [[pointsF[i][1]] + [""] * (n - 1) for i in range(n)]
for j in range(1, n):
    for i in range(n - j):
        TPP[i][j] = (TPP[i + 1][j - 1] - TPP[i][j - 1]) / 2
print(tabulate(TPP, tablefmt="simple_outline"))
########################################################################################################################
print(f"3) N{n}(x):")

########################################################################################################################
