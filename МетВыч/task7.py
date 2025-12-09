from tabulate import tabulate
import numpy as np

K = 2

def getYsOfFuncByXsRec(func, xs):
    return


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


#print("Введите размерность: ")
#n = int(input())
n = 9
print("Введите вариант: ", end='')
v = float(input())

########################################################################################################################
x0 = 1
y0 = v
h = 1 / 10 ** 6
for step in range(3):
    tabl = [["x:"] + [x0 + h * i for i in range(n)]]

    ## точный результат
    fx = len(tabl)
    tabl.append(["точный результат:"])
    for i in range(1, n + 1):
        tabl[fx].append(v * tabl[0][i] * tabl[0][i])

    ## метод Эйлера
    mE = len(tabl)
    tabl.append(["метод Эйлера:", y0])
    for i in range(1, n):
        tabl[mE].append(tabl[mE][i] + h * (2 * v * tabl[0][i] + v * tabl[0][i] * tabl[0][i] - tabl[mE][i]))

    ## усовершенствованный метод Эйлера
    cE = len(tabl)
    tabl.append(["усов. метод Эйлера:", y0])
    for i in range(1, n):
        tablcEi1 = tabl[cE][i] + h * (2 * v * tabl[0][i] + v * tabl[0][i] * tabl[0][i] - tabl[cE][i])
        tabl[cE].append(tabl[cE][i] + h * (2 * v * tabl[0][i + 1] + v * tabl[0][i + 1] * tabl[0][i + 1] - tablcEi1))

    ## разница mE - fx
    e1 = len(tabl)
    tabl.append(["мет. Э. - точн."])
    for i in range(1, n + 1):
        tabl[e1].append(tabl[mE][i] - tabl[fx][i])
    ## разница cE - fx
    e2 = len(tabl)
    tabl.append(["усов. мет. Э. - точн."])
    for i in range(1, n + 1):
        tabl[e2].append(tabl[cE][i] - tabl[fx][i])
    ## разница mE - cE
    e3 = len(tabl)
    tabl.append(["мет. Э. - усов. мет. Э."])
    for i in range(1, n + 1):
        tabl[e3].append(tabl[mE][i] - tabl[cE][i])

    print(tabulate(tabl, tablefmt="fancy_outline"))  # psql

    h /= 10
########################################################################################################################
