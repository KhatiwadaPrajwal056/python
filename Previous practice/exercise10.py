import random
winning = random.randint(1,100)
times = 1
num = int(input('Enter a number from 1 to 100: '))
over = False
while not over:
        if num == winning:
                print(f'You guessed correct in {times} time.')
                over = True
        else:
                if num > winning:
                        print('Number is high')
                        times += 1
                        num = int(input('Enter again: '))
                else:
                        print('Number is low')
                        times += 1
                        num = int(input('Enter again: '))
        '''
        Or remove line 13,14 & 17,18 then:
        times += 1
        num = int(input('Enter again: ')) '''

# DRY - Don't repeat yourself 
# Line 13 & 14 is repeated in line 17 & 18
        