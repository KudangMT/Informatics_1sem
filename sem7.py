import math

# 1 --------------------------
class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print("Initialized:", x, y, z)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise ValueError("TypeError")

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise ValueError("TypeError")

    def __str__(self):
        return "{" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "}"

    def isOrth(self, other):
        if isinstance(other, Vector):
            if other * self == 0:
                return True
            else:
                return False
        else:
            raise ValueError("TypeError")


k = Vector(1, 2, 1)
l = Vector(3, -4, 5)
m = Vector(1, 32, 5)
print(Vector.isOrth(k, m))