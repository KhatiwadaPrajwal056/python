#Map(): simplifies the code
#Map(function,*iterables)

def mul(li):
    new_li=[]
    for item in li:
        new_li.append(item)
    return new_li

print(map(mul,[1,2,3]))
