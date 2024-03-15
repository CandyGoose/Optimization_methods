import math

a = 1
b = 1.5

epsilon = 0.05
GR = (1 + math.sqrt(5)) / 2


def y_function(x: float) -> float:
    return x**2 - 2*x + math.exp(-x)


def golden_ratio_method():
    a_ = a
    b_ = b
    c1 = 1 - 1/GR
    c2 = 1/GR

    x1 = a_ + c1 * (b_ - a_)
    x2 = a_+ c2 * (b_ - a_)
    y1 = y_function(x1)
    y2 = y_function(x2)
    if (y1 < y2):
        b_ = x2
    else:
        a_ = x1

    while (b_ - a_  > 2 * epsilon):
        print(f"x1 = {x1} x2 = {x2} y1={y1} y2={y2} a={a_} b={b_} b-a={b_ - a_}")

        if (y1 < y2):
            x2 = x1
            x1 = a_ + c1 * (x2 - a_)
            y2 = y1
            y1 = y_function(x1)
        else:
            x1 = x2
            x2 = a_ + c2 * (b_ - x1)
            y1 = y2
            y2 = y_function(x2)

        if (y1 < y2):
            b_ = x2
        else:
            a_ = x1

    print(f"x1 = {x1} x2 = {x2} y1={y1} y2={y2} a={a_} b={b_} b-a={b_ - a_}")
    xm = (a_ + b_) / 2
    ym = y_function(xm)
    print(f"x_min={xm} y_min={ym}")


if __name__ == "__main__":
    golden_ratio_method()