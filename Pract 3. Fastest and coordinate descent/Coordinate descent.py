import numpy as np
import sympy as sym

# Визначення символьної функції
x1, x2 = sym.symbols('x1 x2')
h = sym.symbols('h')
f = 10 * x1 ** 2 + x2 ** 2 + 4 * x1 * x2 - 2 * x1 + x2

# Початкова точка
x0 = np.array([0, 0]).astype(float)

eps = 0.0005  # Точність

e = np.zeros((x0.size, x0.size)).astype(float)
np.fill_diagonal(e[:, ::-1], 1)


def coord(x, f, eps):
    j = 1
    dx_val = [1]
    while np.linalg.norm(dx_val) > eps:
        print('-' * 50)
        print(f'Крок {j}.')
        print('-' * 50)

        for i in range(2):
            dx = h * sym.Matrix(e[i])
            phi = f.subs({x1: x[0] + dx[0], x2: x[1] + dx[1]})
            dphi = sym.diff(phi, h)
            h_val = float(sym.solve(dphi, h)[0])
            dx_val = np.transpose(np.array(sym.Matrix(dx).subs({h: h_val})).astype(float))[0]
            print(dx_val)
            x += dx_val
        f_ = np.round(np.array(f.subs({x1: x[0], x2: x[1]})).astype(np.double), 6)
        print(f'x = {x}; f(x({j},{j})) = {f_}')

        j += 1
    # Повертаємо оцінку екстремуму та точку, де вона була досягнута
    return f_, x


coord(x0, f, eps)
