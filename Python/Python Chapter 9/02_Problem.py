import random
def game():
    print("you are playing the game: ")
    score = random.randint(1,65)

    #Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore=int(hiscore)
        else:
            hiscore = 0


    print(f"Your Score: {score}")
    if(score > hiscore):
        #write the new hiscore
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()        
