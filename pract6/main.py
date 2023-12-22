import math

import numpy as np


def f(x1, x2):
    return -(-pow(x1, 2) - x1 * x2 - pow(x2, 2) - 3 * x1 - 5 * x2)
    # return 3 * pow(x2, 2) - x1 - 1 + pow(x1, 2)


def bar_func(x1, x2, r):
    f = 3 * x2 ** 2 - x1 - 1 + x1 ** 2
    b = (1 / r) * (-(8 / (2 * x1 + 3 * x2)) + (12 / (8 * x1 + 2 * x2)))
    # b = (1 / r) * (-(1 / (x2 ** 2 + x1)) + (-1 / (-x1 + 2 * x2)))
    return f + b


def gold(a, b, x01, x02, eps, i, func):
    while ((b - a) / 2) > eps:
        x1 = a + 0.382 * (b - a)
        x2 = a + 0.618 * (b - a)
        if func(x01, x02, i, x1) < func(x01, x02, i, x2):
            b = x2
        elif func(x01, x02, i, x1) > func(x01, x02, i, x2):
            a = x1
        else:
            a = x1
            b = x2
    return (a + b) / 2


def next_pc(x01, x02, i, alpha):
    d, d1 = [1, 0], [0, 1]
    npt = [0, 0]
    if i % 2 == 0:
        npt[0] = x01 + alpha * d[0]
        npt[1] = x02 + alpha * d[1]
    else:
        npt[0] = x01 + alpha * d1[0]
        npt[1] = x02 + alpha * d1[1]
    return npt


def phi(x01, x02, i, alpha):
    d, d1 = np.array([1, 0]), np.array([0, 1])
    npt = np.array([x01, x02]) + alpha * d if i % 2 == 0 else np.array([x01, x02]) + alpha * d1
    return f(npt[0], npt[1])


def coordinate_descent(x01, x02, r, eps):
    i = 0
    alpha = gold(-1, 1, x01, x02, eps, i, phi)
    x1, x2 = next_pc(x01, x02, i, alpha)[0], next_pc(x01, x02, i, alpha)[1]
    print("x1:", x1, "x2:", x2, "f(x1,x2):", f(x1, x2))
    while (math.sqrt(pow(x01 - x1, 2) + pow(x02 - x2, 2)) > eps) or (
            (abs(f(x01, x02) - f(x1, x2))) > eps):
        x01, x02 = x1, x2
        i += 1
        alpha = gold(-1, 1, x01, x02, eps, i, phi)
        x1, x2 = next_pc(x01, x02, i, alpha)[0], next_pc(x01, x02, i, alpha)[1]
        print(f"x1: {x1} x2: {x2} f_bar(x1,x2): {bar_func(x1, x2, r)}")


x1, x2 = 0, 0
r, eps = 1.0, 0.001
while r > eps:
    print(f"Функція бар'єру з r = {r}")
    coordinate_descent(x1, x2, r, eps)
    print()
    r /= 2
