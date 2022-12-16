# While Loop
# Examples:
''' i = 1
while i <=2:
        print('Prajwal Khatiwada')
        i += 1

# Sum of the numbers
sum = 0
i = 1
while i <= 5:
        sum += i
        i += 1
print(sum)

# Infinite loop
i = 0
while i <= 10:
        print('Prajwal')     

while True:
        print('PK')   

# For Loop ---> We use range function
# Examples:

# Ranging:
for i in range(2):        #ie 0 to 4 OR range(1,5) ie 1 to 4
        print('Prajwal')

# Sum of natural numbers:
sum = 0
for i in range(int(input('Enter a number: '))):    #ranage is asked from the user(also range will be n-1)
        sum += i
print(sum) 

# Asking user numbers and printing individual sum of them (ie 1234=1+2+3+4)
num = input('Enter numbres: ')
sum = 0
n = len(num)
for i in range(n):
        sum += int(num[i])
print(sum) 

# Exercise 9 (From for loop)
# i.e Counting the numbers of character in the string
name = input('Enter your name: ')
n = len(name)
character = ''
for i in range(n):
        if name[i] in character:
                pass
        else:
                print(f'{name[i]} = {name.count(name[i])}')
                character += name[i] 


# Break Keyword ---> Used to break the loop in between
for i in range(11):
        if i == 5:
                break
        print(i)

# Continue Keyword ---> Used to break the loop in between and continue from the braking point
for i in range(11):
        if i == 5:
                continue     # ---> It Jumps to the for loop rather than printing
        print(i)


# Step Argument in range function
for i in range(2,11,2):
         print(i)

for i in range(10,0,-2):
        print(i) 

# For loop with string
name = 'prajwal'
for i in name:
        print(i) 

num = input('Enter numbers: ')
sum = 0
for i in num:
        sum += int(i)
print(sum)
'''
for i in range(10,0,-2):
        print(i) 






