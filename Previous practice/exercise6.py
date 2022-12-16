name , age = input('Enter your name and age(comma separated): ').split(',')
# age = int(input('Enter your age: '))
if (name[0]== 'P' or name[0] == 'p') and int(age) > 10 :
        print('You can')
else:
        print('You cant')