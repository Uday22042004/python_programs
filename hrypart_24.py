#       CLASS METHOD 
class student:
    college=" V.I.T. "
    def __init__(self,name,year):
     self.name=name
     self.year=int(year)
     
    def intro(self,branch):
        print(f"My name is {self.name} and I am pursuing B.tech from vit bhopal . Right now I am in {self.year} year and My branch is {branch}")
        return None
    # @classmethod
    # def change_college(cls,newcollege):
    #     cls.college=newcollege
        
    @staticmethod
    def info_club(club):
        print(f"I have a experience in this club {club} ")
        return None
stud_1=student("Rohan",2)
stud_2=student("Vishal",3)
stud_3=student("Deepak",1)

print(stud_1.intro("Specialization in Aiml"))

print(stud_1.info_club("fine Art "))
print(stud_1.college)

print(stud_2.intro("Specialization in Cyber security"))

print(stud_2.info_club("Cognitive fitness "))
stud_2.college="D.U"
print(stud_2.college)

print(stud_3.intro("Specialization in Cyber security"))

print(stud_3.info_club("Cognitive fitness "))
stud_3.college="IIT"
print(stud_3.college)
# stud_2.change_college("IIT")

# print(stud_2.college)
print(f"student 1{stud_1.college}")
stud_2.college="IIT"
# stud_2.change_college("LNCT")
print(f"student 2 {stud_2.college}")
print(f"student 3{stud_3.college}")
print(f"student 1 {stud_1.college}")

student.college="IIT"
print("joi") 

stud_1=student("Rohan",2)
stud_2=student("Vishal",3)
stud_3=student("Deepak",1)

print(stud_1.intro("Specialization in Aiml"))

print(stud_1.info_club("fine Art "))
print(stud_1.college)

print(stud_2.intro("Specialization in Cyber security"))

print(stud_2.info_club("Cognitive fitness "))
# stud_2.college="D.U"
print(stud_2.college)

print(stud_3.intro("Specialization in Cyber security"))

print(stud_3.info_club("Cognitive fitness "))
# stud_3.college="IIT"
print(stud_3.college)
# stud_2.change_college("IIT")

# class MyClass:
#     class_variable = 0
    
#     def _init_(self):
#         MyClass.class_variable +=1 # yee toh samj aaraha hai par
        
#     def print_class_variable(self):
#         print(MyClass.class_variable)
        

# obj1 = MyClass()
# obj2 = MyClass()

# obj1.print_class_variable() # Output: 2 # yaha pe two kese aa raha hai
# obj2.print_class_variable() # Output: 2
# class Myclass:
#     class_var=0
#     def __init__(self):
        
#         Myclass.class_var +=3
        
#     def print_var(self):
#         print(Myclass.class_var)
        
        
# obj1=Myclass()
# obj1.print_var()
# obj2=Myclass()
# obj3=Myclass()
# obj4=Myclass()
# obj2.print_var() #