# Functions and recursions
# Functions are the group of statements that performs a specific tasks
'''
def sum(x,y):
    return(x+y)
a,b=map(int,input("enter a num: ").split()) #concept of map is int basic.py file
avg=sum(a,b)/2
print("average is ",avg)

# Greatest among 3
def num(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

x,y,z=map(float,input("enter 3 numbers:").split())
print("greatest among 3 is",num(x,y,z))


#To convert C to F
def convert(c):
    return(c*1.8+32)
cel=float(input("Enter tempr in celcius:"))
print("tempr in fahrenheit is",convert(cel))



#sum of n natural num using recursive
def sum(x):
    if x==0:
        return 0
    else:
        return(x+sum(x-1))
n=int(input("Enter sum up to: "))
print("sum of num is",sum(n))


#Pattern printing 
def patt(a):
    for i in range(1,n):
        for j in range(i,n):
            print(end="* ",)
        print("\n")
n=5
patt(n)
#Or
for i in range(n):
    print("* "*(n-i))


def rem(a,nm):
    if nm in a:
        a=l.replace(nm,"")
        print(a.strip())
    else:
        print("There's no such word in the string ")

l ="    he is a bad boy     "
name=input("Enter a word to remove: ")
rem(l,name)
'''






















