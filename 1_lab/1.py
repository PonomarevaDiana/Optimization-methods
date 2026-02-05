def f(x):
    return (
        0.2945 * x**8
        - 1.5086 * x**7
        + 3.7762 * x**6
        + 13.9522 * x**5
        - 21.0103 * x**4
        + 0.1067 * x**3
        - 2.4968 * x**2
        + 20.8671 * x
        - 89.9776
    )


def minimum(a, b, delta=1e-6, eps=1e-7, max_iter=1000):
    for _ in range(max_iter):
        mid = (a + b) / 2
        x1 = mid - delta
        x2 = mid + delta
        f1 = f(x1)
        f2 = f(x2)

        if f1 <= f2:
            b = x2
        else:
            a = x1

        if abs(b - a) < eps:
            break
    x_min = (a + b) / 2
    return x_min, f(x_min)


x_min, f_min = minimum(-9, 12)
print(f"f(x) = {x_min:.6f}")
print(f"f(x) = {f_min:.6f}")
