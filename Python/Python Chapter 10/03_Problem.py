class Demo:
    a= 4 

o = Demo()
print(o.a)# Print the class attribute because instance attribute is not present
o.a = 0# Instance attribute is set
print(o.a)# Print the instance attribute because instance attribute is present
print(Demo.a)# Print the class attribute