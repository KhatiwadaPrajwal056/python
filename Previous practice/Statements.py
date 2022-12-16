# If statement 
'''
age = int(input('Enter your age: '))
if age >= 14:
        print('Your age is above 14')


# Pass Statement ---> It simply passes the program without error
a = 20
if a>20:
        pass   

# If-else statement
a = int(input('Enter a number: '))
if a > 10:
        print('Done! ')
else:
        print('Error')

if a>10 :print('hello') ; print('yuck') 


# If-elif  else statement ---> Used when there are multiple conditions to check
age = int(input('Enter your age: '))
if age == 0 or age < 0 :
        print('Age entered wrong')
elif 0<age<=12 :
        print('You are a child')
elif 12<age<=19 :
        print('You are a teen')
else:
        print('You are an adult') '''


# In keyword ---> To check presence/absence of character in the string
# If with in
name = input('Entr your name: ')
if 'P' or 'p' in name:
        print('P is present')
else:
        print('P is not present')       
                

