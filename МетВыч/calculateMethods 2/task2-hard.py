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

def polyFFTMul(polyList):
    if len(polyList) == 0:
        return []
    n = 1
    for pli in polyList:
        n += len(pli) - 1
    n_ = 1 << (n - 1).bit_length()  # длина до степени двойки

    res = np.fft.fft(polyList[0], n_)
    for i in range(1, len(polyList)):
        res = res * (np.fft.fft(polyList[i], n_))
    return np.fft.ifft(np.real_if_close(res, tol=1e18)[:n])

def divWithoutRemainder(a, b):
    return np.polydiv(a, b)
    # n = len(a) + len(b) - 1
    # n_ = 1 << (n - 1).bit_length()  # длина до степени двойки
    #
    # A = np.fft.fft(a, n_)
    # B = np.fft.fft(b, n_)
    # Q = A / B
    # q = np.fft.ifft(Q)
    # return np.real_if_close(q, tol=1e8)[:n]

def polyAdd(a, b):

    return #A + B

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
# numeratorList = [[1, -pointsF[i][0]] for i in range(n)]
# numerator = polyFFTMul(numeratorList)
# for i in range(n):
#     denominator = 1
#     for j in range(n):
#         if j != i:
#             denominator *= pointsF[i][0] - pointsF[j][0]
#     L_i = divWithoutRemainder(numerator, np.array([1, pointsF[i][0]]))
#     L_i = [pointsF[i][1] / denominator * L_i[i] for i in range(len(L_i))]
#     L_n = polyAdd(L_n, L_i)
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


pointsP = [pointsF[0]]
for i in range(1, n):
    x = (pointsF[i - 1][0] + pointsF[i][0]) / 2
    pointsP.append([x, calcF(coefs, x)])
    pointsP.append(pointsF[i])