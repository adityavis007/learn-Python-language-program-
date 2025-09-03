class Calculator:
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"This is the square of {self.n}: {self.n * self.n}")
    def cube(self):
        print(f"This is the cube of {self.n}: {self.n * self.n * self.n}")
    def squareroot(self):
        print(f"This is the squareroot of {self.n}: {self.n ** 0.5}")
    @staticmethod
    def hello():
           print("Hello everyone!")

a = Calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()
