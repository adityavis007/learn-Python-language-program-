class Calculator:
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"This is the square of {self.n}: {self.n * self.n}")
    def cube(self):
        print(f"This is the cube of {self.n}: {self.n * self.n * self.n}")
    def squareroot(self):
        print(f"This is the squareroot of {self.n}: {self.n ** 0.5}")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()
