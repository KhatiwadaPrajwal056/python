# Dictionary and sets
# Dictionary is a collection of unordered key-value pairs
# keywords cant be expressions
# dict= {
#     "int": "1,2,3",
#     "name":"pk,sagar",
#     "marks":"12,23"
# }
# print(dict['int']) 
'''
#nested dictionary
dict= {
    "int": "1,2,3",
    "name":"pk,sagar ",
    "marks":"12,23",
    "hero" : {"op":"topi"}
}
# print(dict["hero"]) #nested
# print(dict["int"])

#properties::
It is unordered
A dictionary key always has to be mimutable
It is indexed
cannot contain duplicate keys, it overrides i.e need to be unique keys


# Dictionary methods
print("\n")

print(dict.values()) #prints the keys
print(dict.items()) #prints (key,value)
print(dict.keys()) . #prints keys
dict.clear() #clears everything in thr dictionary

dictor ={
    "ok":"3434" ,
    'hi':[3,4,5]
    'ok':"nai nababhhnu la'
}
print(dictor.get('nithin'))  ; prints NONE i.e this avoids error 
OR we can do
print(dictor.get('nothin',20)) ; if it cant find given keyvalur then print 20 i.e default value
dict.update(updateee)   # updates by adding key-value pairs in the dict
dict.update({"oho":"7878"})
print(dict)
print(dict.get("ok"))
print(dict.get("ok2"))  #Returns NONE as ok2 is not present
print(dict["ok2"])  # thorws key error 
.pop()
.popitem()
.update()
.copy()


#Sets In python

a= {1,2,3,4,50,"hghg",50.0}   #empty dict not empty set


#a=set() #empty set
print(type(a))
print(len(a))

a.add(500)
print(a)

# Properties of sets:
# they are unordered
# they are unindexed
# there is no way yo change items in sets
# cannot contain dupicate values

print(len(a))
a.remove(50)
print(a)
print(a.pop())  #removes a random value from the set
print(a)
#a.clear()   #clears the set
print(a.union({7,0}))
print(a.intersection({2}))
'''

dict= {

}
a=input("Enter you fav language p1")
b=input("Enter you fav language p2")
c=input("Enter you fav language p3")
d=input("Enter you fav language p4")
dict["p1"]=a
dict["p2"]=b
dict["p3"]=c
dict["p4"]=d
print(dict) #If the name of keys are same then the new value is set to the key

# set comprehension - less used








