# fibonacci series

num = int(input("Enter a num for the series: "))
a=0
b=1
nextterm=a+b
print("",a,b,end="")
for i in range(num):
    print("",nextterm,end=" ")
    a=b
    b=nextterm
    nextterm=a+b
    
