p1 = "Make a lot of Money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click here"
p5 = "limited time offer"

message = input("Enter your message: ")
if(p1 in message or p2 in message or p3 in message or p4 in message or p5 in message):
    print("This is a spam message")
else:
    print("This is not a spam message")