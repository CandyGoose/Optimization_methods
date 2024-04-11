from vector import Vector

epsilon = 0.01

def y_function(point_x: Vector) -> float:
    x_es: list[float] = point_x.getArray()
    return 4 * x_es[0] ** 2 + 3 * x_es[1] ** 2 + 16 * x_es[0] - 4 * x_es[1]


def gradient(point_x: Vector) -> Vector:
    x_es: list[float] = point_x.getArray()
    return Vector([8 * x_es[0] + 16, 6 * x_es[1] - 4])


def min_lambda_(x_vec: Vector, S: Vector) -> float:
    x_es: list[float] = x_vec.getArray()
    S_es: list[float] = S.getArray()
    def y_function_lambda(lambda_: float) -> float:
        return lambda_ ** 2 * (4 * S_es[0] ** 2 + 3 * S_es[1] ** 2) + \
            lambda_ * (- 8 * x_es[0] * S_es[0] - 16 * S_es[0] - 6 * x_es[1] * S_es[1] + 4 * S_es[1]) + \
            4 * x_es[0] ** 2 + 3 * x_es[1] ** 2 + 16 * x_es[0] - 4 * x_es[1]

    def half_method() -> float:
        a_ = -5
        b_ = 5
        while (b_ - a_ > 2 * epsilon):
            x1 = (a_ + b_ - epsilon) / 2
            x2 = (a_ + b_ + epsilon) / 2
            y1 = y_function_lambda(x1)
            y2 = y_function_lambda(x2)
            if (y1 > y2):
                a_ = x1
            else:
                b_ = x2
        xm = (a_ + b_) / 2
        return xm

    return half_method()

def fastest_descent_method() -> float:
    x_vec = Vector([0, 0])
    while(gradient(x_vec).module() >= epsilon):
        print("grad: ", gradient(x_vec), gradient(x_vec).module())
        S: Vector = (1/gradient(x_vec).module()) * gradient(x_vec)
        lambda_: float = min_lambda_(x_vec, S)
        print("S: ", S, lambda_)
        x_vec -= lambda_ * S
        print(x_vec)
    return y_function(x_vec)

if __name__ == "__main__":
    print(fastest_descent_method())