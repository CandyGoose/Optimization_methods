from vector import Vector

epsilon = 0.01

def y_function(point_x: Vector) -> float:
    x_es: list[float] = point_x.getArray()
    return 4 * x_es[0] ** 2 + 3 * x_es[1] ** 2 + 16 * x_es[0] - 4 * x_es[1]

def gradient(point_x: Vector) -> Vector:
    x_es: list[float] = point_x.getArray()
    return Vector([8 * x_es[0] + 16, 6 * x_es[1] - 4])

def gradient_descent_method() -> float:
    x_vec = Vector([0, 0])
    step: float = 0.25
    try:
        while(gradient(x_vec).module() >= epsilon):
            print("grad: ", gradient(x_vec), gradient(x_vec).module())
            x_prev_vec = x_vec
            x_vec -= step * gradient(x_vec)
            if (y_function(x_vec) > y_function(x_prev_vec)):
                step /= 2
            print(x_vec, y_function(x_vec))
        return y_function(x_vec)
    except OverflowError:
        print("Числа слишком большие")

if __name__ == "__main__":
    print(gradient_descent_method())