# import random
# def swg():
# 	print("Enter your name")
# 	name = str(input())
# 	print("Enter no. of round you want to play")
# 	n = int(input())
# 	time = 0
# 	p = 0
# 	c = 0
# 	print("ok %s here is rule"%name)
# 	print("[RULES]:-\n1)Snake is win from Water but lose from Gun\n2)Water is win from Gun but lose from snake\n3)Gun is win from snake but lose from Water")
# 	com = "because computer write"
# 	while(time<n):
# 		type = ['Snake', 'Water', 'Gun']
# 		r = random.choice(type)
# 		turn = str(input("\nEnter Snake or Water or Gun:\n"))
# 		if turn==r:
# 			print("\ndraw ")
# 		elif turn=="Snake" and r=="Water":
# 			p = p+1
# 			print("\nYou win")
# 		elif turn=="Snake" and r=="Gun":
# 			c = c+1
# 			print("\nYou lose")
# 		elif turn=="Water" and r=="Snake":
# 			c=c+1
# 			print("\nYou lose")
# 		elif turn=="Water" and r=="Gun":
# 			p = p+1
# 			print("\nYou win")
# 		elif turn=="Gun" and r=="Water":
# 			c=c+1
# 			print("\nYou lose")
# 		elif turn=="Gun" and r=="Snake":
# 			p=p+1
# 			print("\nYou win")
# 		else :
# 			print("\n[error occur]: Unexpected name")
# 		time = time+1
# 	if p<c:
# 		print("computer win")
# 	elif p==c:
# 		print("Draw")
# 	else:
# 		print("%s you win"%name)
# if __name__ == '__main__':
# 	swg()

import random

option=["Snake🐍","Water🌊","Gun🔫"]
user_name=input("Enter your name :- ")
print(f"\nWelcome {user_name} , Let's play with Snake , Water and Gun. ")
print("\nSnake🐍 can win with Water🌊.\nWater🌊 can win with Gun🔫.\nGun🔫 can win with Snake🐍   ")
print("Rules of Game :- \n 1. (0) zero is for Snake🐍.\n 2. (1) one is for Water🌊.\n 3. (2) is for Gun🔫.")
print("Winner will be decided after 3 round .\n Each round gives you 1 point  and the one who has more point will Win.")


a=0
b=0
n= 1

while n<=3:
    n=n+1
    computer=random.randint(0,2)
    ask_user=int(input("Choose any number between them . \nWrite here =  "))
    if (ask_user<0 or ask_user>2):
        raise ValueError("Sorry, that is not a valid option. Please give one of the given options. ")
    print(f"You have chosen {option[ask_user]} .")
    print(f"Computer have chosen {option[computer]} .")
    
    



    if (computer==0 and ask_user==1  ):
        print("Oops! That's incorrect. You have lost the game. Better luck next time!")
        a=a+1
# elif (computer==1 and ask_user==0):
#     print("Congratulations! You have won the game!")
    elif (computer==1 and ask_user==2):
        print("Oops! That's incorrect. You have lost the game. Better luck next time!")
        a=a+1
# elif (computer==2 and ask_user==1):
    # print("Congratulations! You have won the game!")
    elif (computer==2 and ask_user==0):
        print("Oops! That's incorrect. You have lost the game. Better luck next time!")
        a=a+1
    # elif (computer==0 and ask_user==1):
    # print("Congratulations! You have won the game!") 
    elif (computer==ask_user):
    
     print("The game is a draw. Neither player has won.")

    else:
        print("Congratulations! You have won the game!") 
        b=b+1   

if b>a:
    print(f"{user_name} is Winner")   
    
elif a>b:
    print(f"Computer is Winner") 
    
else:
    print("Draw no one is the winner. ") 

