def c_to_f(f):
    c = 5*(f-32)/9
    return c
print("The temperature in Celsius is: ", 
      c_to_f(int(input("Enter temperature in Fahrenheit: "))))