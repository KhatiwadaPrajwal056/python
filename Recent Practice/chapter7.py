#Loops
'''
#While Loop

i=0
while i<10:
    print("yes",i)
    i+=1
 

#Contents of a list
name =["pk","sagar","sarthak"]
i=0
while i<len(name):
    print(name[i])
    i+=1  #Python doesnot supports post and pre increment and decrement


# For loop: control flow statement for specifying iteration. Iteration over a sequence (either list , tupples, dict, set or strings)
name =["pk","sagar","sarthak"]
for item in name:
    print(item) 

#Wowking with ranges in for loop : used to generate a sequence of numbers 
#for i in range(0,5):
   # print(i)
for i in range(0,10,2):  #2 is step size, like i++ ad i-- with partucular numbers of jump
    print(i)

#for with else
for i in range(0,5):
   print(i)
else:
    print("hello") #after the for loop terminates else gets executed , helps in while using break statements
    

for i in range(6):
    print(i)
    if i==5:
        break
else:
    print("hello")

# continus statemet




# pass statement: A null statement
# instructs to do nothing

i=1
if i<2:
    print("Dfdf")
    i=+1
    if(i==2):
        pass 


#Multiplication table


for i in range(1,11):    # For reversing, range(10,0,-1)
    #print("2*"+str(i)+"="+str(2*i))

     print("2*"f'{i}' "="f'{2*i}')


#Whether a num is prime or not
num=int(input("Enter a num "))
prime = True
for i in range(2,num):
    if(num%i==0):
        prime=False
        break
if prime:
    print("Prime")
else:
    print("not"


#Name starts with S
k =["pk","sagar","sarthak"]
for i in k:
    if i.startswith("s"):
        print("hello"+i)



#sum of n natural nums
n=int(input("Enter sum to that num: "))
sum=1
for i in range(n):
    i+=1
    sum=sum*i
print("Total sum is "+ str(sum))



#Patterns
1.
for i in range(1,4):
    for j in range(1,4-i):
        print(end="  ") 
    for k in range(2*i-1):
        print(end="* ")     
        
         # print executes and enters in a new line, the use of end is that it keeps the output cursor of a given string or location
    print("\n") 
2.
for i in range(1,4):
    for j in range(1,i+1):
        print(end="* ")
    print("\n")


3.
for i in range(1,4):
    for j in range(1,4):
        if (i==2 and j==2):
            print(end="  ")
        else:
            print(end="* ")
    print("\n")



4.
for i in range(1,4):
    for j in range(1,4-i):
        print(end="  ")
    for k in range(1,i+1):
        print(end= "* ")
    print("\n")

5.

for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="") 
    for k in range(1,i+1):
        print(end="* ")  
    print("\n")
'''

6.

k=0
for i in range(1,6):
    for j in range(1,i+1):
        print(k+1,end=" ")
        k+=1
    print("\n")


