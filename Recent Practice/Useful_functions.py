#Map(): simplifies the code
#Map(function,*iterables)
'''
def mul(li):
    new_li=[]
    for item in li:
        new_li.append(item)
    return new_li

print(map(mul,[1,2,3])) # get map object at the specified location

#To view

def mul(li):
    return li*2
print(list(map(mul,[1,2,3])))  #map will call the function itself and does operation with the data given , also does iterations and converts into list


# Also original list will not change or modify i.e immutable , no side effects of the function and returns a new list '''

#Filter() filters items 
