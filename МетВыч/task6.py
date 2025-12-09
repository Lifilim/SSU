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
print(f"=Тест вариант №{(v := 2)}=")
n = 5
A = [[(v + i) * (i == j) for j in range(n)] for i in range(n)]
for i in range(n):
    if i > 0:
        A[i][i - 1] = A[i][i] * 0.01
    if i + 1 < n:
        A[i][i + 1] = A[i][i] * 0.01
A = np.array(A)
b = np.matmul(A, [2, 3, 4, 5, 6])

# print("Введите матрицу A: ")
# A = [list(map(float, input().split()))]
# n = len(A[0])
# for _ in range(n - 1):
#     A.append(list(map(float, input().split())))
# A = np.array(A)
# print("Введите значения для b (в строку): ", end='')
# b = np.array([ai for ai in map(float, input().split())])
########################################################################################################################
print("1) Матрица (A|b):")
Ab = getTransposed(A)
Ab.append(b)
Ab = getTransposed(Ab)
printAb(Ab)
########################################################################################################################
print("2) Коэффециенты от прямой прогонки матрицы (A|b):")
sPQs = [ [Ab[0][1] / -Ab[0][0], Ab[0][n] / Ab[0][0]] ]
for i in range(1, n - 1):
    sPQs.append([Ab[i][i + 1] / (-Ab[i][i] - Ab[i][i - 1] * sPQs[-1][0])
                , (Ab[i][i - 1] * sPQs[-1][1] - Ab[i][n])
                   / (-Ab[i][i] - Ab[i][i - 1] * sPQs[-1][0])])
sPQs.append(["", (Ab[-1][-3] * sPQs[-1][1] - Ab[-1][n])
                 / (-Ab[-1][-2] - Ab[-1][-3] * sPQs[-1][0])])
printPoints(sPQs, "Q", "P")
########################################################################################################################
print("3) Вычисление x в обратном порядке по полученным коэффициентам:")
xs = [sPQs[-1][1]]
for i in range(len(sPQs) - 2, -1, -1):
    xs.append(sPQs[i][0] * xs[-1] + sPQs[i][1])
print(*[f"x{n-i}: {round(xs[i], K)}" for i in range(len(xs))], sep=" │ ")
########################################################################################################################
print("4)Решение системы:")
xs.reverse()
print(*[f"x{i}: {round(xs[i], K)}" for i in range(len(xs))], sep=" │ ")
########################################################################################################################
# done
