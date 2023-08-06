#File IO way of manupulating files with python
#READING A FILE
# f=open('hrypart3.py','r')
# print(f)
# # t=f.read() 

# print(f.read())
# # print(t)
# # f.close()


# #WRITING A FILE
# f=open('hrypart3.py','w')


# f.write("Hey bro JAY SHREE RAM")
# f.close()#it is imp becauce it show that your done now you can excute 

# #   APPENDING A FILE 
# f=open('hrypart3.py','a')


# f.write("Hey bro whatsapp jay shree ram  ")
# f.close()#it is imp becauce it show that your done now you can excute 

#USE OF (WITH STATEMENTS) OR we can say alternate way to skip f.close
# with open ("part6.py","r") as f:
#     print(f.read())

#USE OF READLINES 
# f=open('checkreadline.txt','r')
# while True:
#     line=f.readline()
#     if  not line:
#         print("Thats it in that file")
#         break
#     print(line)
    
#ANOTHER EXAMPLE OF READLINES


def assign_grade(percent):
        if percent>=90:
            return "A+"
        elif percent>=80:
            return "A"
        elif percent>=70:
              return "B+"
        elif percent>=60:
              return "B"
        elif percent>=50:
              return "C+"
        elif percent>40:
              return "C"
        elif percent>=35:
              return "D"
        else :
            return "F"
        
f=open("checkreadline.txt","r")
# with open("checkreadline.txt","r")as f:
    # f.readline()
    
while True:
    line=(f.readline())
    # nam=input("Enter your name :- ")
    if not line:
        print("The End")
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    m4=int(line.split(",")[3])
    m5=int(line.split(",")[4])
    
    
    print(f"Your marks in English is {m1} ")
    print(f"Your marks in Hindi is {m2} ")
    print(f"Your marks in Physics is {m3} ")
    print(f"Your marks in Chemistry is {m4} ")
    print(f"Your marks in Maths is {m5} ")
    
    percent=((m1+m2+m3+m4+m5)/5)
    percent=round(percent,2)
    print(f"Your percentage is {percent}")
    
    grade=assign_grade(percent)
    # if percent>90:
    print(f"your grade is {grade}  at {percent}")
    # elif percent<90 and percent>80:
    #         print(f"Your grade is {grade} at {percent}")
    # elif percent<90 and percent>80:
    #         print(f"Your grade is {grade} at {percent}")
    # elif percent<90 and percent>80:
    #         print(f"Your grade is {grade} at {percent}")
    # elif percent<90 and percent>80:
    #         print(f"Your grade is {grade} at {percent}")
    # elif percent<90 and percent>80:
    #         print(f"Your grade is {grade} at {percent}")
    # elif percent<90 and percent>80:
    #         print(f"Your grade is {grade} at {percent}")
            
    
   
    
    
    # def percentage():
        
    #     return sum_mark/500
    # print(line)
    
def assign_grade(percent):
        if percent>=90:
            return "A+"
        elif percent>=80:
            return "A"
        elif percent>=70:
              return "B+"
        elif percent>=60:
              return "B"
        elif percent>=50:
              return "C+"
        elif percent>40:
              return "C"
        elif percent>=35:
              return "D"
        else :
            return "F"