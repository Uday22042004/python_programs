#In this file we have done some if else condition code 
# eli = int(input("Enter the year of service you have : "))

# if(eli>5):
#     sal = int(input("Enter the Salary of last month in rupees : "))
#     year= int(input("Enter the experience of service you have till now : "))

# as You see below it is example of nested if statements 


num = int(input("Enter the value" ))

if(num<0):
    print("The value is negative .")
elif(num>0):
    if(num<10):
        print("The value is between 1 and 10 ")
    elif(num<20):
        print("The value is between 11 and 20 .")
    else:
        print(" The value is greater than 20 .")
else:
    print("The value is zero 0 ")
    
print("Thank you ")