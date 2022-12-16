name = input('Enter your name: ')
n = len(name)
i = 0
repeatable = ''
while i < n :
        if name[i] not in repeatable:
                repeatable += name[i]
                print(f'{name[i]} = {name.count(name[i])}')
        i += 1     

''' Or
name = input('Enter your name: ')
n = len(name)
i = 0
repeat = ''
while i < n :
        if name[i] in repeat:
                pass

        else:           
                repeat += name[i]
                print(f'{name[i]} = {name.count(name[i])}')
        i += 1 '''