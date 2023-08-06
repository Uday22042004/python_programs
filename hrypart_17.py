# #LAMBDA FUNCITON
# cube= lambda x:x**2
# print(cube(4))
# # list = lambda u:u/2

# # print(round(list(8)))

# #MAP FUNTION
# cube = lambda i: i * i * i
# l = [2, 9, 3, 19, 30]
# newlist = list(map(cube, l))
# print(newlist)


# sq_oflist = list(map(lambda x: x * x, l))
# print(sq_oflist)

# #FILTER FUNCTION
# # List of numbers
# # numbers = [1, 2, 3, 4, 5]

# # # Get only the even numbers using the filter function
# # evens = filter(lambda x: x % 2 == 0, numbers)

# # # Print the even numbers
# # print(list(evens))

# students_marks={"Vishal":77,"Guatam":78,"Uday":99,"Piyush":34,"Vikas":23,"Somesh":0.100}
# marks_list=list(students_marks.values())
# passed_student = list(filter(lambda mark : mark>33,marks_list))

# #ITS my example from my understanding 
# age=[23,5,2,66,98,14,64,45,30]
# can_watchmovie=list(filter(lambda x:x>18,age))
# for i in can_watchmovie:
#     print(f"This age can watch movie : {i}")
# num=[2,63,13,20,30,32 ,78,22,13,23]

# evens=list(filter(lambda x:x%2==0,num))
# print(evens)
#REDUCE FUNCITON 

#To use reduce we have import reduce from duntion
# from functools import reduce
# mark=[77,85,88,89,87]

# percent=reduce(lambda x,y:x+y,mark)
# print(percent/5)


# DIFFERENCE BETWEEN is AND == OPERATER
# lets try for constant value or immutable 
a=4
b=4
#here both is and == show same answer 
print(a is b)
print(a ==  b)
#Here we take string
c="hello"
d="hello"
print(c is d)
print(c == d)

#NOw we try for mutable 
a=[1,2,4]
b=[1,2,4]
print(a is  b)#this show false because a and b don't have same space in memory 

print(a ==  b)#this show true becase a and b both hvae same value
