import math


def f(x: float) -> float:
    return x**2 - 2*x + math.exp(-x)


a = 1
b = 1.5

epsilon = 0.0001

inf = 2**31 - 1


def quadratic_approximation_method() -> float:
    x_1 = 1.25
    delta_x = 0.05
    epsilon_1 = epsilon
    epsilon_2 = epsilon

    x_result: float

    x_mid = -1 * inf
    x_mid_copy = x_mid

    can_continue = True
    while (can_continue):
        x_2 = x_1 + delta_x
        x_3: float
        if (f(x_1) > f(x_2)):
            x_3 = x_1 + 2 * delta_x
        else:
            x_3 = x_1 - delta_x
        while (True):
            x_and_y = {f(x): x for x in [x_1, x_2, x_3]}
            x_min = x_and_y[min(x_and_y.keys())]
            F_min = f(x_min)
            nominator = (x_2**2 - x_3**2) * f(x_1) + (x_3**2 - x_1**2) * f(x_2) + (x_1**2 - x_2**2) * f(x_3)
            denominator = 2 * ((x_2 - x_3) * f(x_1) + (x_3 - x_1) * f(x_2) + (x_1 - x_2) * f(x_3))
            if (denominator == 0):
                x_1 = x_min
                break
            x__ = nominator / denominator
            is_e1 = abs((F_min - f(x__)) / f(x__)) < epsilon_1
            is_e2 = abs((x_min - x__) / x__) < epsilon_2
            print(f"x_1={x_1}, x_2={x_2}, x_3={x_3}, f(x_1)={f(x_1)}, f(x_2)={f(x_2)}, f(x_3)={f(x_3)}, x_min={x_min}, F_min={F_min}")
            print(f"x__={x__}, f(x__)={f(x__)}, A={abs((F_min - f(x__)) / f(x__))}, B={abs((x_min - x__) / x__)}")
            print(is_e1, is_e2)
            if (is_e1 and is_e2):
                x_result = x__
                can_continue = False
                break
            else:
                if (x_1 < x__ and x__ < x_3):
                    x_mid: float
                    if (f(x_min) < f(x__)):
                        x_mid = x_min
                    else:
                        x_mid = x__
                    # x_mid = min(x_min, x__)
                    if (x_mid == x_mid_copy):
                        can_continue = False
                        x_result = x_mid
                        break
                    x_mid_copy = x_mid
                    x_left = max(list(filter(lambda x: x < x_mid, [x_1, x_2, x_3])))
                    x_right = min(list(filter(lambda x: x > x_mid, [x_1, x_2, x_3])))
                
                    x_1 = x_left
                    x_2 = x_mid
                    x_3 = x_right
                    print(f"x_left={x_left}, x_mid={x_mid}, x_right={x_right}")
                else:
                    x_1 = x__
                    print(f"new x_1={x_1}")
                    break
    return x_result

res = quadratic_approximation_method()
print(res)