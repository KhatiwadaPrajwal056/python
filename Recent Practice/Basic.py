'''

python is a case sensitive language


print('prajwal')
print("hello 'prajwal' zworld")
print('khatiwada')
print('namaste "pk" pkk') or print("nepal 'nepali' pkk")

# Escape Sequence
print('prajwal \'khatiawda\' pk')
print('Line \\n A') or print(r'line \n A')

more Escape Sequences
\' = (')single quote
\" = (")double quote
\\ = backslash
\n= newline
\t = tab 
\b = backspace '  

# Emoji
print('\U0001F607') 
print('\U0001F603') 
print('\U0001F601') 

# Check empty or not
name = input('Enter your name: ')
if name:    # Here string is not empty
        print('Your name is '+ name)
else:
        print('Please enter your name!!')



# playing audio with external mudule
import subprocess    #Subprocess in Python is a module used to run new codes and applications by creating new processes. It lets you     start new applications right from the Python program you are currently writing.               
audio_file = "file path" 
return_code = subprocess.call(["afplay", audio_file]) 

#printing contents of a directory with module os,  this module provides the facility to establish the interaction between the user and the operating system
# import os
# print(os.listdir())                     # gives the list of folders in the dir...
import math
from math import sqrt
from math import *     #every function will be included


num1=1_00_00_00
num2=1_00_00_00
ans=num1*num2
print(f'{ans:,}')

for i in range(4):
        print(i)



# for the multiple integers inputs it can be difficult to take and understand
input() function takes input as a string. For example, if your input is 3 4 5 6 it will take the whole as a string.

input().split() will split the whole string based on the space existing between various elements (note the spaces purposely given in the input above) and return the elements to form a list.

But the elements still are of string type. So we need to typecast each element of the list into integer. So, here the map() function comes into role.

map() function takes 2 parameters, first one a function or data type or a functions and the second one any iterator (list, tuple, or dictionary). i.e map(functions, iterator)

In the above case, map() takes int type and applies int() to every element of the list and finally returned the result into another list
 #taking multiple integer inputs on a single line 
l = map(int,input().split()) 



#Operators
 
5/2=2.5
5//2=2 only integers

# Range
range(5) 



#exception

try: it tries the code as in c++
except: its like a throw and catch but i catches a particular error generated in try block of code, for eg if try block gets valueerror  then except for valueerror is needed . also there can be multiple error on same try and need to make each except for each error '''
try:
        num=int(input("enter a num"))
        print(num)
except ValueError:
        print("You entered different value ")
