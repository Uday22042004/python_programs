print("If you don't have value of c,d,e then write 0 there .")
print("Enter the value of a : ")
a=int(input())
print("Enter the value of b : " )
b = int(input())
print("Enter the value of c : " )
c = int(input())
print("Enter the value of d : " )
d = int(input())
print("Enter the value of e  : " )
e = int(input())
print("If you want addition then write 1 ")
print("If you want subtration then write 2 ")
print("If you want muiltipication than write 3 ")
print("Write what do you want : ")
h=int(input())


if (h==1):
    
    print("The sum of 'a' and 'b' is : ", a+b+c+d+e)
elif (h==2):
    print("The difference between is : ",a-b-c-d-e)
elif(h==3):
    print("The muiltiplication  is : ",a*b*c*d*e)
else:
    print("Please write any three number between 1,2,3 according to your need. ") 
    
print("Thank  You  🙏🏻 ")
    
