#Use of else in loops 
#first we use for loop 
rm="Jay Shri Ram "
for r in range(1,109):
    for i in rm:
        print(i)
        
else:
    print("Radhe Radhe")
    
#if loop will break then else will not excute 
#same but with break statement 
rm="Jay Shri Ram "
for r in range(1,109):
    for i in rm:
        print(i)
    if r==11:
        break
    
        
else:
    print("Radhe Radhe")
    #here alsso else statement is written but its not excuted because the loop condition is 
    #not false is just break and ekse statement will excute only when loop is stop
    
#Here now we use while loop
rm="Jay shree ram"
i=0
while i<10:
    print(i+1,"position")
    i=i+1
    # if i==3:
    #   mem=["Rahul","Vikas","Harry"]
    #   for m in mem:
    #         print(m)
    #   break   
    
else:
    print("positions are empty")
    
    
#now We use exception handling:


# print("Enter the number : ")
# t=input()
# print(f"The muiltiplication table of {t} is ")


#     # for i in range(1,11):
#     #     print(f"{t} x {i} = {int(t)*i} ")
    
# try:
#     for i in range(1,11):
#      print(f"{t} x {i} = {int(t)*i} ")
     
# except:
#     print("Invaild number is given . Try again")
    
# print("Thank you")


# #    from chatgpt

# try:
#     # Code that may raise an exception
#     ...
# except ExceptionType:
#     # Code to handle the exception
#     ...
# try:
#     # Code that may raise an exception
#     ...
# except ValueError:
#     # Code to handle ValueError
#     ...
# except TypeError:
#     # Code to handle TypeError
#     ...
# try:
#     # Code that may raise an exception
#     ...
# except ValueError:
#     # Code to handle ValueError
#     ...
# except:
#     # Code to handle any other exception
#     ...
# try:
#     # Code that may raise an exception
#     ...
# except ExceptionType:
#     # Code to handle the exception
#     ...
# finally:
#     # Code that will always execute
#     ...


#now we use finally 
def areaofcircle(r):
    
    try:
        print("the circle area is  ",3.14*r**2)
        
    except:
        print("The area of rectangle",r*r)
        
    finally:
        print("The program will executed perfectly")
        
a=areaofcircle("ryan")
print(a)
        
#raise error
a=int(input("enter the number"))
if (a>1 or a<10):
    raise ValueError("value should be 1 be 10")