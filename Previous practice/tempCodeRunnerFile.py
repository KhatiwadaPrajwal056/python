import random
pc = random.randrange(3)
your = 0
pcs = 0
choose = input('Choose between rock,paper and sissor: ')
over = False
while not over:
        if(choose == 'rock' and  pc == 0):
                pc == 'paper'
                print('You won!')  
                your += 1
                          
        elif(choose=='rock'and pc==1):
                pc=='sissor'
                print('You won!')
                your += 1
                        
        elif(choose=='sissor'and pc==0):
                pc=='paper' 
                print('You won!')
                your += 1
        else:
                if(choose=='rock'and pc==2):
                        pc=='rock'
                        print('Draw!')
                elif(choose=='sissor'and pc==1):
                        pc=='sissor'
                        print('Draw!')
                elif(choose=='paper'and pc == 0):
                        pc=='paper'
                        print('Draw!')
                else:
                        if (pc==2 and choose=='paper'):
                                pc=='rock'
                                print('You loose!')
                                pcs +=1
                        elif (pc==1 and choose=='paper'):
                                pc=='sissor'
                                print('You loose!')
                                pcs +=1
                        elif (pc==2 and choose=='sissor'):
                                pc=='rock'
                                print('You loose!')
                                pcs +=1
        pc = random.randrange(3)                     
        choose = input('Choose between rock,paper and sissor: ')
        if your == 2:
                print('Game over.You won! ')
                over=True
        else:
                if pcs == 2:
                        print('Game over.You loose! ')
                        over=True
        
              
        
                
                