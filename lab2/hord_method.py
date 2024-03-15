import math

a = 1
b = 1.5

epsilon = 0.05


def y_function(x: float) -> float:
    return x**2 - 2*x + math.exp(-x)


def y_derivative(x: float) -> float:
    return 2*x - 2 - math.exp(-x)


def hord_method():
    a_ = a
    b_ = b
    x_ = a_ - y_derivative(a_) / (y_derivative(a_) - y_derivative(b_)) * (a_ - b_)
    der_x_ = y_derivative(x_)
    print(f"a={a_} b={b_} x_={x_} der_x_ = {der_x_}")
    while (abs(der_x_) > epsilon):
        if (der_x_ > 0):
            b_ = x_
        else:
            a_ = x_
        x_ = a_ - y_derivative(a_) / (y_derivative(a_) - y_derivative(b_)) * (a_ - b_)
        der_x_ = y_derivative(x_)
        print(f"a={a_} b={b_} x_={x_} der_x_ = {der_x_}")
    xm = x_
    ym = y_function(xm)
    print(f"x_min={xm} y_min={ym}")


if __name__ == "__main__":
    hord_method()