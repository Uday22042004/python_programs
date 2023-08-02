# Doc-string and recursion
#doc-string is like comment but python will ignor comment but for doc it help the user to understand the 
#out of fuct. , and clas, method and more 
def factorial(n):
    '''this will find the factorial of given 
    num and give factorial like 3*2*1 for (3)
    '''#This is a doc string 
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)# this is a recursion when we use fuc.in one fuc 
    #for 3

c=factorial(3)
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(c)

