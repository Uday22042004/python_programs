# IN this file we talk about f-string and use of that

#we can use f-str as like a fuction I mean in func. we do like a,b you have to use this and put it
#in space that I give you

# Let us see 
intro="Hey my name is {} and I am from {}"  #here you see this {} will work space 
# where you have to put the value 
intro="Hey my name is {0} and I am from {1}" #here we use this just for our help

country="India"
name="Uday Kelodiya"
print(intro.format(name,country))


#another way to do that or we can say that use of f-string

print(f"Hey my name is {name} and I am from {country}")
#in this we have to use f before your str and in {} you have to tell what you want to put there
txt="the value of pie is {pie:.6f}"
pie=3.14 
print(f"The value of pie is {pie}")
print(txt.format(pie=3.14))