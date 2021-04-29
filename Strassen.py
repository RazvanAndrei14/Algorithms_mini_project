from numpy import random
from datetime import datetime
import time

start_time = datetime.now()

A = [[40, 43, 10, 75],
     [42, 81, 77, 90],
     [85, 22, 73, 19],
     [17, 5, 35, 33]]
B = [[60, 91, 52, 11],
     [7, 58, 70, 11],
     [82, 48, 34, 13],
     [17, 94, 64, 88]]


# x = random.randint(100, size=(4, 4))
# print(x)


# Strassen algorithm for multiplication

def Top_Right(a, n):
    k = int(n / 2)
    t_right = [[[0] for i in range(0, k)] for j in range(0, k)]
    for i in range(0, k):
        for j in range(0, k):
            t_right[i][j] = a[i][j]
    return t_right


def Top_Left(a, n):
    k = int(n / 2)
    t_left = [[[0] for i in range(0, k)] for j in range(0, k)]
    for i in range(0, k):
        for j in range(0, k):
            t_left[i][j] = a[i][j + k]
    return t_left


def Bottom_Right(a, n):
    k = int(n / 2)
    b_right = [[[0] for i in range(0, k)] for j in range(0, k)]
    for i in range(0, k):
        for j in range(0, k):
            b_right[i][j] = a[i + k][j]
    return b_right


def Bottom_Left(a, n):
    k = int(n / 2)
    b_left = [[[0] for i in range(0, k)] for j in range(0, k)]
    for i in range(0, k):
        for j in range(0, k):
            b_left[i][j] = a[i + k][j + k]
    return b_left


def Combine_Areas(a11, a12, a21, a22, n):
    k = int(2 * n)
    a = [[[0] for i in range(0, k)] for j in range(0, k)]
    for i in range(0, n):
        for j in range(0, n):
            a[i][j] = a11[i][j]
            a[i][j + n] = a12[i][j]
            a[i + n][j] = a21[i][j]
            a[i + n][j + n] = a22[i][j]
    return a


def Sum(a, b, n):
    c = [[[0] for i in range(0, n)] for j in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            c[i][j] = a[i][j] + b[i][j]
    return c


def Subtract(a, b, n):
    c = [[[0] for i in range(0, n)] for j in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            c[i][j] = a[i][j] - b[i][j]
    return c


def Strassen_Formula(a, b, n):
    k = n
    if k == 2:
        l = [[[0] for i in range(2)] for i in range(2)]
        l[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        l[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        l[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        l[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
        return l
    else:
        A11 = Top_Right(a, n)
        A12 = Top_Left(a, n)
        A21 = Bottom_Right(a, n)
        A22 = Bottom_Left(a, n)
        B11 = Top_Right(b, n)
        B12 = Top_Left(b, n)
        B21 = Bottom_Right(b, n)
        B22 = Bottom_Left(b, n)
        k = int(n / 2)
        p1 = Strassen_Formula(A11, Subtract(B12, B22, k), k)
        p2 = Strassen_Formula(Sum(A11, A12, k), B22, k)
        p3 = Strassen_Formula(Sum(A21, A22, k), B11, k)
        p4 = Strassen_Formula(A22, Subtract(B21, B11, k), k)
        p5 = Strassen_Formula(Sum(A11, A22, k), Sum(B11, B22, k), k)
        p6 = Strassen_Formula(Subtract(A12, A22, k), Sum(B21, B22, k), k)
        p7 = Strassen_Formula(Subtract(A11, A21, k), Sum(B11, B12, k), k)

        C11 = Sum(Subtract(Sum(p5, p4, k), p2, k), p6, k)
        C12 = Sum(p1, p2, k)
        C21 = Sum(p3, p4, k)
        C22 = Subtract(Subtract(Sum(p5, p1, k), p3, k), p7, k)
        C = Combine_Areas(C11, C12, C21, C22, k)
        return C


allRunningTimes = []
allStartTimes = []
allEndTimes = []
nrOfIterations = 100000
for i in range(nrOfIterations):
    start_time = datetime.now()
    Strassen_Formula(A, B, 4)
    end_time = datetime.now()
    allStartTimes.append(start_time)
    allEndTimes.append(end_time)

timeLapsed = allEndTimes[nrOfIterations - 1] - allStartTimes[0]

print('Started: {}'.format(allStartTimes[0]) + ' Ended: {}'.format(allEndTimes[nrOfIterations - 1]), sep="\n")
print('Time lapsed: {}'.format(timeLapsed))
print('Average time/iteration: {}'.format(timeLapsed / nrOfIterations))