import math
class Pointtest:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
if __name__ == "__main__":
    A = Pointtest(3,4)
    O = Pointtest(0,0)
    B = str((input()))
    B = B.split()
    B = [int(i) for i in B]
    B = Pointtest(B[0],B[1])
    C = Pointtest(-B.x,-B.y)
    print(f"({A.x},{A.y})")
    print(f"({B.x},{B.y})")
    print(f"({C.x},{C.y})")
    print(f"{B.distance(A):.1f}")
