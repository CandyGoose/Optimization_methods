class Vector:
    def __init__(self, components: list[float]):
        self.components = components

    def getArray(self) -> list[float]:
        return self.components
    
    def getLength(self) -> int:
        return len(self.components)

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same length")
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same length")
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, scalar: float):
        return Vector([a * scalar for a in self.components])

    def __rmul__(self, scalar: float):
        return self.__mul__(scalar)

    def __str__(self) -> str:
        return f"Vector({self.components})"
    
    def module(self) -> float:
        square_result: float = sum([component**2 for component in self.components])
        return square_result ** 0.5