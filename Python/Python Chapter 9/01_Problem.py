f = open("poem.txt")

content = f.read()
if("Twinkle" in content):
    print("The word 'Twinkle' was found in the poem.")

else:
    print("The word 'Twinkle' was not found in the poem.")

f.close()