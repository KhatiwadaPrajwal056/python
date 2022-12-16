 
first_name = 'prajwal '
last_name ='khatiwada'
full_name = first_name + last_name 
print(full_name)
print(full_name + '100') or print(full_name+ str(100))       #you must make it string
print(full_name * 3)

# String Formatting
name = 'prajwal'
age = 18
print('hello {} Your age is {}'.format(name,age))    # Python 3
print(f'Hello {name} Your Age is {age}')             # f=format (Python 3.6)

# String Indexing
Text = 'Prajwal'
print(Text[5])
print(Text[-1])

# String Slicing/selecting sub sequences
# Syntax - [start argument : End argument]
something = 'Hello'
print(something[0:5])   #or [ : ] , [ :5],[0: ]

# Step argument slicing
# Syntax - [start argument : End argument : Step argument]
anything = 'Prajwal'
print(anything[0:7:1])
print(anything[0:7:2])

# Methods in string : part 1
name = 'PrAjWAl KhaTIWaDA'
print(len(name))               # Len function counts total character in the string
print(name.lower())            # Lower method gives string in small character
print(name.upper())            # Upper method gives string in capital character
print(name.title())            # Title method gives 1st character of string in capital & remaining in small
print(name.count('A'))         # Count method counts number of partcular letter in the string

# Methods in string : part 2
# Replace method ---> To replace the strings
# Syntax = ('what to replace','is to replace','number of time to replace')
Prajwal = 'He is dumb and is stupid'
print(Prajwal.replace('is','was'))
print(Prajwal.replace('is','was',1))

# Find method ---> To find the position of the string
me = 'Prajwal is good and he is bad'
print(me.find('is'))      # For first is
print(me.find('is',9))    # For second is 

# Center method ---> To add symbols in the string
name = 'prajwal'
print(name.center(9,'#'))  # total letter in string = 9
name = input('Enter your name: ')
print(name.center(len(name)+4,'*'))















