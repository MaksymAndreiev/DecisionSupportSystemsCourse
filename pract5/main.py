import numpy as np
import sympy as sym
from sympy import derive_by_array, pretty, Matrix

# Визначення символьної функції

x1, x2 = sym.symbols('x1 x2')
h = sym.symbols('h')
f = 10 * x1 ** 2 + x2 ** 2 + 4 * x1 * x2 - 2 * x1 + x2

# Початкова точка
x0 = np.array([0, -1]).astype(float)

eps = 0.005  # Точність

grad_f = derive_by_array(f, (x1, x2))
hess_f = derive_by_array(derive_by_array(f, (x1, x2)), (x1, x2))

print('Функція:')
print(pretty(f))
print('Градієнт функції:')
print(pretty(Matrix(grad_f)))
print('Гессіан функції:')
print(pretty(Matrix(hess_f)))


def conj_grad(x, f, grad, hess):
    global f_
    dx = np.array([0, -1]).astype(np.double)
    i = 1

    while np.linalg.norm(dx) > eps:
        print('-' * 50)
        print(f'Крок {i}.')
        print('-' * 50)
        # Обчислюємо градієнт у поточній точці
        grad_ = np.array(grad.subs({x1: x[0], x2: x[1]})).astype(np.double)
        print(f'Значення градієнту в точці x{i - 1}:')
        print(pretty(Matrix(grad_)))

        # 3начення руху
        if i == 1:
            d = - grad_

        alpha = -(d.T @ grad_) / (d.T @ hess @ d)

        # Оновлюємо x
        dx = np.array(alpha * d).astype(float)
        x += dx
        print(f'x{i} =\n{pretty(Matrix(x))}')

        # Оновлюємо градієнт
        grad_ = np.array(grad.subs({x1: x[0], x2: x[1]})).astype(np.double)

        beta = (grad_.T @ grad_) / (d.T @ hess @ d)
        d = - grad_ + beta * d

        f_ = np.array(f.subs({x1: x[0], x2: x[1]})).astype(np.double)
        print(f'f = {f_}')

        i += 1

    # Повертаємо оцінку екстремуму та точку, де вона була досягнута
    return f_, x


conj_grad(x0, f, grad_f, hess_f)
