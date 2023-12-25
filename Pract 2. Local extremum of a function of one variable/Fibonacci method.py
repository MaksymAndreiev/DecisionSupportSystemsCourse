def function(x):
    return 3 * x ** 4 + 5 * x ** 3 - 10 * x ** 2 + 6 * x


def fibonacci_search(f, a, b, epsilon):
    """
    Знаходить локальний мінімум функції f на відрізку [a;b] методом Фібоначчі.
    :param f: функція, для якої треба знайти локальний мінімум
    :param a: початок відрізку
    :param b: кінець відрізку
    :param n: число обчислень значень функції f(x)
    :param epsilon: точність, з якою треба знайти мінімум
    :return: кортеж з двома елементами: координати точки з мінімальним значенням та мінімальне значення функції
    """

    def fibonacci(m):
        if m == 0:
            return 0
        elif m == 1:
            return 1
        else:
            return fibonacci(m - 1) + fibonacci(m - 2)

    n, k = 1, 1
    while fibonacci(n + 2) <= (b - a) / epsilon:
        n += 1

    u = a + fibonacci(n) / fibonacci(n + 2) * (b - a)
    v = a + b - u
    fu = f(u)
    fv = f(v)

    x_min = 0
    f_min = 0

    while k != n:
        print(f'Крок {k}')
        if fu <= fv:
            x_min = u
            f_min = fu
            b = v
            v = u
            fv = fu
            u = a + b - v
            fu = f(u)
        else:
            x_min = v
            f_min = fv
            a = u
            u = v
            fu = fv
            v = a + b - u
            fv = f(v)

        print(" x_min = {:.4f}, f_min = {:.4f}".format(x_min, f_min))
        k += 1

    return x_min, f_min


a = -4
b = 2
epsilon = 0.05
delta = 0.01

x_min, f_min = fibonacci_search(function, a, b, epsilon)

print("Мінімум знайдено в точці x = {0:.4f}, f(x) = {1:.4f}".format(x_min, f_min))
