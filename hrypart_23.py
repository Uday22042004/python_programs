#           STATIC METHOD IN PYTHON
# basically this method do not use self in class 

class Math:
    def __init__(self,num):
        self.num= num
        
    def add_to_num(self,n):
        self.num=self.num+n
        
        
    @staticmethod
    def add(a,b):
        return a+b
    
a=Math(2)
a.add_to_num(3)

#how i can add when i wanto add
print(a.num)


#       # how i can do directly 
print(a.add(2,5)) #


#               INSTANCE AND CLASS VARIABLE


# +=1 se add hota hai  
#                               broooooooooo instance means object yesss

# INSTANCE = yee vo hota hai call karte waqt diya jata hai  #They are defined inside the init method and are usually used to store information that is specific to each instance of the class
#                                                                   a=Math(2)
#                                                                   a.add_to_num(3)

class MyClass:
    class_variable = 0
    
    def __init__(self):
        MyClass.class_variable += 1
        
    # def print_class_variable(self):
    #     print(MyClass.class_variable)
        

obj1 = MyClass()
obj2 = MyClass()

obj1.print_class_variable() # Output: 2
obj2.print_class_variable() # Output: 2