def patten(n):
    if(n==0):
        return
    print("*"*n)
    patten(n-1)

patten(int(input("Enter a number: ")))