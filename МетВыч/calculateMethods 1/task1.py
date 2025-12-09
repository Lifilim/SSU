from tabulate import tabulate
import numpy as np

K = 3

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
print("2) Вспомогательная СЛАУ в виде расширенной матрицы:")
A = [[1] * n for _ in range(n)]
for i in range(n):
    for j in range(n - 2, -1, -1):
        A[i][j] = A[i][j + 1] * pointsF[i][0]
Anp = np.array(A)
print(tabulate(Anp, tablefmt="simple_outline"))
########################################################################################################################
print("3) Решения СЛАУ:")
D = float(np.linalg.det(Anp))
coefs = [0] * n
for j in range(n):
    for i in range(n):
        Anp[i][j] = pointsF[i][1]
    coefs[j] = float(np.linalg.det(Anp)) / D
    for i in range(n):
        if j == n - 1:
            Anp[i][j] = 1
        else:
            Anp[i][j] = Anp[i][j + 1] * pointsF[i][0]
print(tabulate([[f"a{n - i - 1}" for i in range(n)], [round(coefs[i], K) for i in range(n)]], tablefmt="double_outline"))
########################################################################################################################
print("4) Заполнение таблицы для P(x):")
pointsP = [pointsF[0]]
for i in range(1, n):
    x = (pointsF[i - 1][0] + pointsF[i][0]) / 2
    pointsP.append([x, calcF(coefs, x)])
    pointsP.append(pointsF[i])
printPoints(pointsP, "P")
########################################################################################################################
# done
