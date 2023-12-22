import numpy as np
import sympy as sym
from sympy import pretty, Matrix
from sympy.tensor.array import derive_by_array

# Визначення символьної функції

x1, x2 = sym.symbols('x1 x2')
f = 10 * x1 ** 2 + x2 ** 2 + 4 * x1 * x2 - 2 * x1 + x2 + sym.sin(x1)


def newton_method(x, f, grad, hess, eps):
    global f_
    dx = np.array([1, 1]).astype(np.double)
    i = 1

    while np.linalg.norm(dx) > eps:
        print('-' * 50)
        print(f'Крок {i}.')
        print('-' * 50)
        # Обчислюємо градієнт та гессіан у поточній точці
        grad_ = np.array(grad.subs({x1: x[0], x2: x[1]})).astype(np.double)
        print(f'Значення градієнту в точці x{i - 1}:')
        print(pretty(Matrix(grad_)))
        hess_ = np.array(hess.subs({x1: x[0], x2: x[1]})).astype(np.double)
        print(f'Значення гессіану в точці x{i - 1}:')
        print(pretty(Matrix(hess_)))
        hess_inv = np.linalg.inv(hess_)
        print(f'Значення оберненого гессіану в точці x{i - 1}:')
        print(pretty(Matrix(hess_inv)))

        # Оновлюємо x
        dx = hess_inv @ grad_
        x -= dx
        print(f'x{i} =\n{pretty(Matrix(x))}')

        f_ = np.array(f.subs({x1: x[0], x2: x[1]})).astype(np.double)

        i += 1

    # Повертаємо оцінку екстремуму та точку, де вона була досягнута
    return f_, x


def modified_newton_method(x, f, grad, hess, eps):
    global f_
    dx = np.array([1, 1]).astype(np.double)
    hess_ = np.array(hess.subs({x1: x[0], x2: x[1]})).astype(np.double)
    hess_inv = np.linalg.inv(hess_)
    i = 1

    while np.linalg.norm(dx) > eps:
        print('-' * 50)
        print(f'Крок {i}.')
        print('-' * 50)
        # Обчислюємо градієнт у поточній точці
        grad_ = np.array(grad.subs({x1: x[0], x2: x[1]})).astype(np.double)
        print(f'Значення градієнту в точці x{i - 1}:')
        print(pretty(Matrix(grad_)))

        # Оновлюємо x
        dx = hess_inv @ grad_
        x -= dx
        print(f'x{i} =\n{pretty(Matrix(x))}')

        f_ = np.array(f.subs({x1: x[0], x2: x[1]})).astype(np.double)

        i += 1

    # Повертаємо оцінку екстремуму та точку, де вона була досягнута
    return f_, x


# Початкова точка
x0 = np.array([0, 0]).astype(np.double)

eps = 0.0001  # Точність

grad_f = derive_by_array(f, (x1, x2))
hess_f = derive_by_array(derive_by_array(f, (x1, x2)), (x1, x2))

print('Функція:')
print(pretty(f))
print('Градієнт функції:')
print(pretty(Matrix(grad_f)))
print('Гессіан функції:')
print(pretty(Matrix(hess_f)))

print('\n\nМетод Ньютону\n\n')

# Застосування методу Ньютона
fmin, xmin = newton_method(x0, f, grad_f, hess_f, eps)
print(f"Мінімум функції за допомогою методу Ньютона: x = {xmin.tolist()}, f(x) = {fmin.tolist()}")

print('\n\nМодифікований метод Ньютону\n\n')

# Застосування модифікованого методу Ньютона
fmin_mod, xmin_mod = modified_newton_method(x0, f, grad_f, hess_f, eps)
print(f"Мінімум функції за допомогою модифікованого методу Ньютона: x = {xmin_mod.tolist()}, f(x) = {fmin_mod.tolist()}")
