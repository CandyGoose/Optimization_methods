import math

a = 1
b = 1.5

epsilon = 0.05


def y_function(x: float) -> float:
    return x**2 - 2*x + math.exp(-x)


def half_method():
    a_ = a
    b_ = b
    print(f"a={a_} b={b_}")
    while (b_ - a_ > 2 * epsilon):
        x1 = (a_ + b_ - epsilon) / 2
        x2 = (a_ + b_ + epsilon) / 2
        y1 = y_function(x1)
        y2 = y_function(x2)
        if (y1 > y2):
            a_ = x1
        else:
            b_ = x2
        print(f"x1 = {x1} x2 = {x2} y1={y1} y2={y2} a={a_} b={b_} b-a={b_-a_}")
    xm = (a_ + b_) / 2
    ym = y_function(xm)
    print(f"x_min={xm} y_min={ym}")


if __name__ == "__main__":
    half_method()