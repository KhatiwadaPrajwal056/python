# fibonacci series
'''
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
'''

# write a code to find the greatest number in an array: using function 

def greatnum(arr):
    greatest=arr[0]
    for num in arr:
        if greatest<num:
            greatest=num
    return greatest


arr=list(map(int,input("ENter the elements of array: ").split()))
print("THE GREATEST NUMBER IN AN ARRAY IS",greatnum(arr))


