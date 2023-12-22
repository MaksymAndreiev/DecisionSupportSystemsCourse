import numpy as np
import sympy as sym
from sympy import pretty, Matrix
from sympy.tensor.array import derive_by_array

# Визначення символьної функції
x1, x2 = sym.symbols('x1 x2')
alpha = sym.symbols('alpha')
f = 10 * x1 ** 2 + x2 ** 2 + 4 * x1 * x2 - 2 * x1 + x2

# Початкова точка
x0 = np.array([0, 0]).astype(float)

eps = 0.005  # Точність

grad_f = derive_by_array(f, (x1, x2))


def quick(x, f, grad, eps):
    i = 1
    dx_val = 1
    while np.linalg.norm(dx_val) > eps:
        print('-' * 50)
        print(f'Крок {i}.')
        print('-' * 50)
        # Обчислюємо градієнт у поточній точці
        grad_ = grad.subs({x1: x[0], x2: x[1]})
        # 3начення руху
        d = - grad_

        # Оновлюємо x
        dx = alpha * d
        phi = f.subs({x1: x[0] + dx[0], x2: x[1] + dx[1]})
        dphi = sym.diff(phi, alpha)
        alpha_val = float(sym.solve(dphi, alpha)[0])
        dx_val = np.array(dx.subs({alpha: alpha_val})).astype(float)
        x += dx_val
        print(f'x{i} =\n{pretty(Matrix(x))}')

        f_ = np.array(f.subs({x1: x[0], x2: x[1]})).astype(np.double)
        print(f'f = {f_}')

        i += 1

    # Повертаємо оцінку екстремуму та точку, де вона була досягнута
    return f_, x


quick(x0, f, grad_f, eps)
