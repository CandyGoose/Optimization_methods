import math
import random

a = 1
b = 1.5

epsilon = 0.05


def y_function(x: float) -> float:
    return x**2 - 2*x + math.exp(-x)


def y_derivative(x: float) -> float:
    return 2*x - 2 - math.exp(-x)


def y_2nd_derivative(x: float) -> float:
    return 2 + math.exp(-x)


def newton_method():
    xk = random.uniform(a, b)
    xk = 1.5
    i = 0
    print(f"x{i}={xk} der={y_derivative(xk)}")
    while (abs(y_derivative(xk)) > epsilon):
        i+=1
        xk = xk - y_derivative(xk) / y_2nd_derivative(xk)
        print(f"x{i}={xk} der={y_derivative(xk)}")
    xm = xk
    ym = y_function(xk)
    print(f"x_min={xm} y_min={ym}")


if __name__ == "__main__":
    newton_method()