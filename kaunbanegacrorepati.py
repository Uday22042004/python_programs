name=input("Enter your name : ")
print("\nWelcome",name,"Kaun Banega Crorepati (KBC)")

print("\nThis Quiz is based on your General knowledge as Engineering student ")

money=["Uday", "Ishank","priyanshu"]
print("""\n1.What is the primary goal of the freshman year for an engineering student?
a) To socialize and make new friends
b) To explore different majors
c) To build a strong foundation in fundamental engineering concepts
d) To focus on extracurricular activities""")
one=input()
#
if one=='c':
    print("\nCorrect Answer")
    money.append(5000)
else:
    print("\nWronge Answer")
print("""\n2.Which subjects are commonly included in the freshman year curriculum?
a) Biology and literature
b) Mathematics, history, and sociology
c) Mathematics, physics, chemistry, computer programming, and introduction to engineering courses
d) Art and music appreciation""")
one=input()

if one=='c':
    print("\nCorrect Answer")
    money.append(5000)
else:
    print("\nWronge Answer")
print("""\n3.What is the significance of the term "weed-out courses" for engineering students?
a) Courses focused on horticulture
b) Courses designed to eliminate weak students from the program
c) Courses on environmental sustainability
d) Courses on landscape design""")
one=input()
#
if one=='b':
    print("\nCorrect Answer")
    money.append(5000)
else:
    print("\nWronge Answer")

print("""\n4.What is the purpose of engineering design projects in the freshman year?
a) To showcase creativity
b) To introduce students to the engineering design process and enhance their problem-solving skills
c) To encourage students to pursue art alongside engineering
d) To emphasize theoretical concepts without practical application""")
one=input()
#
if one=='b':
    print("\nCorrect Answer")
    money.append(5000)
else:
    print("\nWronge Answer")

print("""\n5.What resources are typically available for freshman engineering students to seek academic support?
a) Tutoring centers, study groups, and faculty office hours
b) Sports facilities and gyms
c) Music studios and performance halls
d) Cafeterias and food courts""")
one=input()
#
if one=='a':
    print("\nCorrect Answer")
    money.append(5000)
else:
    print("\nWronge Answer")

print("""\n6.What are some common extracurricular activities that engineering students engage in during their freshman year?
a) Drama club and dance teams
b) Business competitions and stock trading
c) Engineering clubs, student organizations, and volunteer work related to engineering
d) Outdoor adventures and hiking clubs""")
one=input()
#
if one=='c':
    print("Correct Answer")
    money.append(5000)
else:
    print("Wronge Answer")

print("""\n7.What is the importance of teamwork in the freshman year for engineering students?
a) It helps in finding a part-time job
b) It is essential for organizing events on campus
c) It prepares students for collaborative work environments and fosters communication and leadership skills
d) It is necessary for participating in sports teams""")
one=input()
#
if one=='c':
    print("Correct Answer")
    money.append(5000)
else:
    print("Wronge Answer")

print("""\n8.What challenges do engineering students often face during their freshman year?
a) Balancing academics and social life
b) Finding a suitable place to live on campus
c) Dealing with financial issues
d) All of the above""")
one=input()
#
if one=='d':
    print("Correct Answer")
    money.append(5000)
else:
    print("Wronge Answer")

print("""\n9.How can engineering students make the most of their freshman year?
a) By attending parties and social events
b) By skipping classes and focusing on personal projects
c) By actively participating in class, seeking help when needed, and getting involved in engineering-related activities
d) By exploring different career options unrelated to engineering""")
one=input()
#
if one=='c':
    print("Correct Answer")
    money.append(5000)
else:
    print("Wronge Answer")

print("""\n10.What is the significance of building a network of peers and mentors during the freshman year?
a) It helps in finding a romantic partner
b) It provides opportunities for joining exclusive clubs on campus
c) It allows for collaboration on homework assignments
d) It provides support, guidance, and future career opportunities for engineering students""")
one=input()
#
if one=='d':
    print("Correct Answer")
    money.append(5000)
else:
    print("\nWronge Answer")
    
total=sum(money)
print("""Congratulation 🎉🎊 
      The total amount you win is """,total,"$")

if total==0:
    print("Sorry better luck next time ")
    
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
    


 


    
    