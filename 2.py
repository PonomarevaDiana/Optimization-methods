def f(x):
    return 0.1176 * x**4 + 1.8851 * x**3 + -1.6427 * x**2 - 28.4306 * x + 127.0896


def maximum(a, b, delta=1e-6, eps=1e-7, max_iter=2000):
    k2 = (5 ** (1 / 2) - 1) / 2
    k1 = (3 - 5 ** (1 / 2)) / 2
    x1 = a + k1 * (b - a)
    x2 = a + k2 * (b - a)
    f1 = f(x1)
    f2 = f(x2)

    for _ in range(max_iter):
        if f1 >= f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + k1 * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + k2 * (b - a)
            f2 = f(x2)

        if abs(b - a) < eps:
            break
    x_max = (a + b) / 2
    return x_max, f(x_max)


x_max, f_max = maximum(9, 11)
print(f"x_max = {x_max:.6f}")
print(f"f(x) = {f_max:.6f}")
