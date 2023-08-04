#This file contain use of list in python 
god =["Shri Ram","Veer Hanuman", "Radhe Radhe ","Ram","preeti"]
# print(len(god))
# print(god[5])
# print(god[0:2])
# print(god[3:])
#print(god[1: ])
# print(god[-2])#we have to always use square bracket for index value
# print(god[len(god)-2])
# print(god[1::2])


#    List comprehension 
name01=[god for god in god if "a" in god]
print(name01)
# forr=[god for god in god if "R" in god]
# print(forr)
print([god for god in god if "R" in god])

#methods of manipulating list
#use of
money=[23,4]
total=sum(money)
print(total)