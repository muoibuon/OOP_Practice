import math 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return f"({self.x}, {self.y})"
if __name__ == "__main__":
    p1 = str(input())
    p1 = p1.split()
    p1 = Point(float(p1[0]), float(p1[1]))
    O = Point(0, 0)
    print(f"({p1.x:.0f}, {p1.y:.0f})")
    print(f"{p1.distance(O)}")
