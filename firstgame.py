import random
num = random.randint(1,22)
 
while(True):
    inp=int(input())
    if(inp<num):
        print("Wrong number the number is greater than your guess")
    elif(inp>num):
        print("Wrong number the number is smaller than your guess")
    else:
        print("Congrats your guess is right")
        
