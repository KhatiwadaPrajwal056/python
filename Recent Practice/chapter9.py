# File handling
'''
#Practice set
#1. Finding a word in a file, whether it is present or not
with open('/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/python course/Code with harry/hellooo.txt','r') as f:
    data=f.read()
    if "hello" in data:
        print("Hello is in file")
    else:
        print("not found")
    f.close()


#2. updating a hi-score of a game if it is crossed

f=open('/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/python course/Code with harry/game.txt','r')
predata=f.read()
if len(predata)==0:   # Just to check whether the file is empty or not
    data=0
else:
    data=int(predata) # Typecasting str=int 
score= int(input("Enter the score: "))
if score>data:
    f.close()
    f=open('/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/python course/Code with harry/game.txt','w')
    print("New high score registered in the file ")
    f.write(str(score))
    f.close
else:
    print("Your score was low ") 

#3.Multiplication table
f=open('/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/python course/Code with harry/tables.txt','w')
for j in range(2,21):
    f.write("Multiplication table for " + str(j)+"\n")
    for i in range(1,11):
        hello=str(j)+"*"+str(i)+"="+str(j*i)+"\n"
        f.write(str(hello))
    f.write("\n")
  
f.close()



#4. To replace particular word 
f=open('/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/python course/Code with harry/replace.txt','r')
data=f.read().lower()
hello="monkey"
data=data.replace("donkey",hello)
f.close()
f=open('/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/python course/Code with harry/replace.txt','w')
f.write(data)
f.close()


#5.To find linenumber of a particular word
data=True
i=1
with open('/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/python course/Code with harry/replace.txt') as f:
    while data :        #will run till all the line are read
        data=f.readline()
        if 'python' in data.lower():
            print(data)
            print("Yes python is present in line number ",i)
        i+=1
    

#6. to check contents of two files are indentical or not

with open('/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/python course/Code with harry/game.txt') as f:
    data=f.read()
with open('/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/python course/Code with harry/hellooo.txt') as f:
    data1=f.read()
if data ==data1:
    print("Identical datas")
else:
    print("Non-identical data")

'''

#7. renaming file name

import os #About os module read in chapter 1

old="/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/python course/Code with harry/game.txt"
new="/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/python course/Code with harry/renamed.txt"
with open(old) as f:
    data=f.read()
with open(new,'w') as f:
    f.write(data)

os.remove(old)





















