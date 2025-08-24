mark1 = int(input("Enter your First Subject marks:"))
mark2 = int(input("Enter your Second Subject marks:"))
mark3 = int(input("Enter your Third Subject marks:"))

marks = (mark1 + mark2 + mark3)/3

if(marks>40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("You are Pass")
    print("Congratulations!")

else:
    print("You are Fail")
    print("Better Luck Next Time")

    # End Of Program