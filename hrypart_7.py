#Here we are doing Functions with example just to clearify 

def areaofcircle(r):
    print(3.14*r*r)
    return(3.14*r*r)
    
#find the areaof circle of this given radius 9,2,5,7
# areaofcircle(2)
# v=areaofcircle(9)
# # print(v)
# print("The area of circle of radius 9 is " , areaofcircle(9))
# print("The area of circle of radius 2 is " , areaofcircle(2))
# print("The area of circle of radius 5 is " , areaofcircle(5))
# print("The area of circle of radius 7 is " , areaofcircle(7))
#-----
#      This code is for find area of reactangle or circle according to your wish
 #                                                                              ----------#
want=input("Enter the 'R' for area of reactangle and 'C' for area of circle : ")

if (want=="R"):
    # while True:
    #it is just to find the area of rectangle
    
    def areaofreactangle(l,b):
        print("\nThe length of reactangle = ",l)
        print("\nThe breath of reactangle = ",b)
        return(l*b)
    
    l=int(input("\nEnter the length of reactangle : "))  
    b=int(input("\nEnter the breath of reactangle : "))    
  
    print("\nThe area of reactangle is = ",areaofreactangle(l,b))
    
    def diagram(l,b):
        pass  # right now we don't know how to draw a diagram i.e. we write pass we can write this later

elif(want == "C" ):
    
    def areaofcicle(r):
        print("\nThe Radius of circle you give is : ",r)
        return(3.14*r*r)
    
    r=int(input("Enter the radius of cirle : "))
    
    print("\nThe area of circle is ",areaofcicle(r))
    
    
    
else:
    print("""Sorry😔  you give invaild instruction 😔 .
          
          Try Again Please """)
    
print("""\nThank you 😃\n 
         Please give you feedback below """)

print("\nFor Feedback write here 'Feedback'")
feedback=input()
if (feedback=="Feedback"):
    print(" Write here below")
    box=input()
    print(box,"""Thank you for your precious time that you take for Feedback 
      That inspire me to work more.""")
    
else:
    print("""Thank you😃
        
        Have a nice day 🥳""")
