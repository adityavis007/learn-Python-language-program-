import random   

'''
1 for snake
-1 for water
0 for gun 

'''

computer = random.choice([1, -1, 0])

youstr = input("Enter s for snake, w for water, g for gun: ")
youDict = {"s":1, "w":-1, "g":0 }
reversedDict = {1:"s", -1:"w", 0:"g"}
you = youDict[youstr]   

print("You chose:", reversedDict[you])
print("Computer chose:", reversedDict[computer])
if(computer == you):
    print("Tie")
else:
    if(computer == 1 and you == 0):
        print("loses")
    elif(computer == -1 and you == 1):
        print("wins")
    elif(computer == 1 and you == -1):
        print("loses")
    elif(computer == 0 and you == -1):
        print("wins")
    elif(computer == 0 and you == 1):
        print("loses")
    else:
        print("something went wrong!")