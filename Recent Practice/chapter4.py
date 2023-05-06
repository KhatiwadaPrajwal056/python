#list and tuples
#list are the containers to store a set of valus of any data types(collection of datatypes)a compplex data type, its like an array
'''
a=[1,5,4,6,8]
x,y,z=a #unpacking
x,y,*other=a 
print(other) #prints everything after x and y 
print(a)

print(a[0:2]) prints 1,5
# slicing of list can also be done same like string slicing
THEY ARE MUTABLE:


#list functions/methods
a.sort() #sorts the list and changes the list i.e returns the sorted list
but sorted(a) only modifies but doesnot changed original list
print(a)
a.reverse() #reverses the lists and return the reversed list
print(a)
a.append(45) # adds at the end of the list and doesnt produces the result it just change the list in end position i.e modifies but doesnt copies
print(a)
a.insert(0,55) #inserts to the list (position, item) : modifies but doesnt copies
print(a)
a.pop(0) #removes element at the given position of the list , if no any index, it removes last item
POP returns whatever it is popped i.e gives the value
print(a)
a.remove(45) #removes the particular element of the list 
Remove doesnt returns the valir ut just modifies
print(a)
a.clear()  #clears entire list
a.index()  #gives the index position of the item
a.count() #count the item repeated

pk='s'
pk.join([]) #joins to end of every word word i.e 's'

# list comprehension 
#square of num to 10:
num=[i**2 for i in range(1,11)]
print(num



# Tuples , It is an immutable (cannot be changed )data type in python, Once a tuples is defined it can't be altered or manipulated
a=(1,2,3) #tuple with numerious elements
x,y,z = a # unpacking
a=() # empty tuple
a=(1) # wrong way to declare tuple with single element
a=(1,) # correct way to declare tuple with single element
b=(3,5,6,8,1,1,1,12,4)
print(b.count(1)) #counts the occurances of the particular element '''


# IMPORTANT:: 

old_list= [
    'prajwal',
    'saimon',
    'potato'
]
new_list=old_list #this doesnt copy the list , oldlist points somewhere in the memory and new list equals to the data to that memory location 
new_list[0]='aalu'
print(new_list)
print(old_list) #hence both print gives the same output

#for copying list :

new_list=old_list[:]