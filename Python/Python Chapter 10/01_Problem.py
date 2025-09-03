class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Aditya",100000,231417)
print(p.company, p.name, p.salary, p.pin)
r = Programmer("Rahul",10000,231217)
print(r.company, r.name, r.salary, r.pin)
s= Programmer("Suraj",100000,231417)
print(s.company, s.name, s.salary, s.pin)