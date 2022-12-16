'''
# INT FUNCTION
a = int(input('Enter first number '))
b = int(input('Enter second number '))
total = a + b
print('total is ' + str(total))

# str   a --> 'a'
# int   'a'--> a

# float   'a' --> a.0
a = str(5)
b = float('5')
c = int('5')
print(c+b)    #Ans will be in float

# INPUT FUNCTION
# let = input('Enter your name?')    # Input is always taken in string
# print('Hello '+let)
# Age = input('What is age?')
# print('My age is '+ Age)

# Inputing in same line
Name , Age = input('Enter your Name and age ').split()  #Or Split(',')
print(Name)
print(Age)  

#FUNCTION
# Defining function is called parameter and caling is called arguement
name = 'prajwal'
print(len(name))    # Here len is a function 

def pk(a,b):
        return a + b  #Instead of return we can directly use print...but  in real life program return is important
total = pk(5,5)
print(total)
#Also
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
total = pk(a,b)
print(total)
#Or
a = input('Enter first name: ')
b = input('Enter last name: ')
total = pk(a,b)
print(total)  

# Practicing function
# 1. Printing last letter of the user's name
def pk(b):
        return b
a= input('Enter you first name: ')
print(pk(a[-1]))   

# 2. Determining Odd or Even
def a(num):
        if num%2 == 0:
                return 'Number is Even.'
        else:
                return 'Number is Odd' 
# Or:
# def a(num):
#         if num%2 == 0:
#                 return 'Number is Even.'
#         return 'Number is Odd'

# Or(Python way)
def a(num):
     return num%2==0      # This gives True & False, If condition is true so the num is Even else it is odd
b = int(input('Enter a number: '))
print(a(b))    '''

# Without passing parameter in the function
def hi():
        return 'Hello'
print(hi())
        


