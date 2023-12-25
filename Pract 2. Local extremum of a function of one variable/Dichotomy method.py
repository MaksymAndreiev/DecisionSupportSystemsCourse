def function(x):
    return 3 * x ** 4 + 5 * x ** 3 - 10 * x ** 2 + 6 * x


def dichotomy_search(f, a, b, epsilon, delta):
    """
    Знаходить локальний мінімум функції f на відрізку [a;b] методом дихотомії.
    :param f: функція, для якої треба знайти локальний мінімум
    :param a: початок відрізку
    :param b: кінець відрізку
    :param epsilon: точність, з якою треба знайти мінімум
    :param delta: крок методу дихотомії
    :return: кортеж з двома елементами: координати точки з мінімальним значенням та мінімальне значення функції
    """
    global x_min, f_min
    x1 = (a + b - delta) / 2
    x2 = (a + b + delta) / 2
    f1 = f(x1)
    f2 = f(x2)
    if f1 <= f2:
        b = x2
        x_min = a
        f_min = f1
    else:
        a = x1
        x_min = b
        f_min = f2
    print("Крок 1.")
    print("x1 = {0:.4f}, x2 = {1:.4f}, f1 = {2:.4f}, f2 = {3:.4f}, x_min = {4:.4f}, f_min = {5:.4f}".format(
        x1, x2, f1, f2, x_min, f_min))
    step = 2
    while b - a >= epsilon:
        if f1 <= f2:
            b = x2
            x_min = x1
            f_min = f1
        else:
            a = x1
            x_min = x2
            f_min = f2
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2
        f1 = f(x1)
        f2 = f(x2)
        print("Крок {}.".format(step))
        print(
            "x1 = {0:.4f}, x2 = {1:.4f}, f1 = {2:.4f}, f2 = {3:.4f}, x_min = {4:.4f}, f_min = {5:.4f}".format(
                x1, x2, f1, f2, x_min, f_min))
        step += 1
    return x_min, f_min


a = -4
b = 2
epsilon = 0.05
delta = 0.01

x_min, f_min = dichotomy_search(function, a, b, epsilon, delta)

print("Мінімум знайдено в точці x = {0:.4f}, f(x) = {1:.4f}".format(x_min, f_min))
