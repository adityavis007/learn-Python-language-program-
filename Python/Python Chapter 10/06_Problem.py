from random import randint

class Train:

    def __init__(aditya, trainNo):
        aditya.trainNo = trainNo
        

    def book(aditya,fro,to):
        print(f"Ticket is booked in Train No: {aditya.trainNo} from {fro} to {to}")


t = Train(12487)
t.book("Delhi","Mumbai")