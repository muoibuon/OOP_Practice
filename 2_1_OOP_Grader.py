import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return f"({self.x}, {self.y})"
if __name__ == "__main__":
    diem = str(input())
    hihi = diem.split()
    A = [int(i) for i in hihi]
    B = [int(i) for i in hihi]
    pointA = Point(A[0], A[1])
    pointB = Point(B[2], B[3])
    goc = math.atan2(pointB.y - pointA.y, pointB.x - pointA.x)*180/math.pi
    print(f"[({pointA.x}, {pointA.y}), ({pointB.x}, {pointB.y})]")
    print(f"{pointA.distance(pointB):.1f}")
    print(f"{goc:.0f}")

