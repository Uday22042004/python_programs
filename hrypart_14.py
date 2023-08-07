# short hand if-else statement
print("To find which number is greater than 'A' and 'B' ")
a=12#int(input("Enter the value of A "))
b=2#int(input("Enter the value of B "))

print("A is greater than B ")if a>b else print("Both numbers are equal ") if a==b else print("B  is greater than A ")

#To use enumerate function:
#to get index value of list , tuple , string 
mala= []
for i in range (1,109,1):
    moti = "Jay Shree Ram"
    mala.append(moti)

for index,time in enumerate(mala):
    print(index+1,time )
    
    
districts = [("Indore", 1818),("Jabalpur", 1822),("Bhopal", 1822),
    ("Ujjain", 1822),
    ("Chhindwara", 1822),
    ("Rewa", 1868),
    ("Gwalior", 1861),
    ("Hoshangabad", 1867),
    ("Sagar", 1861),
    ("Morena", 1866),
    ("Balaghat", 1867),
    ("Vidisha", 1972),
    ("Ratlam", 1947),
    ("Shivpuri", 1972),
    ("Sidhi", 1972),
    ("Chhatarpur", 1972),
    ("Damoh", 1972),
    ("Datia", 1998),
    ("Harda", 1998),
    ("Khandwa", 1998),
    ("Mandla", 1998),
    ("Tikamgarh", 1998),
    ("Narsinghpur", 1998),
    ("Sehore", 1998),
    ("Betul", 2003),
    ("Ashoknagar", 2003),
    ("Seoni", 1998),
    ("Dewas", 1998),
    ("Guna", 2003),
    ("Rajgarh", 1998),
    ("Sheopur", 1998),
    ("Anuppur", 2003),
    ("Agar Malwa", 2013),
    ("Alirajpur", 2008),
    ("Burhanpur", 2003),
    ("Jhabua", 1998),
    ("Katni", 1998),
    ("Mandsaur", 1998),
    ("Neemuch", 1998),
    ("Panna", 1998),
    ("Raisen", 1998),
    ("Shajapur", 2003),
    ("Singrauli", 2008),
    ("Umaria", 1998),
    ("Barwani", 1998),
    ("Dindori", 1998),
    ("Shahdol", 1998),
    ("Anantapur", 2018),
    ("Ashoknagar", 2003),
    ("Singrauli", 2008)]


for index,district in enumerate(districts):
  print(index+1,district)
 
  if (index==1):
      m=districts[index]
      print("First district of Madhya Pradesh")
      print(m)
      

# #To show where you have to work like on which subject and which subject is your strong
  
# n=1
# verify={}
# try:
#  subjects=("English","Hindi", "Physics", "Chemistry","Maths")
#  for subject in subjects:
#     print(f"Enter you mark in {subject} : ")
#     mark=int(input())
#     verify [subject]=mark
#     if (mark<5 or mark>100):
#         raise ValueError("Mark should be between 10 and 100 ")
#     mark_list=verify.values()
    


# except ValueError:
#     print("You enter wronge number or any non-integer value .")
   
# print('Confirm you marks. "press Enter"')
# print(verify)
# confirm= input()
# if confirm == "":
  
#     only_mark=list(mark_list)
#     only_mark.sort()
#     if index,marks in enumerat(only_mark):
#         print
    

# # for mark in range(1,6):
# #     print(f"Enter you mark in {subject} : ")
# #     mark=int(input())
# # while (n<6):
# #     print("Enter your marks ")
# #     print(int(input()))
# #     n=n+1